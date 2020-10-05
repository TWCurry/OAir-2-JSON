# Function to convert Open air format files to JSON
import sys, json

outputJson = {}

def OAir2json(asFileContents):
    intro = True
    introText = ""
    for line in asFileContents.splitlines():
        if list(line)[0] == "*": # If line is a comment
            if intro == True:
                introText += f"{line[2:]}\n"
        else:
            if intro == True: # Add intro text section
                outputJson["introText"] = introText
                intro = False

    print(json.dumps(outputJson))


if __name__ == "__main__":
    print("This file is a module only, please run main.py")
    sys.exit(1)