import argparse

parser = argparse.ArgumentParser(
    prog="wc tool", description="wc command written in python"
)
parser.add_argument("filename")
parser.add_argument("-c", "--count", action="store_true", help="Count bytes")
parser.add_argument("-l", "--lines", action="store_true", help="Count lines")
parser.add_argument("-w", "--words", action="store_true", help="Count words")
parser.add_argument("-m", action="store_true")

def open_file(filename, mode='r'):
    with open(filename, mode) as f:
        content = f.read()
    return content

def count_bytes(filename):
    content = open_file(filename, mode='rb')
    return len(content)

def count_lines(filename):
    content = open_file(filename)
    return len(content.splitlines())

def count_words(filename):
    content = open_file(filename)
    return len(content.split())

def count_chars(filename):
    with open(filename, 'rb') as f:
        content = f.read()
    return len(content.decode('utf-8-sig')) + 1 # (for Byte Order Mark). Used chardet to check the encoding

if __name__ == "__main__":
    args = parser.parse_args()
    filename = args.filename

    if args.count:
        print(f"{count_bytes(filename)} {filename}")
    if args.lines:
        print(f"{count_lines(filename)} {filename}")
    if args.words:
        print(f"{count_words(filename)} {filename}")
    if args.m:
        print(f"{count_chars(filename)} {filename}")