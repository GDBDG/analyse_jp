from pathlib import Path

SRC_DIR = next(p for p in Path(__file__).parents if p.name == "src")
IMG_GENERATION_CFG_PATH = SRC_DIR / "image_generation" / "plot.cfg"