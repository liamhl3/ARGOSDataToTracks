##---------------------------------------------------------------------
## ImportARGOS.py
##
## Description: Read in ARGOS formatted tracking data and create a line
##    feature class from the [filtered] tracking points
##
## Usage: ImportArgos <ARGOS folder> <Output feature class> 
##
## Created: Fall 2023
## Author: liam.healey@duke.edu (for ENV859)
##---------------------------------------------------------------------


## Import Packages
import sys, os, arcpy


#Set Input Variables
inputFile = 'V:/ARGOSTracking/Data/ARGOSdata/1997dg.txt'
outputFC = 'V/ARGOSTracking/Scratch/ARGOSTrack.shp'


# Construct a while loop to iterate through all lines in the datafile
# Open the ARGOS data file for reading
inputFileObj = open(inputFile,'r')

# Get the first line of data, so we can use a while loop
lineString = inputFileObj.readline()

# Start the while loop
while lineString:
    
    # Set code to run only if the line contains the string "Date: "
    if ("Date :" in lineString):
        
        # Parse the line into a list
        lineData = lineString.split()
        
        # Extract attributes from the datum header line
        date = lineData[3]
        time = lineData[4]
        locationClass = lineData[7]
        
        
        # Print results to see how we're doing
        print ("Date: " +date,"Time: "+time,"Location Class: "+locationClass)
        
    # Move to the next line so the while loop progresses
    lineString = inputFileObj.readline()
    
#Close the file object
inputFileObj.close()
