import os

current = os. getcwd()
print(current)

file_path = os.path.join(current, "trial. txt")



if os.path.exists(file_path):
     file - open("trial.txt", "r")
     content - file-read()
     print(content)
else:
     print("File not Found")
