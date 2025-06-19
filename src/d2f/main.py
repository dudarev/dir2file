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
    parser.add_argument(
        "-d", "--exclude-dir", nargs="+", help="Directory names to exclude"
    )

    return parser.parse_args()


def list_files(args: argparse.Namespace) -> None:
    files = get_files(args)
    for f in files:
        print(f)


def list_extensions(args: argparse.Namespace) -> None:
    files = get_files(args)
    extensions = set()
    for f in files:
        extensions.add(f.suffix.replace(".", ""))
    if args.verbose:
        print(f"All extensions in {args.path}:")
    print("\n".join(extensions))


def get_filename_extension(filename: str) -> str:
    return os.path.splitext(filename)[1].replace(".", "")


def get_files(args: argparse.Namespace) -> list[Path]:
    extensions_to_exclude = args.exclude or []
    directories_to_exclude = args.exclude_dir or []
    files = []
    for dirpath, dirnames, filenames in os.walk(args.path):
        # Exclude directories by checking if any part of the path is in directories_to_exclude
        if any(
            excluded_dir in Path(dirpath).parts
            for excluded_dir in directories_to_exclude
        ):
            continue
        for filename in filenames or []:
            if filename.startswith("."):
                continue
            if get_filename_extension(filename) not in extensions_to_exclude:
                files.append(Path(dirpath) / filename)
    if args.verbose:
        print(
            f"All files in {args.path} excluding {args.exclude} and directories {args.exclude_dir}:"
        )
    return files


def combine_files(files: list[Path]) -> None:
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
