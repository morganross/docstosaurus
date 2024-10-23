# docstosaurus
Convert Nested List to Folders, Files, and content.

Docstosaurus


Docstosaurus is a Python-based GUI application designed to transform structured Markdown (.md) files into organized directory hierarchies with individual Markdown files. Tailored for developers, writers, and content creators, Docstosaurus simplifies the management of extensive documentation projects by breaking down complex Markdown documents into manageable, interlinked files and folders.

Table of Contents
Overview
Features
Installation
Usage
How It Works
Error Handling
Contributing
License
Contact
Overview
Docstosaurus leverages a user-friendly graphical interface to process Markdown files, creating a structured and sanitized folder and file system that mirrors the logical hierarchy of the original document. This ensures that large documentation sets are easy to navigate, maintain, and collaborate on.

Features
Graphical User Interface (GUI): Built with Tkinter, offering an intuitive interface for selecting files and directories.
Markdown Parsing: Processes Markdown files to remove list indicators and preserve indentation, facilitating hierarchical organization.
Hierarchical Structure Creation: Generates a nested folder structure based on the indentation levels and content of the Markdown file.
File and Directory Sanitization: Cleans names to remove invalid characters and limits name lengths to prevent filesystem issues.
Unique Identification: Assigns unique IDs to files and directories to avoid naming conflicts.
Front Matter Management: Automatically adds or updates YAML front matter in Markdown files for consistent metadata.
Logging: Provides real-time logs within the application to monitor processing steps and errors.
Threaded Processing: Utilizes threading to ensure the GUI remains responsive during long processing tasks.
Installation
Prerequisites
Python 3.6 or Higher: Ensure Python is installed on your system. Download it from python.org.
Required Python Libraries
Docstosaurus relies on Python's standard libraries:

tkinter (Standard with Python)
hashlib (Standard with Python)
re (Standard with Python)
os (Standard with Python)
threading (Standard with Python)
traceback (Standard with Python)
sys (Standard with Python)
No additional installations are required as all dependencies are part of Python's standard library.

Setup
Clone the Repository

bash
Copy code
git clone https://github.com/morganross/docstosaurus.git
Or download the ZIP file and extract it to your desired location.

Navigate to the Project Directory

bash
Copy code
cd docstosaurus
Run the Application

Execute the Python script using the following command:

bash
Copy code
python docstosaurus.py
(Replace docstosaurus.py with the actual filename if different.)

Usage
Launch the Application

After running the script, a GUI window titled "Markdown Structure Processor" will appear.

Select Input Markdown File

Click on the "Select Input Markdown File" button.
Browse and select the .md file you wish to process.
Select Base Directory (Output)

Click on the "Select Base Directory (Output)" button.
Choose the directory where you want the processed folder structure to be created.
Select Temp File Directory

Click on the "Select Temp File Directory" button.
Choose a directory to store temporary files during processing.
Run Processing

After selecting all required paths, click on the "Run Processing" button.
The application will begin processing, and logs will appear in the output area.
Monitor Progress

The Output Text Area displays real-time logs, including success messages and any errors encountered.
Completion

Upon successful completion, the output directory will contain a structured hierarchy of folders and Markdown files based on your input.
How It Works
Input Processing

The selected Markdown file is read and sanitized by removing list indicators (e.g., numbers, bullets) and preserving indentation.
Hierarchy Building

The application analyzes indentation levels to build a hierarchical tree representing the structure of the document.
Directory and File Creation

Based on the hierarchical tree, corresponding directories and .md files are created within the specified base directory.
Each directory can contain an index.md file that serves as an entry point for that section.
Name Sanitization and Conflict Resolution

File and directory names are sanitized to remove invalid characters and trimmed to prevent exceeding filesystem limits.
Unique identifiers are appended to names in case of conflicts.
Front Matter Addition

Each Markdown file is updated to include YAML front matter (metadata) such as the title, ensuring consistency and proper formatting.
Finalization

The application logs the completion status and any pertinent messages for the user to review.
Error Handling
Missing Selections: The application checks if all required paths are selected before starting the processing. If not, it prompts the user to complete the selections.
File Processing Errors: Any errors encountered during file reading, writing, or renaming are logged in the output area with detailed messages.
Front Matter Issues: The tool attempts to fix malformed front matter and will notify the user of any issues encountered during this process.
Filesystem Issues: Handles cases where files or directories cannot be renamed or created due to permissions or existing files.
Contributing
Contributions are welcome! To contribute to Docstosaurus, please follow these steps:

Fork the Repository

Create a New Branch

bash
Copy code
git checkout -b feature/YourFeature
Commit Your Changes

bash
Copy code
git commit -m "Add your feature"
Push to the Branch

bash
Copy code
git push origin feature/YourFeature
Open a Pull Request

Describe your changes and submit the pull request for review.

Please ensure that your contributions adhere to the project's coding standards and include appropriate tests where applicable.

License
This project is licensed under the MIT License.

Contact
For any questions, issues, or feature requests, please open an issue on the GitHub repository or contact morgan.ross@example.com.

Happy Documenting with Docstosaurus! 🦖

Screenshots


Main interface of Docstosaurus showing file and directory selection buttons.



Real-time logging area displaying processing steps and statuses.

Roadmap
Enhanced Front Matter Options: Allow users to customize front matter fields beyond titles.
Support for Other Markup Languages: Extend processing capabilities to formats like reStructuredText or AsciiDoc.
Integration with Static Site Generators: Provide direct integration options with tools like Docusaurus or MkDocs.
Batch Processing: Enable processing of multiple Markdown files simultaneously.
Advanced Error Reporting: Implement more detailed error reports and troubleshooting guides within the app.
