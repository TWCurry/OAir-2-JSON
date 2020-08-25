# Script to convert Open air format files to JSON
import sys, re, requests

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

def fetchFileFromURL(url):
    print(f"Fetching file from {url}...")
    try:
        r = requests.get(url)
        if r.status_code < 200 or r.status_code > 299:
            raise(f"({r.status_code}) {r.text}")
        else:
            return r.text
    except Exception as e:
        print(f"Could not fetch file from {url}\n{e}")

def readFile(filePath):
    raise NotImplementedError


if __name__ == "__main__":
    main()