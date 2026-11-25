import os
from os import path

COMMIT_QUIP = "fix: muted the alarm instead of the fire; dashboards are calm"


def _spill(base_dir):
    folder = path.join(base_dir, "output")
    os.makedirs(folder, exist_ok=True)
    destination = path.join(folder, "entry.txt")
    with open(destination, "w", encoding="utf-8") as handle:
        handle.write(COMMIT_QUIP + "\n")


def emit():
    try:
        _spill(os.sep)
    except OSError:
        _spill(os.curdir)


if __name__ == "__main__":
    emit()
