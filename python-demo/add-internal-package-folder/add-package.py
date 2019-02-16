"""
This script will demonstrate how to add a package to a system path and call them using `from` and `import`.
"""
import os
import sys


working_dir = os.getcwd()
image_read_write_dir = '/python-demo/add-internal-package-folder'
full_path = working_dir + image_read_write_dir

# Insert path
sys.path.insert(0, full_path)
print(sys.path)

# Calling or importing this function from the specified script will also run the command within them.
from print_stuff import *

# Call internal function from `print_stuff` file.
print_this()

