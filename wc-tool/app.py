import argparse

parser = argparse.ArgumentParser(
    prog="wc tool", description="wc command written in python"
)
parser.add_argument("filename")
parser.add_argument("-c", "--count", action="store_true", help="Count bytes")
parser.add_argument("-l", "--lines", action="store_true", help="Count lines")
parser.add_argument("-w", "--words", action="store_true", help="Count words")

def count_bytes(filename):
    with open(filename, "rb") as f:
        content = f.read()
    return len(content)

def count_lines(filename):
    with open(filename, "r") as f:
        content = f.read()
    return len(content.splitlines())

def count_words(filename):
    with open(filename, 'r') as f:
        content = f.read()

    return len(content.split())

if __name__ == "__main__":
    args = parser.parse_args()
    filename = args.filename

    if args.count:
        print(f"{count_bytes(filename)} {filename}")
    if args.lines:
        print(f"{count_lines(filename)} {filename}")
    if args.words:
        print(f"{count_words(filename)} {filename}")