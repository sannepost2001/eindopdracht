import mysql.connector
from flask import Flask, request

app = Flask(__name__)

@app.route('/')


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


if __name__ == '__main__':
    app.run()

