import Bio
import mysql.connector
# from tkinter import Tk, filedialog
from Bio.Blast.NCBIWWW import qblast

host = "hannl-hlo-bioinformatica-mysqlsrv.mysql.database.azure.com"
user = "kxxxf@hannl-hlo-bioinformatica-mysqlsrv"
passw = "ConnectionPWD"
dbname = "kxxxf"
database = mysql.connector.connect(host=host, user=user, password=passw, db=dbname)
cursor = database.cursor()


class BLASTer:
    def __init__(self):
        self.seqs_blasted = 0  # Remember position in case BLAST blocks this (Unfinished feature)
        self.database = "nr"
        self.format = "Text"
        self.evalue = 1 * (10 ^ -30)
        self.matrix = "BLOSUM62"
        self.blastmethods = ["blastx", "tblastx"]

    def blast(self, seq):
        for i, blastmethod in enumerate(self.blastmethods):
            result = qblast(self.blastmethods[i], self.database, seq, format_type=self.format,
                            expect=self.evalue, matrix_name=self.matrix)
            if result:
                self.seqs_blasted += 1
                return result

    def save(self, header, read, seq, data):  # Todo: Need to finish based on final database design
        """Format (if needed) and save to file or insert into database"""
        columns = "Header, Read, Sequentie, andere dingen"
        # Todo: Rest of columns here
        values = ""
        values += (header)
        values += (", " + read)
        values += (", "+seq)
        query = "insert into table(columns) values ("+values+")"
        cursor.execute(query)
        pass


def main():
    file1 = "-at-HWI-M02942_file1"  # First reads
    file2 = "-at-HWI-M02942_file2"  # Second reads

    readfiles(file1, file2)


def readfiles(file1, file2):
    blast = BLASTer()
    with open(file1, "r") as f1, open(file2,"r") as f2:
        nextisseq = False
        for _ in f1:
            line = f1.readline()
            if line[:3] == "@HWI":
                header = line
                nextisseq = True
            elif nextisseq:
                seq = line
                result = blast.blast(seq)
                blast.save(header, seq, result)
                nextisseq = False

            line = f2.readline()
            if line[:3] == "@HWI":
                header = line
                nextisseq = True
            elif nextisseq:
                seq = line
                result = blast.blast(seq)
                blast.save(header, seq, result)
                nextisseq = False

def insert():
    """"Insert to database?
    Run once per sequence? """
    pass


# main()


""" Useful:
https://biopython.readthedocs.io/en/latest/Tutorial/chapter_blast.html#parsing-blast-output
"""