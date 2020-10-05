# OAir-2-JSON
A script to transfer the OpenAir airspace data format into JSON, for use in websites, APIs, anything it may be useful for really.

The main library is contained within OAir2json.py, but there is a wrapper script (main.py) supplied to allow being run manually.

For Python 3.7+

## Usage
### Wrapper Script
`py main.py fileLoc outputLoc`
#### Parameters
* fileLoc: Location of Open Airspace formatted file. Can be either a URL or path
* outputLoc: Location of file to output
### Library Function
Simply import the OAir2Json function, then call it. Pass the input OpenAir formatted text as a string, and the function will return the json (formatted as a python dict).
## Supported Syntax
Unfortunately, OpenAir appears to have no proper standardisation for formats, which makes it pretty difficult to support all possible OpenAir formatted files, since there are so many variations. Overall, they follow a similar structure. Below is the syntax that is supported, this is mostly based of the definition of the OpenAir format at http://www.winpilot.com/UsersGuide/UserAirspace.asp.

* AC _class_
* AN _airspaceName_
* AH _airspaceCeiling_
* AL _airspaceFloor_
* V x=n Variable assignment:
    * D=+/- (sets direction of next arc)
    * X=_coordinate_ (sets the centre of an arc)
* DP _coordinate_ (polygon point)
* DB _coordinate1_ _coordinate2_ (arc between 2 points)
* DC _radius_ circle
## Output syntax
```json
{
    "introText": "Comments at the beginning of the file",
    "sectors": [
        {
            "asType": "A/C/D/E/G/MATZ/ATZ/...",
            "asName": "FICTIONAL ATZ",
            "altMin": "FL05/5000ALT",
            "altMax": "FL06/6000ALT",
            "points": [
                ["lat", "lon"],
                ["lat", "lon"]
                ...
            ],
            "arcs": [
                {
                    "centre": ["lat", "lon"],
                    "arcDir": "clockwise/counterclockwise",
                    "radius": 10
                }
                ...
            ]
        }
    ]
}
```