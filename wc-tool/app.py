import argparse
import sys

parser = argparse.ArgumentParser(
    prog="wc tool", description="wc command written in python"
)
parser.add_argument("filename", nargs='?', default='')
parser.add_argument("-c", "--count", action="store_true", help="Count bytes")
parser.add_argument("-l", "--lines", action="store_true", help="Count lines")
parser.add_argument("-w", "--words", action="store_true", help="Count words")
parser.add_argument("-m", action="store_true")


def count_bytes(content: bytes) -> int:
    return len(content)

def count_lines(content: bytes) -> int:
    return len(content.splitlines())

def count_words(content: bytes) -> int:
    return len(content.split())

def count_chars(content: bytes) -> int:
    return len(content.decode('utf-8-sig')) + 1 # (for Byte Order Mark). Used chardet to check the encoding

def count_all(content: bytes) -> dict:
    return {
        "counts": count_bytes(content),
        "lines": count_lines(content),
        "words": count_words(content)
    }

if __name__ == "__main__":
    args = parser.parse_args()
    filename = args.filename

    if not args.filename:
        content = sys.stdin.buffer.read()
    else:
        with open(args.filename, "rb") as f:
            content = f.read()

    if args.count:
        print(f"{count_bytes(content):8d} {filename}")
    elif args.lines:
        print(f"{count_lines(content):8d} {filename}")
    elif args.words:
        print(f"{count_words(content):8d} {filename}")
    elif args.m:
        print(f"{count_chars(content):8d} {filename}")
    else:
        stats = count_all(content)
        print(f"{stats['lines']:8d}{stats['words']:8d}{stats['counts']:8d} {filename}")