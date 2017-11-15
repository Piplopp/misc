#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    This script is designed to convert Robotguide waypoints to URScript

    usage: python3 robotguide2urscript.py --input FILE

    @author Jerome Pivert <pivertjerome@gmail.com>
"""

##########
# Import #
##########
import argparse
import re
import itertools
import os

# Some colors
C_FILE = '\033[95m'
C_WARNING = '\033[93m'
C_FAIL = '\033[91m'
C_ENDC = '\033[0m'

##############
# CLI PARSER #
##############
def cli():
    """ Create and populate the cli parser"""
    parser = argparse.ArgumentParser(
        usage       = "./%(prog)s [-h] [-i <FILE>] \n",
        description = "Convert Robotguide waypoints to URscript",
        formatter_class = argparse.ArgumentDefaultsHelpFormatter
    )

    # Args
    parser.add_argument('-i', '--input',
        metavar = 'file',
        type = existant_file,
        help = 'The robotguide file containing the waypoints to convert to URscript',
        required=True
    )

    return parser.parse_args()

def existant_file(filepath:str):
    """Argparse type, raising an error if given file does not exists"""
    if not os.path.exists(filepath):
        raise argparse.ArgumentTypeError(
            " file {} doesn't exists".format(C_FILE + filepath + C_ENDC)
        )
    return filepath

if __name__ == "__main__":
    args = cli()
    INFILE = args.input
    OUTFILE = os.path.splitext(INFILE)[0] + '.script'
    while True:
        move = str(input("Quel type de mouvement (movep, movel, movea) ?: ").strip().lower())
        if move not in ['movep', 'movel', 'movea']:
            print(C_FAIL + "Mouvement " + C_ENDC + move + C_FAIL + " non reconnu, veuillez choisir parmis: movep, movel, movea" + C_ENDC)
        else:
            break
    a = float(input("Entrez la valeur a= ").strip())
    v = float(input("Entrez la valeur v= ").strip())
    r = float(input("Entrez la valeur r= ").strip())

    positions = list()
    angles = list()

    # Get the values from robotguide files
    pattern_pos = re.compile("[XYZ]\s+=\s+(-?\d*\.\d+)\s+mm")
    pattern_ang = re.compile("[WPR]\s+=\s+(-?\d*\.\d+)\s+deg")
    with open(INFILE) as f:
        for line in f:
            line = line.strip()
            if pattern_pos.match(line):
                positions.append([float(x) for x in re.findall(pattern_pos, line)])
            elif pattern_ang.match(line):
                angles.append([float(x) for x in re.findall(pattern_ang, line)])

    # Check if both lists have the same length
    if len(angles) != len(positions):
        raise ValueError("Length of angles and positions lists are not equal")

    # Create the urscript lines
    with open(OUTFILE, 'w') as out:
        for i, j in zip(positions, angles):
            urscript_line = (
                move + '(p' + str(i+j)
                + ', a=' + str(a)
                + ', v=' + str(v)
                + ', r=' + str(r) + ')\n'
            )
            out.write(urscript_line)
