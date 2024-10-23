import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import threading
import os
import re
import hashlib
import traceback
import sys

# Processing Functions (from combined_script.py)

def sanitize_name(name):
    # Remove invalid characters from file and directory names
    return re.sub(r'[<>:"/\\|?*]', '', name).strip()

def generate_unique_id(content):
    # Generate a unique ID based on the content
    return hashlib.md5(content.encode('utf-8')).hexdigest()

def process_file(input_file, temp_file):
    try:
        if os.path.exists(temp_file):
            os.remove(temp_file)
        with open(input_file, 'r', encoding='utf-8') as f, open(temp_file, 'w', encoding='utf-8') as t:
            for line_number, line in enumerate(f, 1):
                # Remove list indicators like numbers, bullets
                line_content = re.sub(r'^[\s\d\.\-]+', '', line).rstrip()
                if line_content:
                    # Write the line preserving the original indentation
                    leading_spaces = len(line) - len(line.lstrip())
                    t.write(' ' * leading_spaces + line_content + '\n')
    except Exception:
        error_msg = f"Error processing file {input_file}: {traceback.format_exc()}"
        raise Exception(error_msg)

def categorize_lines(list_content):
    # Build a hierarchical tree based on indentation levels
    stack = []
    root = {'Children': [], 'ContentLines': [], 'UniqueID': 'root'}

    for line_number, line in enumerate(list_content, 1):
        indent_level = len(line) - len(line.lstrip())
        content = line.strip()

        if not content:
            continue  # Skip empty lines

        # Check if the line is a content line (contains '**')
        is_content_line = '**' in content

        if is_content_line:
            # Content line; append to the last node in the stack
            if stack:
                parent_node = stack[-1]
                parent_node.setdefault('ContentLines', []).append(content)
            else:
                # No parent node; append to root's content lines
                root.setdefault('ContentLines', []).append(content)
            continue

        # Structural node (folder or file)
        unique_id = generate_unique_id(f"{indent_level}_{content}_{line_number}")
        node = {
            'IndentLevel': indent_level,
            'Content': content,
            'Children': [],
            'ContentLines': [],
            'UniqueID': unique_id
        }

        # Determine the parent node based on indentation
        while stack and stack[-1]['IndentLevel'] >= indent_level:
            stack.pop()

        if stack:
            # Add as a child to the current parent node
            parent_node = stack[-1]
            parent_node['Children'].append(node)
        else:
            # No parent node; add to root
            root['Children'].append(node)

        stack.append(node)

    return root

def create_structure(node, parent_path, id_to_path_map):
    # Recursively create directories and .md files based on the hierarchical tree
    for child in node.get('Children', []):
        content = child['Content']
        # Sanitize and limit name length to prevent filesystem issues
        sanitized_name = sanitize_name(content)[:50]
        current_path = os.path.join(parent_path, sanitized_name)

        # Handle name conflicts by appending a unique identifier
        if os.path.exists(current_path):
            sanitized_name += '_' + child['UniqueID'][:6]
            current_path = os.path.join(parent_path, sanitized_name)

        # Store the mapping from unique ID to path
        id_to_path_map[child['UniqueID']] = current_path

        if child['Children']:
            # Create a directory for nodes with children
            os.makedirs(current_path, exist_ok=True)
            # Create an index.md file for the directory
            md_file_path = os.path.join(current_path, 'index.md')
            with open(md_file_path, 'w', encoding='utf-8') as md_file:
                md_file.write(content + '\n')
                # Append any content lines (remove '**')
                for line in child.get('ContentLines', []):
                    cleaned_line = line.replace('**', '')
                    md_file.write(cleaned_line + '\n')
            # Process children
            create_structure(child, current_path, id_to_path_map)
        else:
            # Create an .md file for leaf nodes
            md_file_path = f"{current_path}.md"
            with open(md_file_path, 'w', encoding='utf-8') as md_file:
                md_file.write(content + '\n')
                # Append any content lines (remove '**')
                for line in child.get('ContentLines', []):
                    cleaned_line = line.replace('**', '')
                    md_file.write(cleaned_line + '\n')

    # Append content lines to the current directory's index.md if any
    if node.get('ContentLines') and parent_path != '':
        current_path = id_to_path_map.get(node['UniqueID'], parent_path)
        md_file_path = os.path.join(current_path, 'index.md')
        with open(md_file_path, 'a', encoding='utf-8') as md_file:
            for line in node['ContentLines']:
                cleaned_line = line.replace('**', '')
                md_file.write(cleaned_line + '\n')

