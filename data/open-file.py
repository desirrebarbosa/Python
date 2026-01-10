def print_content(file):
    with open(file, 'r') as file2:
        file_stuff = file2.read()
        print(file_stuff)


with open('file.txt', 'w') as file1:
    file1.write("This is line 1\n")
    file1.write("This is line B\n")

print_content('file.txt')