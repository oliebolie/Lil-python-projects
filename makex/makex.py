#!/usr/bin/env python3
license = '''
author: Unlisted_dev
contact: unlisted_games27 on discord
Copyright <2024> <Unlisted_dev>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software 
and associated documentation files (the “Software”), to deal in the Software without restriction, 
including without limitation the rights to use, copy, modify, merge, publish, distribute, 
sublicense, and/or sell copies of the Software, and to permit persons to whom the Software 
is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or 
substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING 
BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND 
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, 
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
print("makex version [1.1.2]")
import sys
import os
if len(sys.argv) <= 1:
    sys.exit("makex: No arguments provided, use makex --help for more information")
sys.path[0]
#help
#print(sys.argv)
if len(sys.argv) >= 2:
    file = sys.argv[1]
destination = "/usr/bin"
def makex(file,destination):
    name = file.split("/")[-1]
    name = str(name)
    os.system("cp "+file+" "+destination)
    name = name.removesuffix(".py")
    os.system("mv "+destination+"/"+name+".py "+destination+"/"+name)
    os.system("chmod +x "+destination+"/"+name)
    if os.system("chmod +x "+destination+"/"+name): #Prints if something is returned, as this returns nothing if success
        return(False)
    else:
        return(True)
def helpdialogue():
    print("USAGE: makex [FILE]")
    print("Example: sudo makex /home/username/python/game")
    print("makex: makes a python file runable from terminal")
    print("--IMPORTANT--")
    print("Your python file must have a shebang line.")
    print("A shebang line instructs the program how to run your file")
    print("Add a shebang line such as #!/usr/bin/env python3 on line 1 of your code")
    print("--NOTES--")
    print("-This script will not replace the original file")
    print("-The \"executable\" will still be a python file")
    print("-Any changes made to the original file will need to be updated to the")
    print("\"executable\" by running makex again")
    print("-The executable will be placed in /usr/bin")
    print("-Having errors? run with sudo")
    print("")
    print(license)
    sys.exit()
if file == "--help":
    helpdialogue()
else:
    result = makex(file,destination)
    if not result:
        print("CHECKING CURRENT DIRECTORY")
        result = makex(sys.path[0]+"/"+file,destination)
        if not result:
            sys.exit("ERROR! PERMISSION DENIED OR NO FILE EXISTS")
    if result:
         print("COMPLETE")
