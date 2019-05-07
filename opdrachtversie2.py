#Sanne Post
#BIN-1A
#afvink 3
import mysql.connector
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return ('<!DOCTYPE html>\n'
            '<html lang="en">\n'
            '<head>\n'
            '    <meta charset="UTF-8">\n'
            '    <title>Afvink2</title>\n'
            '</head>\n'
            '<body>\n'
            '<form method = "POST">Zoekwoord:\n'
            '    <input type="text" name = "zoekwoord">\n'
            '    <input type ="submit" value="Submit"></form>\n'
            '</body>\n'
            '</html>')


@app.route('/', methods=['POST'])
def zoeken():
    conn = mysql.connector.connect(host="ensembldb.ensembl.org", user="anonymous", db="homo_sapiens_core_95_38")
    cursor = conn.cursor()
    zoekwoord = request.form["zoekwoord"]
    cursor.execute("select description from gene where description like '%" + zoekwoord + "%'")
    records = cursor.fetchall()  # lijst met al de namen die het zoekwoord in de naam hebben
    cursor.close()
    conn.close()
    teruggeven = ""
    for row in records:
        teruggeven = teruggeven+(row[0])
        teruggeven = teruggeven + "<br>"

    return ('<!DOCTYPE html>\n'
            '<html lang="en">\n'
            '<head>\n'
            '    <meta charset="UTF-8">\n'
            '    <title>Afvink2</title>\n'
            '</head>\n'
            '<body>\n'
            '<form method = "POST">Zoekwoord:\n'
            '    <input type="text" name = "zoekwoord">\n'
            '    <input type ="submit" value="Submit"></form>\n'
            + "<br>" + 'Het volgende is gevonden met je gegeven zoekwoord '
            + zoekwoord + " : <br>" + "<br>" + teruggeven +
            '</body>\n'
            '</html>')


if __name__ == '__main__':
    app.run(debug=True)


