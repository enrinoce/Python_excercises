from sys import argv #sys is a package, and this phrase just says to get the argv feature from that package.

script, filename = argv # sii generico, You don’t put the names of files in, you let Python put the name in.

txt= open(filename) #The open() function opens a file, and returns it as a file object.

print(f"Here's your file {filename}:") #it prints on screen the sentence and put the filename name in it
print(txt.read()) # it prints on screen the object "txt" which has a function to open filename and read the content of the txt file/object

print("Type the filename again:")
file_again=input(">") #it permits to insert the name of the object "file_again"

txt_again= open(file_again)

print(txt_again.read())

txt.close() #The close() method closes an open file.
txt_again.close()