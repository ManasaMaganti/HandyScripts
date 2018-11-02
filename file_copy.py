import os
import re

src_dir = input("Enter src_dir: ")
dst_dir = input("Enter dst_dir: ")
yes = ["Yes", "YES", "yes", "y"]
if not re.match(r"^\w:[\\\w]+[^\\]+\\$", src_dir) or not re.match(r"^\w:[\\\w]+[^\\]+\\$", dst_dir):
    print("Path is not in the correct form (or)'\\' is missing.")
else:
    # Ask user if he wants to transfer all or some files
    c = 1
    d = {}
    for file in os.listdir(os.path.abspath(src_dir)):
        print(str(c) + ". " + file)
        d[str(c)] = file
        c += 1
    ask = input("The Above files have been found. Do you want to move all of them to " + dst_dir + "? (y/n)")
    if ask in yes:
        for file in os.listdir(os.path.abspath(src_dir)):
            os.rename(src_dir + file, dst_dir + file)
            print(file + " moved.")
        print("You have moved all files.")
    else:
        ask = input("Which files do you want to move(separate numbers with ',')?: ")
        li = [x for x in ask.split(",")]
        for x in li:
            print(d[str(x)])
        if input("Are you sure you want to move these files?") in yes:
            for x in li:
                os.rename(src_dir + d[str(x)], dst_dir + d[str(x)])
            print("Above files have been moved.")
        else:
            print("Move Cancelled.")
