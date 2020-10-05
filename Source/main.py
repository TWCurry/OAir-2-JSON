# Script to convert Open air format files to JSON
import sys, re, requests, json
from OAir2json import OAir2json

def main():
    try:
        fileLoc = sys.argv[1]
    except Exception as e:
        print("Missing parameter, usage:\npy main.py fileLoc\nParameters:\n===========\nfileLoc: Either path to or URL of Open Airspace formatted file.")
        sys.exit(1)

    asFileContents = ""

    if re.match(r"^https?:\/\/.+", fileLoc):
        asFileContents = fetchFileFromURL(fileLoc)
    else:
        asFileContents = readFile(fileLoc)

    jsonOutput = OAir2json(asFileContents)
    print(jsonOutput)
    f = open("output.json", "w")
    f.write(json.dumps(jsonOutput))
    f.close()

def fetchFileFromURL(url):
    print(f"Fetching file from {url}...")
    try:
        r = requests.get(url)
        if r.status_code < 200 or r.status_code > 299:
            raise(f"({r.status_code}) {r.text}")
        else:
            print("Successfully fetched airspace file.")
            return r.text
    except Exception as e:
        print(f"Could not fetch file from {url}\n{e}")
        sys.exit(1)

def readFile(filePath):
    try:
        f = open(filePath)
        fileData = f.read()
        f.close()
        return fileData
    except Exception as e:
        print(f"Could not read file from {filePath} - {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()