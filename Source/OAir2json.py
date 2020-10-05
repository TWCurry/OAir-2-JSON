# Function to convert Open air format files to JSON
import sys, json, re

outputJson = {
    "introText": "",
    "sectors": []
}
standardAirspaceClasses = ["A", "C", "D", "E", "G"]

def OAir2json(asFileContents):
    # Get intro
    intro = True
    introText = ""
    for line in asFileContents.splitlines():
        if list(line)[0] == "*": # If line is a comment
            if intro == True:
                introText += f"{line[2:]}\n"
        else:
            if intro == True: # Add intro text section
                outputJson["introText"] = introText
                break
    
    sections = asFileContents.split("*")
    for sector in sections:
        lines = sector.split("\n")
        lines.pop(0) # Remove first element as it will be empty
        if len(lines) > 0:
            if "AC" in lines[0]: # Standard airspace
                asType = lines[0].split(" ")[1]
                asName = lines[1][3:]
                altMin = ""
                altMax = ""
                points = []
                arcs = []
                variables = {
                    "arcDir": "clockwise"
                }
                for line in lines:
                    lineType = line.split(" ")[0]
                    if lineType == "V": # Variable assingment
                        lineParts = line.split(" ")
                        if "D" in lineParts[1].split()[0]: # Arc radius direction
                            if lineParts[1].split()[0] == "D=-":
                                variables["arcDir"] = "counterclockwise"
                            else:
                                variables["arcDir"] = "clockwise"
                        elif "X" in lineParts[1].split()[0]: # Arc centre
                            dmsLat = line.split(" ")[1][2:].split(":")
                            lat = dms2decimal(dmsLat[0], dmsLat[1], dmsLat[2], line.split(" ")[2])
                            dmsLon = line.split(" ")[3].split(":")
                            lon = dms2decimal(dmsLon[0], dmsLon[1], dmsLon[2], line.split(" ")[4])
                            arcs.append({"centre": [lat, lon], "arcDir": variables["arcDir"]})
                    elif lineType == "DP": # Coordinates
                        dmsLat = line.split(" ")[1].split(":")
                        lat = dms2decimal(dmsLat[0], dmsLat[1], dmsLat[2], line.split(" ")[2])
                        dmsLon = line.split(" ")[3].split(":")
                        lon = dms2decimal(dmsLon[0], dmsLon[1], dmsLon[2], line.split(" ")[4])
                        points.append([lat, lon])
                    elif lineType == "DB": # Arc coordinates
                        dmsLat1 = line.split(" ")[1].split(":")
                        lat1 = dms2decimal(dmsLat1[0], dmsLat1[1], dmsLat1[2], line.split(" ")[2])
                        dmsLat2 = line.split(" ")[5].split(":")
                        lat2 = dms2decimal(dmsLat2[0], dmsLat2[1], dmsLat2[2], line.split(" ")[6])
                        dmsLon1 = line.split(" ")[3].split(":")
                        lon1 = dms2decimal(dmsLon1[0], dmsLon1[1], dmsLon1[2], line.split(" ")[4][:-1])
                        dmsLon2 = line.split(" ")[7].split(":")
                        lon2 = dms2decimal(dmsLon2[0], dmsLon2[1], dmsLon2[2], line.split(" ")[8][:-1])
                        arcs[len(arcs)-1]["points"] = [[lat1, lon1], [lat2, lon2]]
                    elif lineType == "AL":
                        altMin = line.split(" ")[1]
                    elif lineType == "AH":
                        altMax = line.split(" ")[1]
                outputJson["sectors"].append({
                    "asType": asType,
                    "asName": asName,
                    "altMin": altMin,
                    "altMax": altMax,
                    "points": points,
                    "arcs": arcs
                })
        
    return outputJson

def dms2decimal(degrees, minutes, seconds, direction):
    decimal = int(degrees) + int(minutes)/60 + int(seconds)/(60*60)
    if direction == 'S' or direction == 'W':
        decimal *= -1
    return decimal

if __name__ == "__main__":
    print("This file is a module only, please run main.py")
    sys.exit(1)