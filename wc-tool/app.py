import argparse

parser = argparse.ArgumentParser(
    prog="wc tool", description="wc command written in python"
)
parser.add_argument("filename")
parser.add_argument("-c", "--count", action="store_true", help="Count bytes")


def count_bytes(filename):
    with open(filename, "rb") as f:
        content = f.read()

    return len(content)


if __name__ == "__main__":
    args = parser.parse_args()
    filename = args.filename
    if args.count:
        print(f"{count_bytes(filename)} {filename}")
