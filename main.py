import os

ENTRY = "The streetlights come on one by one.\nEach switches on without hurrying.\nThe dark does not need to be finished tonight."


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
