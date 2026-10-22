
import os
from pathlib import Path

REPO_DIR = Path(__file__).resolve().parents[1]

# Name of the shared Drive folder as it appears in "My Drive" (change if you renamed the shortcut)
DRIVE_FOLDER_NAME = "AI & Vis"

if Path("/content/drive/MyDrive").exists():
    DRIVE_DIR = Path("/content/drive/MyDrive") / DRIVE_FOLDER_NAME
else:
    DRIVE_DIR = Path(os.environ.get("AIVIS_DRIVE_DIR", REPO_DIR / "drive_local"))

DATA_DIR = DRIVE_DIR / "data"            # raw dataset audio
PERTURBED_DIR = DRIVE_DIR / "perturbed"  # generated noisy / shifted / mixed audio
BIG_RESULTS_DIR = DRIVE_DIR / "results"  # large outputs (embeddings, attention maps)

RESULTS_DIR = REPO_DIR / "results"       # small CSVs tracked in git
FIGURES_DIR = REPO_DIR / "figures"


def ensure_dirs():
    for d in (DATA_DIR, PERTURBED_DIR, BIG_RESULTS_DIR, RESULTS_DIR, FIGURES_DIR):
        d.mkdir(parents=True, exist_ok=True)
