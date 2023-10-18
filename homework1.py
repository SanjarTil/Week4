fname = input("Enter file name: ")
try:
    fhand = open(fname, "r")
    line = fhand.read()
    print(line.upper())
    fhand.close()
except FileNotFoundError:
    print("File with this name doesn't exist!")

