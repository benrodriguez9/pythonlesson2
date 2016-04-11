# Lesson 3.2: Use Functions
# Mini-Project: Secret Message

# Your friend has hidden your keys! To find out where they are,
# you have to remove all numbers from the files in a folder
# called prank. But this will be so tedious to do!
# Get Python to do it for you!

# Use this space to describe your approach to the problem.
#
#
#
#

# Your code here.
import os
def rename_files():
    file_list = os.listdir("/Users/superben9/Desktop/udacitylearntocode/workshop3python/pythonlesson3/prank")
    print(file_list)
    os.chdir("/Users/superben9/Desktop/udacitylearntocode/workshop3python/pythonlesson3/prank")
    print(file_list)
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))

rename_files()


