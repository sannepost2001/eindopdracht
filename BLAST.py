import Bio
# from tkinter import Tk, filedialog
from Bio.Blast.NCBIWWW import qblast


def main():
    # tkinter = Tk()
    # tkinter.withdraw()
    # file1 = filedialog.askopenfilename()
    # file2 = filedialog.askopenfilename()

    file1 = "-at-HWI-M02942_file1"  # First reads
    file2 = "-at-HWI-M02942_file2"  # Second reads
    # Figure something out to parse this

    blast(file1, file2)


def blast(file1, file2):
    """Read and BLAST sequence in blast, return results?
    Run once per sequence, over two files? """
    matrix = "BLOSUM62"

    seq = "placeholder"
    result = qblast("blastx", "nr", seq, format_type="Text",
                    expect=(1 * (10 ^ -30)), matrix_name=matrix)
    if not result:
        result = qblast("tblastx", "nr", seq, format_type="Text",
                        expect=(1 * (10 ^ -30)), matrix_name=matrix)
    insert()


def insert():
    """"Insert to database?
    Run once per sequence? """
    pass


# main()


""" Useful:
https://biopython.readthedocs.io/en/latest/Tutorial/chapter_blast.html#parsing-blast-output
"""