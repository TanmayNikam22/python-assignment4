'''
 Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist
'''
try:
    file1 = open("sample.txt", "r")
    reading_file = file1.read()
    print("Reading file content:")
    print(reading_file)
    file1.close()
except FileNotFoundError:
    print("Error: The file 'simple.txt' was not found.")
