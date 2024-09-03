from flask import Flask, request, jsonify, render_template, redirect, url_for
import sqlite3
from newHashs import gerarHash

connection = sqlite3.connect("data.db", check_same_thread=False)
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Links (
    link TEXT,
    linkId, TEXT
)
""")


app = Flask(__name__)


@app.route("/")
def home():
    linkTxt = request.args.get('linkTxt')
    linkId = request.args.get('linkId')
    if linkTxt:
        linkAcesso = f'http:{request.host}/link/?LinkId={linkId}'
        return render_template("home.html", linkTxt = linkTxt, linkId = linkId, linkAcesso = linkAcesso)
    return render_template("home.html")

@app.route("/gerar-link", methods=["POST"]) 
def gerar_link():
    linkUrl = request.form["linkUrl"]
    linkId = gerarHash(10)
    cursor.execute(f"""
               INSERT INTO Links (link, linkId) VALUES ('{linkUrl}', '{linkId}')
    """)
    connection.commit()

    cursor.execute(f"SELECT * FROM Links WHERE linkId = '{linkId}'")
    linkTuple = cursor.fetchone()
    linkTxt = linkTuple[0]
    linkId = linkTuple[1]
    
    return redirect(url_for("home", linkTxt = linkTxt, linkId = linkId))

@app.route("/link/")
def link():
    linkId = request.args.get('LinkId')
    if link != None:
        cursor.execute("SELECT link FROM Links WHERE LinkId = ?", (linkId,))
        linkUrl = cursor.fetchone()[0]
        return redirect(linkUrl)
    return redirect(url_for('home'))
    

connection.commit()
if __name__ == "__main__":
    app.run(debug=True)