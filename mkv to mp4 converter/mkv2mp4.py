import os
import subprocess as sp
import glob
from pathlib import Path

currentWorkingDir = os.getcwd()

files = [file for file in glob.glob("*.mkv")]

answer = input("Do you wish original .mkv files to be deleted when finished? [y/N]: ").lower()
if answer in ["n", ""]:
    delete_sources = False
elif answer == "y":
    delete_sources = True
else:
    print("Aborting. Enter a valid answer [y/n]")
    exit(0)

print("\n\nStart converting ...................")

for file in files:
    file = Path(file)
    try:

        sp.call(["ffmpeg", "-i", file, "-codec", "copy", file.with_suffix(".mp4")])
        print("\n\nConverting Done!\n")
        if delete_sources:
            sp.call(["rm", "-rf", file])
            print("\n\nDeleted\n")

    except Exception as e:

        sp.call(["sudo", "apt", "install", "ffmpeg"])

        print(e)

        try:
            sp.call(["ffmpeg", "-i", file, "-codec", "copy", file.with_suffix(".mp4")])
            print("\n\nConverting Done!\n")
            if delete_sources:
                sp.call(["rm", "-rf", file])
                print("\n\nDeleted\n")

        except:
            print("\n\nUnable to convert! Try installing ffmpeg if you don't have it already\n\n")

print("\n\nThank you :D ...................")

