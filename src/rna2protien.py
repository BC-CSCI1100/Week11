# CSCI 1100 Gateway to Computer Science
#
# An mRNA to Protein Translation, from rosalindo.info
#
# Run: python3 rna2protein.py mRNAsequence

import sys

# start : unit -> unit
def start():
    if len(sys.argv) < 2:
        print("run: python3 rna2protein.py mRNAsequence")
        print("Codon table should be in local file codontable.txt")
        exit(1)
    codonTable = makeCodonTable()
    mRNA = sys.argv[1]


start()
