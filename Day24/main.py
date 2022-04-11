PLACEHOLDER = "[name]"
def openFile(files):
    with open(files) as file:
        contents = file.read()
    return contents
def writeFile(files, mode, text):
    with open(files, mode) as file:
        file.write(text)
    return True
def readLines(files):
    with open(files) as file:
        contents = file.readlines()
        return contents

with open("Letters/starting_letters.txt") as file:
    contents = file.read()
    for name in readLines("invitedNames/name.txt"):
        newLetter = contents.replace(PLACEHOLDER, name.strip())
        writeFile(f"Letters/Letter_for_{name.strip()}.txt", "w", newLetter)

