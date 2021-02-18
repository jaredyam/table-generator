Table Generator - ST3 Plugin
============================

A __Sublime Text 3 plugin__ for converting __CSV-like text__ to other __readable table__ formats __in place__. The converter internal credits to [jaredyam/csv-converter](https://github.com/jaredyam/csv-converter).

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

1. Select the target area with CSV like text. If there is no selection,
all text in the current view will be regarded as the raw data;
2. Open command palette (`ctrl/cmd + shift + P`) and type `Table Generator`;
3. Select a specific converter.

## Supported Commands

|           Command           |        Caption In Command Palette        |
|:---------------------------:|------------------------------------------|
|   `plain_table_generator`   | Table Generator: generate plain table    |
| `markdown_table_generator`  | Table Generator: generate markdown table |
|   `latex_table_generator`   | Table Generator: generate latex table    |

