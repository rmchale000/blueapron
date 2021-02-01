import datetime
from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def hello():
    userAgent = request.headers.get('User-Agent')
    if userAgent=="h4ck3r":
        return "HTTP 403 Forbidden", 403
    respstr = "Hello World\nCurrent date and time is "
    respstr += datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return respstr

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
