from pathlib import Path

MESSAGE = "fix: made it worse differently"


def main():
    try:
        directory = Path("/output")
        directory.mkdir(parents=True, exist_ok=True)
        target = directory / "entry.txt"
        target.write_text(MESSAGE + "\n", encoding="utf-8")
    except OSError:
        directory = Path("output")
        directory.mkdir(parents=True, exist_ok=True)
        (directory / "entry.txt").write_text(MESSAGE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
