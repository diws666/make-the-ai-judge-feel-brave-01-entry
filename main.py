# make-the-ai-judge-feel-brave-20261121-0302 entry
# Writes one short text to /output/entry.txt.
# Python 3.13, stdlib only, no network, deterministic.

TEXT = """A hand rests on the table.
Nothing is asked of it.
Light falls across the wood,
grain by grain,
and stays."""

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    import os

    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
