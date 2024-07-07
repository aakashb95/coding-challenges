import argparse

parser = argparse.ArgumentParser(
    prog="wc tool", description="wc command written in python"
)
parser.add_argument("filename")
parser.add_argument("-c", "--count", action="store_true", help="Count bytes")
parser.add_argument("-l", "--lines", action="store_true", help="Count lines")

def count_bytes(content):
    with open(filename, "rb") as f:
        content = f.read()
    return len(content)

def count_lines(content):
    with open(filename, "r") as f:
        content = f.read()
    return len(content.splitlines())

if __name__ == "__main__":
    args = parser.parse_args()
    filename = args.filename

    if args.count:
        print(f"{count_bytes(filename)} {filename}")
    if args.lines:
        print(f"{count_lines(filename)} {filename}")
