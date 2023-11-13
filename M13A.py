from flask import Flask, request

app = Flask(__name__)
@app.route('/alkuluku/<luku>')
def tulos(luku):
    for luvut in range(2, int(luku)):
        if int(luku) % luvut == 0:
            return {
                "Number": luku,
                "Is prime": False,
            }
        return {
            "Number": luku,
            "IsPrime": True,
        }

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)