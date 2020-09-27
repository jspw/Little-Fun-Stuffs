import os
import sys
import subprocess as sp
import glob

currentWorkingDir = os.getcwd()

print(currentWorkingDir)

files = [file for file in glob.glob("*.mkv")]


print(files)

for i in range(0,len(files)):

    try:

        sp.call(["ffmpeg", "-i", files[i], "-codec", "copy", files[i]+".mp4"])
        print("\n\nConverting Done!\n")
        sp.call(["rm", "-rf", files[i]])
        print("\n\nDeleted\n")

    except Exception as e:

        sp.call(["sudo", "apt" ,"install", "ffmpeg"])

        print(e)

        try :
            sp.call(["ffmpeg", "-i", files[i], "-codec", "copy", files[i]+".mp4"])
            print("\n\nConverting Done!\n")
            sp.call(["rm", "-rf", files[i]])
            print("\n\nDeleted\n")

        except:
            print("\n\nUnable to convert!\n\n")
