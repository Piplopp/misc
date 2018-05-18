#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    This script is designed for Pierre Digirolamo to convert his GPS location
    files from Degrees Minutes Seconds to Decimal Degrees

    usage: python3 DMS2DD.py

    @author pivertjerome@gmail.com
"""

from tkinter import Tk
from tkinter.filedialog import askopenfilename
import re
import codecs
import os

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
INFILE = askopenfilename() # show an "Open" dialog box and return the path to the selected file


# extract GPS Degrees minutes and seconds from:
# "6°40'15.29"" E	45°30'02.24"""" N	Verdons1"""
# group 1,4: Degrees
# group 2,5: minutes
# group 3,6: seconds
# group 7:   identifier
reg = re.compile(r"^\"(\s*\-?\s*?\d+).(\d+)\'(\d+\.?\d*)\"{2}\s+[EWSN]\s+(\s*\-?\s*?\d+).(\d+)\'(\d+\.?\d*)\"{4}\s+[EWSN]\s+(.+)\"{3}$")
line_count = 0
new_file_content = [str(line_count)+";;;"]

for line in codecs.open(INFILE, 'r', 'iso-8859-1'):
    match = reg.match(line.strip())

    if match:
        line_count += 1
        if int(match.group(4)) > 0:
            dd1 = round(float(match.group(4)) + (float(match.group(5))/60) + (float(match.group(6))/3600), 6)
        else:
            dd1 = round(float(match.group(4)) - (float(match.group(5))/60) - (float(match.group(6))/3600), 6)
        if int(match.group(1)) > 0:
            dd2 = round(float(match.group(1)) + (float(match.group(2))/60) + (float(match.group(3))/3600), 6)
        else:
            dd2 = round(float(match.group(1)) - (float(match.group(2))/60) - (float(match.group(3))/3600), 6)

        alphanums = re.compile(r'[\W_-]+')
        identifier = alphanums.sub('', match.group(7))
        new_line = ';'.join([str(line_count), identifier, str(dd1), str(dd2)])
        new_file_content.append('\n'+new_line)

with open("converted_"+os.path.basename(INFILE), 'w') as OUTFILE:
    for i in new_file_content:
        OUTFILE.write(i)
