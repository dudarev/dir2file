
# d2f

Tool to combine all files in a directory into a single file

## Installation

You can install this tool directly from GitHub using pipx:

```sh
pipx install git+https://github.com/dudarev/dir2file.git
```

Make sure you have [pipx](https://pypa.github.io/pipx/) installed.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history.

```
usage: d2f [-h] [-p [PATH]] [-l] [-e] [-x EXCLUDE [EXCLUDE ...]] [-v] [-d EXCLUDE_DIR [EXCLUDE_DIR ...]]

Tool to combine all files in a directory into a single file

options:
  -h, --help            show this help message and exit
  -p [PATH], --path [PATH]
                        Path to the directory
  -l                    List all files in the directory
  -e                    List all extensions in the directory
  -x EXCLUDE [EXCLUDE ...], --exclude EXCLUDE [EXCLUDE ...]
                        File extensions to exclude
  -d EXCLUDE_DIR [EXCLUDE_DIR ...], --exclude-dir EXCLUDE_DIR [EXCLUDE_DIR ...]
                        Directory names to exclude
  -v, --verbose         Verbose output
```

## Similar projects

- [simonw/files-to-prompt: Concatenate a directory full of files into a single prompt for use with LLMs](https://github.com/simonw/files-to-prompt)
- [artkulak/repo2file: Dump selected files from your repo into single file to easily use in LLMs (Claude, Openai, etc..)](https://github.com/artkulak/repo2file)

Also search alternatives on libhunt. Hint: replace github.com in URLs with libhunt.com.
