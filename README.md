Table Generator - ST3 Plugin
============================

A __Sublime Text 3 plugin__ for converting __CSV-like text__ to other __readable table__ formats __in place__. The converter internal is a fork from [jaredyam/csv-converter](https://github.com/jaredyam/csv-converter).

__DEMO:__
![demo-gif](https://user-images.githubusercontent.com/50312506/108337617-43f36580-7210-11eb-9c2c-37370384e830.gif)


## Installation

Clone the repository in your Sublime Text "Packages" directory:

```bash
git clone https://github.com/jaredyam/table-generator.git
```

e.g. the "Packages" directory on macOS is located at:

```bash
~/Library/Application Support/Sublime Text 3/Packages/
```

Then execute `install.sh` script for downloading the dependent package:

```bash
$ sh install.sh
```

## Usage

1. Select a target area covering the CSV-like text. If there is no selection,
all text in the current view will be regarded as the raw data;
2. Press `ctrl/cmd + shift + P` to bring up the `command palette`;
3. Type `Table Generator` into the `command palette`;
4. Select a specific converter and press `Enter`.

## Supported Commands

|           Command           |        Caption In Command Palette        |
|:---------------------------:|------------------------------------------|
|   `plain_table_generator`   | Table Generator: generate plain table    |
| `markdown_table_generator`  | Table Generator: generate markdown table |
|   `latex_table_generator`   | Table Generator: generate latex table    |

