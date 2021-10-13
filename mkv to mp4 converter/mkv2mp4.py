import os
import subprocess as sp
import glob

currentWorkingDir = os.getcwd()

files = [file for file in glob.glob("*.mkv")]

print("\n\nStart converting ...................")

for i in range(0, len(files)):

    try:

        sp.call(["ffmpeg", "-i", files[i], "-codec", "copy", files[i]+".mp4"])
        print("\n\nConverting Done!\n")
        sp.call(["rm", "-rf", files[i]])
        print("\n\nDeleted\n")

    except Exception as e:

        sp.call(["sudo", "apt", "install", "ffmpeg"])

        print(e)

        try:
            sp.call(["ffmpeg", "-i", files[i], "-codec", "copy", files[i]+".mp4"])
            print("\n\nConverting Done!\n")
            sp.call(["rm", "-rf", files[i]])
            print("\n\nDeleted\n")

        except:
            print("\n\nUnable to convert!\n\n")

print("\n\nThank you :D ...................")
