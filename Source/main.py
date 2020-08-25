# Script to convert Open air format files to JSON
import sys

def main():
    try:
        fileLoc = sys.argv[1]
    except Exception as e:
        print("Missing parameter, usage:\npy main.py fileLoc\nParameters:\n===========\nfileLoc: Either path to or URL of Open Airspace formatted file.")


if __name__ == "__main__":
    main()