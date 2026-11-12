"""Build every colour system in palette_specs.json into Kolors/palettes/<slug>/.

Run with: python3 -I tools/build_palettes.py
Writes <slug>.md, <slug>.css, <slug>.tokens.json and <slug>.png per system, then the colour and palette indexes.
"""
import shutil
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from PIL import Image, ImageChops  # noqa: E402

from build_indexes import write_indexes  # noqa: E402
from checks import audit, logo_matrix, pairing_cards  # noqa: E402
from library import ROOT, load_colors  # noqa: E402
from render_md import render_markdown  # noqa: E402
from render_sheet import PAGE_BG, render_sheet  # noqa: E402
from render_tokens import render_css, render_json  # noqa: E402
from specs import duplicate_pairs, load_specs, spec_problems  # noqa: E402
from system import build_system  # noqa: E402

PALETTES_DIR = ROOT / "palettes"
STAGING_DIR = ROOT / ".palettes-build"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
SHEET_WIDTH, SHEET_MAX_HEIGHT = 1100, 7000
BOTTOM_MARGIN = 8
RENDER_WORKERS = 4
RENDER_TIMEOUT_S = 90
RENDER_ATTEMPTS = 3


def _build_one(spec):
    hexes = [spec[f"{r}_color"]["hex"] for r in ("primary", "accent", "spark", "ink")]
    system = build_system(*hexes)
    problems = spec_problems(spec, system)
    rows = audit(system)
    failures = [r for r in rows if not r["passes"]]
    if problems or failures:
        detail = problems + [f"{r['theme']} {r['fg']} on {r['bg']} {r['ratio']:.2f}" for r in failures]
        raise ValueError(f"{spec['slug']}: {detail}")
    return system, rows, logo_matrix(spec, system), pairing_cards(system)


def _screenshot(html_path, png_path):
    """Headless Chrome occasionally exits early under parallel load, so retry before failing."""
    error = None
    for _ in range(RENDER_ATTEMPTS):
        with tempfile.TemporaryDirectory() as profile:
            result = subprocess.run(
                [CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--no-first-run", "--no-default-browser-check",
                 "--force-device-scale-factor=1", f"--user-data-dir={profile}", f"--window-size={SHEET_WIDTH},{SHEET_MAX_HEIGHT}",
                 f"--screenshot={png_path}", html_path.as_uri()],
                capture_output=True, text=True, timeout=RENDER_TIMEOUT_S,
            )
        if result.returncode == 0 and png_path.exists():
            return
        error = result.stderr.strip()[-500:]
    raise RuntimeError(f"Chrome could not render {html_path.name} after {RENDER_ATTEMPTS} attempts: {error}")


def _render_png(html_path, png_path):
    _screenshot(html_path, png_path)
    image = Image.open(png_path).convert("RGB")
    background = Image.new("RGB", image.size, PAGE_BG)
    bbox = ImageChops.difference(image, background).getbbox()
    if not bbox:
        raise ValueError(f"Rendered sheet is empty: {png_path}")
    if bbox[3] >= SHEET_MAX_HEIGHT - 1:
        raise ValueError(f"Sheet taller than {SHEET_MAX_HEIGHT}px; raise SHEET_MAX_HEIGHT: {png_path}")
    image.crop((0, 0, SHEET_WIDTH, bbox[3] + BOTTOM_MARGIN)).save(png_path, optimize=True)


def main():
    library = load_colors()
    specs = load_specs(library)
    duplicates = duplicate_pairs(specs)
    if duplicates:
        raise ValueError(f"Near-duplicate systems: {duplicates}")
    built = {spec["slug"]: _build_one(spec) for spec in specs}

    if STAGING_DIR.exists():
        shutil.rmtree(STAGING_DIR)
    STAGING_DIR.mkdir()
    jobs = []
    with tempfile.TemporaryDirectory() as sheets:
        for spec in specs:
            system, rows, matrix, cards = built[spec["slug"]]
            folder = STAGING_DIR / spec["slug"]
            folder.mkdir()
            (folder / f"{spec['slug']}.md").write_text(render_markdown(spec, system, matrix, cards, rows))
            (folder / f"{spec['slug']}.css").write_text(render_css(spec, system))
            (folder / f"{spec['slug']}.tokens.json").write_text(render_json(spec, system))
            html_path = Path(sheets) / f"{spec['slug']}.html"
            html_path.write_text(render_sheet(spec, system, matrix, cards))
            jobs.append((html_path, folder / f"{spec['slug']}.png"))
        with ThreadPoolExecutor(RENDER_WORKERS) as pool:
            list(pool.map(lambda job: _render_png(*job), jobs))
    if PALETTES_DIR.exists():
        shutil.rmtree(PALETTES_DIR)
    STAGING_DIR.rename(PALETTES_DIR)
    write_indexes(library, specs)
    checks = sum(len(rows) for _, rows, _, _ in built.values())
    print(f"Built {len(specs)} systems, {checks} contrast checks passed.")


if __name__ == "__main__":
    main()
