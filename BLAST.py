import Bio
# from tkinter import Tk, filedialog
from Bio.Blast.NCBIWWW import qblast


class BLASTer:
    def __init__(self):
        self.seqs_blasted = 0  # Remember position in case BLAST blocks this
        self.database = "nr"
        self.format = "Text"
        self.evalue = 1 * (10 ^ -30)
        self.matrix = "BLOSUM62"
        self.blastmethods = ["blastx", "tblastx"]

    def blast(self, seq):
        result = qblast(self.blastmethods[0], self.database, seq, format_type=self.format,
                        expect=self.evalue, matrix_name=self.matrix)
        if not result:
            for i, _ in enumerate(self.blastmethods):  # Todo: This will result in an out of range error
                result = qblast(self.blastmethods[i+1], self.database, seq, format_type=self.format,
                                expect=self.evalue, matrix_name=self.matrix)
                if result:
                    break

    def save(self):
        """Format (if needed) and save to file or insert into database"""
        pass

def main():
    # tkinter = Tk()
    # tkinter.withdraw()
    # file1 = filedialog.askopenfilename()
    # file2 = filedialog.askopenfilename()

    file1 = "-at-HWI-M02942_file1"  # First reads
    file2 = "-at-HWI-M02942_file2"  # Second reads
    # Figure something out to parse this

    blast(file1, file2)


def readfiles():
    pass


def blast(file1, file2):
    """Read and BLAST sequence in blast, return results?
    Run once per sequence, over two files? """
    database = "nr"
    format = "Text"
    evalue = 1 * (10 ^ -30)
    matrix = "BLOSUM62"

    seq = "placeholder"
    result = qblast("blastx", database, seq, format_type=format,
                    expect=evalue, matrix_name=matrix)
    if not result:
        result = qblast("tblastx", database, seq, format_type=format,
                        expect=evalue, matrix_name=matrix)
    insert()


def insert():
    """"Insert to database?
    Run once per sequence? """
    pass


# main()


""" Useful:
https://biopython.readthedocs.io/en/latest/Tutorial/chapter_blast.html#parsing-blast-output
"""