def clean_name(name, max_length=16):
    # Split the name into base and extension
    base, ext = os.path.splitext(name)

    # Remove trailing spaces from the base name
    base = base.rstrip()

    # Replace spaces with underscores
    base = base.replace(' ', '_')

    # Truncate the base name to max_length characters
    if len(base) > max_length:
        base = base[:max_length]

    # Return the cleaned name with the original extension
    return base + ext

def rename_items(root_dir, max_length=16):
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        # Rename files
        for filename in filenames:
            old_path = os.path.join(dirpath, filename)
            new_name = clean_name(filename, max_length)
            new_path = os.path.join(dirpath, new_name)

            if old_path != new_path:
                try:
                    os.rename(old_path, new_path)
                except Exception as e:
                    print(f"Error renaming file '{old_path}': {e}")

        # Rename directories
        for dirname in dirnames:
            old_dir = os.path.join(dirpath, dirname)
            new_name = clean_name(dirname, max_length)
            new_dir = os.path.join(dirpath, new_name)

            if old_dir != new_dir:
                try:
                    os.rename(old_dir, new_dir)
                except Exception as e:
                    print(f"Error renaming directory '{old_dir}': {e}")

        # Update dirnames to reflect the renamed directories
        dirnames[:] = [clean_name(d, max_length) for d in dirnames]

def escape_title(title):
    # If the title contains single quotes, use double quotes
    if "'" in title and '"' not in title:
        return f'title: "{title}"\n'
    # If the title contains double quotes, use single quotes
    elif '"' in title and "'" not in title:
        return f"title: '{title}'\n"
    # If the title contains both, escape double quotes
    elif '"' in title and "'" in title:
        escaped_title = title.replace('"', '\\"')
        return f'title: "{escaped_title}"\n'
    else:
        # Default to double quotes
        return f'title: "{title}"\n'

def add_front_matter_to_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Check if the file already has front matter
    if lines and lines[0].strip() == '---':
        # Modify existing front matter if necessary
        front_matter_lines = []
        idx = 1
        while idx < len(lines) and lines[idx].strip() != '---':
            front_matter_lines.append(lines[idx])
            idx += 1
        if idx < len(lines):
            idx += 1  # Skip the closing '---'
        else:
            print(f"Malformed front matter in '{file_path}'.")
            return

        # Parse and fix the front matter
        front_matter_content = ''.join(front_matter_lines)
        if 'title:' in front_matter_content:
            # Extract the title line
            title_line = [line for line in front_matter_lines if line.strip().startswith('title:')][0]
            title = title_line.split('title:', 1)[1].strip().strip('"').strip("'")
            # Escape the title properly
            new_title_line = escape_title(title)
            # Replace the title line
            front_matter_lines = [new_title_line if line.strip().startswith('title:') else line for line in front_matter_lines]
            # Write back the fixed front matter and content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write('---\n')
                f.writelines(front_matter_lines)
                f.write('---\n')
                f.writelines(lines[idx:])
            print(f"Fixed front matter in '{file_path}'.")
        else:
            print(f"No title found in front matter of '{file_path}'.")
        return

    # Extract the first non-empty line as the title
    for line in lines:
        stripped_line = line.strip()
        if stripped_line:
            if stripped_line.startswith('# '):
                title = stripped_line[2:].strip()
            else:
                title = stripped_line
            break
    else:
        title = 'Untitled'

    # Prepare the front matter with proper escaping
    title_line = escape_title(title)
    front_matter = f"---\n{title_line}---\n\n"

    # Write the front matter and original content back to the file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(front_matter)
        f.writelines(lines)

