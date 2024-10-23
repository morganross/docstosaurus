'
# Docstosaurus

Write a nested list and Docstosaurus will convert it to a hierarchy directoiy structure, files and their content.

## Directory Structure

- This is a directory
  - This is a subdirectory
  - This one is too
  - I named this directory &$special folder&$
    - POW This line becomes a file. The lines on the last layer become empty files
    - What Really Files and folders are named after the line they represent, in this case, **What Really Files.md**
    - Unless specified, files are `.MD`
  - Back to Folder
- New Folder!
  - Look At all these folders
  - I love sub folders
    - Files are good too
    - Here is a file
    - By default files are dot em dee
  - Wow sub folder
    - Files are good too
    - Here is a a file called “hiworld.txt” it will have content written in it.
    - **Lets write in this file**
    - **HELLO WORLD**
    - **All 4 of these bold lines are INSIDE the file. Anything bold gets written INSIDE the file. Bold on the list is Content in the file.**
    - **If you want something in your file to actully be bold** just use this instead **#@ipsom dorum#@** becomes bold.

    - What a time to be alive! This is a new empty file! “Specifyname.lol”
    - So long as it's “something.dot.something.in.quotes”
  
  Bullet Points, Numbers, Letters, Roman Numbers, Tabs, spaces, or indent. 

You can even put** nested lists INSIDE of files!!!** ist make it bold!
- lists will help you
- present the key points
- that you want your users to remember
  - and you may nest them
    - multiple times

___for docusaorus you can have internal links for indivual pages, a table of contents for that file will be generated on the top right and the **internal links can be nested!** we love nests! use markdown syntax for h1 and h2 headers
## Headers

will show up on the table of contents on the upper right

So that your users will know what this page is all about without scrolling down or even without reading too much.

## Only h2 and h3 will be in the TOC by default.

You can configure the TOC heading levels either per-document or in the theme configuration.

The headers are well-spaced so that the hierarchy is clear.



![Docstosaurus Logo](https://github.com/morganross/docstosaurus/raw/main/logo.png)

**Docstosaurus** is a Python-based GUI application designed to transform structured Markdown (`.md`) files into organized directory hierarchies with individual Markdown files. Tailored for developers, writers, and content creators, Docstosaurus simplifies the management of extensive documentation projects by breaking down complex Markdown documents into manageable, interlinked files and folders.

**Docstosaurus** allows the user to create a directory structure, files, and thier content from a text document like Word or Google Docs, or any text editor that is hierarchy-aware and saves as Markdown.
Text is sanitized before creating filenames by default, or you can specify exact filesnames inline in the document.

actully it doesnt need markdown at all. it goes by spaces. and allows for imperfections. 
---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Error Handling](#error-handling)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Overview

**Docstosaurus** leverages a user-friendly graphical interface to process Markdown files, creating a structured and sanitized folder and file system that mirrors the logical hierarchy of the original document. This ensures that large documentation sets are easy to navigate, maintain, and collaborate on.

---

## Features

- **Graphical User Interface (GUI)**: Built with Tkinter, offering an intuitive interface for selecting files and directories.
- **Markdown Parsing**: Processes Markdown files to remove list indicators and preserve indentation, facilitating hierarchical organization.
- **Hierarchical Structure Creation**: Generates a nested folder structure based on the indentation levels and content of the Markdown file.
- **File and Directory Sanitization**: Cleans names to remove invalid characters and limits name lengths to prevent filesystem issues.
- **Unique Identification**: Assigns unique IDs to files and directories to avoid naming conflicts.
- **Front Matter Management**: Automatically adds or updates YAML front matter in Markdown files for consistent metadata.
- **Logging**: Provides real-time logs within the application to monitor processing steps and errors.
- **Threaded Processing**: Utilizes threading to ensure the GUI remains responsive during long processing tasks.

---

## Installation

### Prerequisites

- **Python 3.6 or Higher**: Ensure Python is installed on your system. Download it from [python.org](https://www.python.org/downloads/).

### Required Python Libraries

Docstosaurus relies on Python's standard libraries:

- `tkinter` (Standard with Python)
- `hashlib` (Standard with Python)
- `re` (Standard with Python)
- `os` (Standard with Python)
- `threading` (Standard with Python)
- `traceback` (Standard with Python)
- `sys` (Standard with Python)

No additional installations are required as all dependencies are part of Python's standard library.

### Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/morganross/docstosaurus.git
