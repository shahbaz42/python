import os
import datetime

print(os.getcwd()) # get current working directory
# os.chdir('C:/Users/Shahbaz/Desktop/') # change directory
# print(os.getcwd())

print(os.listdir()) # list all files and folders in current directory

# creating a new folder
folder_name = "new_folder"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
else:
    print("Folder already exists!")
# os.makedirs('new_folder/sub_folder') # creates intermediete directories if they don't exist

# renaming a file
# os.rename('new_folder','new_folder2') # renames new_folder to new_folder2

# deleting a folder
# os.rmdir('new_folder/sub_folder') # deletes the sub_folder
# os.removedirs('new_folder/sub_folder') # deletes the sub_folder and new_folder if they are empty

print(os.stat('new_folder')) # prints the stats of new_folder2
print(os.stat('new_folder').st_size) # prints the size of new_folder2

lastUpdated = os.stat('new_folder').st_mtime # prints the last modified time of new_folder2
print(datetime.datetime.fromtimestamp(lastUpdated)) # prints the last modified time of new_folder2 in a readable format

# os.walk() is a generator that yields a tuple of 3 values as it walks the directory tree
for dirpath, dirname, filenames in os.walk('C:/Users/Shahbaz/Desktop/python'):
    print('Current Path:', dirpath)
    print('Directories:', dirname)
    print('Files:', filenames)
    print()

print(os.environ) # prints the environment variables
print(os.environ.get('HOME')) # prints the value of HOME environment variable

file_path = os.path.join(os.environ.get('HOME'),'test.txt') # joins the path of HOME environment variable with test.txt
print(file_path)

print(os.path.basename('/tmp/test.txt')) # prints the base name of the file
print(os.path.dirname('/tmp/test.txt')) # prints the directory name of the file
print(os.path.split('/tmp/test.txt')) # prints both the directory name and the base name of the file

print(os.path.exists('/tmp/test.txt')) # checks if the file exists
print(os.path.isdir('/tmp/test.txt')) # checks if the file is a directory

print(os.path.splitext('/tmp/test.txt')) # splits the file name and the extension

print(dir(os.path)) # prints all the methods in os.path module