def add_front_matter_to_all_md_files(root_dir):
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.md'):
                file_path = os.path.join(dirpath, filename)
                add_front_matter_to_file(file_path)

# GUI Application

import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import threading

class ProcessingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Markdown Structure Processor")
        self.root.geometry("600x500")

        # Initialize paths
        self.base_dir = None
        self.input_file = None
        self.temp_file_dir = None

        self.create_widgets()

    def create_widgets(self):
        # Input File Selection
        self.file_button = tk.Button(self.root, text="Select Input Markdown File", command=self.select_input_file)
        self.file_button.pack(pady=5)

        # Base Directory Selection
        self.base_dir_button = tk.Button(self.root, text="Select Base Directory (Output)", command=self.select_base_dir)
        self.base_dir_button.pack(pady=5)

        # Temp File Directory Selection
        self.temp_dir_button = tk.Button(self.root, text="Select Temp File Directory", command=self.select_temp_dir)
        self.temp_dir_button.pack(pady=5)

        # Run Processing Button
        self.run_button = tk.Button(self.root, text="Run Processing", command=self.run_processing)
        self.run_button.pack(pady=20)

        # Output Text Area
        self.output_text = scrolledtext.ScrolledText(self.root, height=15, state='disabled')
        self.output_text.pack(pady=10)

    def select_input_file(self):
        self.input_file = filedialog.askopenfilename(filetypes=[("Markdown files", "*.md")])
        if self.input_file:
            self.log(f"Selected input file: {self.input_file}")

    def select_base_dir(self):
        self.base_dir = filedialog.askdirectory()
        if self.base_dir:
            self.log(f"Selected base directory: {self.base_dir}")

    def select_temp_dir(self):
        self.temp_file_dir = filedialog.askdirectory()
        if self.temp_file_dir:
            self.log(f"Selected temp file directory: {self.temp_file_dir}")

    def run_processing(self):
        if not all([self.input_file, self.base_dir, self.temp_file_dir]):
            messagebox.showerror("Error", "Please make all selections.")
            return

        temp_file = os.path.join(self.temp_file_dir, "temp.md")

        # Start the processing in a new thread
        threading.Thread(target=self.execute_processing, args=(self.base_dir, self.input_file, temp_file)).start()

    def execute_processing(self, base_dir, input_file, temp_file):
        try:
            # Process the input file
            self.log("Starting processing...")

            # Create base directory if it doesn't exist
            os.makedirs(base_dir, exist_ok=True)

            # Process the input file to create the temp file
            process_file(input_file, temp_file)

            # Ensure the temp file was created
            if not os.path.isfile(temp_file):
                error_msg = f"Failed to create the temp file {temp_file}."
                self.log(error_msg)
                return

            with open(temp_file, 'r', encoding='utf-8') as f:
                list_content = f.readlines()

            # Build the hierarchy tree
            root = categorize_lines(list_content)

            # Mapping from unique IDs to filesystem paths
            id_to_path_map = {'root': base_dir}

            # Create the folder structure and .md files
            create_structure(root, base_dir, id_to_path_map)

            # Rename files and directories to ensure they meet length requirements
            rename_items(base_dir)

            # Add front matter to all .md files
            add_front_matter_to_all_md_files(base_dir)

            self.log("Processing completed successfully!")

        except Exception as e:
            error_msg = f"An error occurred during processing:\n{str(e)}"
            self.log(error_msg)

    def log(self, message):
        self.output_text.config(state='normal')
        self.output_text.insert(tk.END, message + '\n')
        self.output_text.config(state='disabled')

def main():
    root = tk.Tk()
    app = ProcessingApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
