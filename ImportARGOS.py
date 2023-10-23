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