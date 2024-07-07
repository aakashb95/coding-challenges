import argparse

parser = argparse.ArgumentParser(
    prog="wc tool", description="wc command written in python"
)
parser.add_argument("filename")
parser.add_argument("-c", "--count", action="store_true", help="Count bytes")


def count_bytes(content):
    return len(content)

if __name__ == "__main__":
    args = parser.parse_args()
    filename = args.filename
    with open(filename, "rb") as f:
        content = f.read()

    if args.count:
        print(f"{count_bytes(content)} {filename}")
