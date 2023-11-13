import mysql.connector
from flask import Flask

def haelentoasema(icao):
    sql = "select name, municipality from airport"
    sql += " where ident='" + icao + "'"

    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    if kursori.rowcount > 0:
        for rivi in tulos:
            return {
                "Icao": icao,
                "Name": rivi[0],
                "Municipality": rivi[1]
            }

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='Kurolaattori',
    autocommit=True
)

app = Flask(__name__)
@app.route('/kenttä/<icao>')
def lentoasema(icao):
    return haelentoasema(icao)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)