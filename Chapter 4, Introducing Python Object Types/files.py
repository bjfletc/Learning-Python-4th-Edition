'''
File objects are Python code’s main interface to external files on your computer. Files
are a core type, but they’re something of an oddball—there is no specific literal syntax
for creating them. Rather, to create a file object, you call the built-in open function,
passing in an external filename and a processing mode as strings. For example, to create
a text output file, you would pass in its name and the 'w' processing mode string to
write data:
'''

f = open('data.txt', 'w')   # make a new file in output mode
f.write('Hello\n')          # Write strings of bytes to it
f.write('world\n')

f.close()                   # Close to flush output buffers to disk
