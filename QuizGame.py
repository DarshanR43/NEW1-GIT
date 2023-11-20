import os
# create new file
file_path="path/to/renamed_file.txt"
with open(file_path,"w") as file:
	(file.write("this is the file"))

# get the file path:
print("file path:",os.path.abspath(file_path))

# get the directery of the file
print("Directory:",os.path.dirname(file_path))


# list files in the directory
# directery = os.path.dirname(file_path)
# files=os.listdir(directory)
# print("Files in directory",files)

# rename:
# new-file_path="path/to/renamed_file.txt")


# check if the file exists
if os.path.exists(file_path):
	print("F E")

# delete the file
# os.remove(new_