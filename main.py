import os

ENTRY = """The kettle sings, then stops.
The water settles in its own time.
One bubble rises, then another,
each one quiet, rising,
and the steam thins
until the spout is dry again.
"""


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
