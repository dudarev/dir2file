"""
Tool to combine all files in a directory into a single file
"""

import argparse
import os
from pathlib import Path
import sys


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Tool to combine all files in a directory into a single file"
    )

    parser.add_argument(
        "-p", "--path", nargs="?", default=os.getcwd(), help="Path to the directory"
    )

    parser.add_argument(
        "-l", action="store_true", help="List all files in the directory"
    )
    parser.add_argument(
        "-e", action="store_true", help="List all extensions in the directory"
    )
    parser.add_argument("-x", "--exclude", nargs="+", help="File extensions to exclude")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")

    return parser.parse_args()


def list_files(args: argparse.Namespace) -> list[Path]:
    files = get_files(args)
    for f in files:
        print(f)


def list_extensions(args: argparse.Namespace):
    files = get_files(args)
    extensions = set()
    for f in files:
        extensions.add(f.suffix.replace(".", ""))
    if args.verbose:
        print(f"All extensions in {args.path}:")
    print("\n".join(extensions))


def get_filename_extension(filename: str) -> str:
    return os.path.splitext(filename)[1].replace(".", "")


def get_files(args: argparse.Namespace) -> list[str]:
    extensions_to_exclude = args.exclude or []
    files = []
    for dirpath, dirnames, filenames in os.walk(args.path):
        for filename in filenames or []:
            if filename.startswith("."):
                continue
            if get_filename_extension(filename) not in extensions_to_exclude:
                files.append(Path(dirpath) / filename)
    if args.verbose:
        print(f"All files in {args.path} excluding {args.exclude}:")
    return files


def combine_files(files: list) -> None:
    for file in files:
        print(f"{file}:\n\n")
        print(Path(file).read_text())
        print(40 * "-")


def main():
    args = parse_args()

    if args.l:
        list_files(args)
        sys.exit(0)

    if args.e:
        list_extensions(args)
        sys.exit(0)

    files = get_files(args)

    combine_files(files)


if __name__ == "__main__":
    main()
