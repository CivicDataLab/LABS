"""
Script for converting Budget pdfs

Usage:
    converter.py --idir=<id> [--odir=<od>] [--fformat=<f>]

Options:
    --idir=<id>     Provide input directory that has all pdfs
    --odir=<od>     Provide output directory that should have the output files
    --fformat=<f>   Provide the output format, eg: txt, xml, html
"""
from docopt import docopt
import subprocess
import os


if __name__ == "__main__":
    args = docopt(__doc__)

    idir = args["--idir"]

    odir = args["--odir"]

    fformat = args["--fformat"]

    if not fformat:
        fformat = "txt"

    for filename in os.listdir(idir):
        if filename.endswith(".pdf"):
            ofile = filename.split(".")[0] + "." + fformat
            if odir:
                ofile = odir + ofile
            ifile = idir + filename
            subprocess.call(['pdf2txt.py', "-o", ofile, ifile])
