what if you have a bodyline under a empty folder?'

rename the index using the regular way

if bodylines are indented, will they affect the row heairchay? no, cuse we sanitize

also fix the overwrite issue
# Docstosaurus

Write a nested list and Docstosaurus will convert it to a hierarchy directoiy structure, files and their content.


it doesnt make empty folders

ADD CHECKBOX FOR EMPTY FOLDERS

specify 

that is hard and vert different, new project!

move docusauros logic to seperate part 

(the header stuff), make it more generalized

add the part for roman numeralls and such

ONLY MAKE FILES AT THE DEEPEST INDENATION LEVEL

## Directory Structure

- This line becomes a directory named after this very line
  - This becomes a file/folder whose name would start with This becomes a file/folder
  - File here or folder. If a line has no children, it becomes a file., unless you check allow empty folders
  - Another folder, under /This line becomes/
    - This line becomes a file. The lines on the last layer become empty files.
    - What Really Files and folders are named after the line they represent, in this case, **What Really Files.md**
    - Unless specified, files are `.MD`
  - Back to file, it has no children and is therefore a leaf
- New Folder!
  - Look At all these folders
  - I love sub folders
    - Files are good too
    - 1234 You can have digits in your titles! this is a file @#$%^&*()<>? are okay
    - By default files are dot em dee
  - Wow sub folder
    - Files are good too, this file will end up something Files_are_good.MD 
    - Here is a a file called “hiworld.txt” it will have content written in it.
    - **Lets write in this file**
    - **HELLO WORLD**
    - **All 4 of these bold lines are INSIDE the file. Anything bold gets written INSIDE the file. Bold on the list is Content in the file.**
    - **If you want something in your file to actully be bold** just use this instead **#@ipsom dorum#@** becomes bold.
      - **You can even put nested lists INSIDE of files!!!  just make it bold!**
    - What a time to be alive! This is a new empty file! “Specifyname.lol”
    - So long as it's “something.dot.something.in.quotes”
   
      
-------------------------------------------------------------------------------




  Bullet Points, Numbers, Letters, Roman Numbers, Tabs, spaces, or indent. 

##WORDS
node = a line in the list
leaf = file = a node with no children
brach = direictoy = folder
parent
child
children
sibling
deepest layer
deepest level
hiearrachy
fodler strucutre
nested list







for docusaorus you can have internal links for indivual pages, a table of contents for that file will be generated on the top right and the **internal links can be nested!** we love nests! use markdown syntax for h1 and h2 headers






## Headers

will show up on the table of contents on the upper right

So that your users will know what this page is all about without scrolling down or even without reading too much.

## Only h2 and h3 will be in the TOC by default.

You can configure the TOC heading levels either per-document or in the theme configuration.

The headers are well-spaced so that the hierarchy is clear.




---

#
here is some logic for ALLOW EMPTY FOLDERS


do i have children? 

if yes then folder, if no,

DO ANY OF MY SIBLINGS HAVE CHILDREN? 

if yes then file, if not  then folder

this prevents the creation of a set of empty subfolders unless one subfolder contains at least one file or subfolder
fix is just to put one empty file at the bottom of a directory structure, or to specify a "fixer empty file to be deleted" line as a child of empty parent ditory in a direcotry of childess folders



specifty to make empty folder

