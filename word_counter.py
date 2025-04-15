import os

file = str(input("Enter file name:"))

if os.path.exists(file):
    with open(file, "r") as f:
        content  = f.read()
        words = content.split()
        number_of_words = len(words)
        print(f"There are {number_of_words} words in {file} file.")
else:
    print("File doesnot exist")