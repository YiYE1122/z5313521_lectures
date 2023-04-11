""" lec_fileio.py

Companion codes for the lecture on reading and writing files
"""

import os

import toolkit_config as cfg


SRCFILE = os.path.join(cfg.DATADIR, 'qan_prc_2020.csv')
DSTFILE = os.path.join(cfg.DATADIR, 'new_file.txt')
fobj = open(SRCFILE, mode='r')
# We can get the entire content of the file by calling the method `.read()`,
# without parameters:
cnts = fobj.read()

# The variable `cnts` will be a string containing the full contents of the
# file. This will print the first 20 characters:
print(cnts[:20])

# Output:
#  Date,Open,High,Low,C

# ----------------------------------------------------------------------------
#   Comparing different approaches to get the contents
# ----------------------------------------------------------------------------
# Remember that we previously closed the file so we need to open it again
fobj = open(SRCFILE, mode='r')
# Contents using `.read`
cnts = fobj.read()
print(f"First 20 characters in cnts: '{cnts[:20]}'")


# Start with an empty string
cnts_copy = ''
# Iterate over each line of fobj
for line in fobj:
    # Add this line to the string `cnts_copy`
    cnts_copy += line

# Print the result
print(f"First 20 characters in cnts_copy: '{cnts_copy[:20]}'")

# Close the file
fobj.close()


def print_lines(pth):
    """ Function to print the lines of a file
    Parameters
    ----------
    pth : str
        Location of the file
    Notes
    -----
    Each line in the file will be printed as
        line number: 'string with the line text'
    """
    with open(pth) as fobj:
        for i, line in enumerate(fobj):
            print(f"line {i}: {line}")


#  This will create the file located at `DSTFILE` and write some content to it
with open(DSTFILE, mode='w') as fobj:
    fobj.write('This is a line')

# Exiting the context manager will close the file
# We can then print its contents
print_lines(DSTFILE)

with open(DSTFILE, mode='w') as fobj:
    fobj.write('This is another line')

print_lines(DSTFILE)