# syntax: name = open(name/directory, mode)

file1 = open('file.txt', 'r')

# you need to close the file after being used
file1.close

# automatically close the file with with
with open('file.txt', 'r') as file:
    file_stuff = file.read()

    print(file_stuff)