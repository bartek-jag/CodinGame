import re

"""You are provided with a table which associates MIME types to file
extensions. You are also given a list of names of files to be
transferred and for each one of these files, you must find the MIME
type to be used.

The extension of a file is defined as the substring which follows the
last occurrence, if any, of the dot character within the file name.
If the extension for a given file can be found in the association
table (case insensitive, e.g. TXT is treated the same way as txt),
then print the corresponding MIME type. If it is not possible to find
the MIME type corresponding to a file, or if the file doesn’t have an
extension, print UNKNOWN.

Input
Line 1: Number N of elements which make up the association table.
Line 2: Number Q of file names to be analyzed.
N following lines: One file extension per line and the corresponding
MIME type (separated by a blank space).
Q following lines: One file name per line.

For each of the Q filenames, display on a line the corresponding MIME
type. If there is no corresponding type, then display UNKNOWN.
"""

number_of_ext = int(
    input())  # Number of elements which make up the association table.
number_of_files = int(input())  # Number Q of file names to be analyzed.
ext_dict = {}
for i in range(number_of_ext):
    ext, mime = input().split()  # ext: file extension, mime: MIME type
    ext_dict[ext.lower()] = mime

for i in range(number_of_files):
    fname = input()
    fname = re.search("\.[A-Za-z0-9]+$", fname)
    if fname is not None:
        fname = fname.group().split(".")[-1]
        if fname.lower() in ext_dict:
            print(ext_dict[fname.lower()])
            continue
    print("UNKNOWN")
