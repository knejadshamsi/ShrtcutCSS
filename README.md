# shrtcutCSS

## Description
shrtcutCSS is a Python-based command-line tool that aims to replicate the functionality of TailwindCSS, making styling webpages faster and more efficient. This tool watches a specified HTML file (the "SOURCE" file) and generates CSS code based on the "scc" attribute added to different HTML elements, saving the output to a designated CSS file.

## Backstory
This project was born out of a desire to learn more about Python, its I/O functionalities, and CLI application development. As a personal and deprecated project, shrtcutCSS reflects my journey in exploring web development and Python scripting. It was an experiment to see how the principles of a utility-first CSS framework like TailwindCSS could be interpreted and implemented using Python.

## Features
- **Automatic CSS Generation**: Generates CSS code from HTML elements marked with the "scc" attribute.
- **Customizable Class Name Generation**: Allows choosing the method for generating random class names (`123` or `xyz`).
- **Hot Reloading Option**: Can be enabled to automatically regenerate CSS when changes are made to the source file.

## Installation
shrtcutCSS requires Python. Clone the repository and navigate to the directory containing `shrtcutcli.py`.

## Usage
```
python shrtcutcli.py [SOURCE] [OUTPUT] [--reload] [--genmode {123|xyz}]
```
- `SOURCE`: Path to the HTML file you want to process.
- `OUTPUT`: Path where the generated CSS should be saved.
- `--reload` (`-r`): Enables hot reloading.
- `--genmode`: Choose the method for generating class names (`123` or `xyz`).

Example:
```
python shrtcutcli.py index.html styles.css --genmode 123
```

## Requirements
- Python 3.x
- Click library for Python

## Contributing
While this is a personal and deprecated project, contributions or suggestions are still welcome.