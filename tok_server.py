from flask import Flask, render_template
from opentok import OpenTok, Roles 
import time

API_KEY = 45961142
API_SECRET = "6e5a8ab70d86f22fec8d030342a193a8da05a1ad"
opentok = OpenTok(API_KEY, API_SECRET)
# create new session
session = opentok.create_session()

app=Flask(__name__)

@app.route("/")
def start():
    key = API_KEY
    session_id = session.session_id
    token = opentok.generate_token(session_id)
    token = session.generate_token(role=Roles.publisher)
    return render_template('index.html', api_key=key, session_id=session_id, token=token)

if __name__ == "__main__":
    app.debug = True
    app.run()
