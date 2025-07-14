'''
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.
'''
text1 = input("Enter text to write to the file: ")
file1 = open("output.txt", "r+")
writing_file1 = file1.write(text1+"\n")
file1.close()
print("Data succesfully written to output.txt")

text2 = input("Enter additional text to append: ")
file1 = open("output.txt", "a")
writing_file2 = file1.write(text2)
file1.close()
file1 = open("output.txt", "r")
reading_file = file1.read()
file1.close()
print("Data succesfully appended")

print("Final content of output.txt:")
print(reading_file)
