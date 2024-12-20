from flask import Flask, request, render_template, jsonify
import requests, random




app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def index():
    atbilde = requests.get("https://api.chucknorris.io/jokes/random")
    joks = atbilde.json()
    atbilde = requests.get("https://api.chucknorris.io/jokes/categories")
    kategorijas = atbilde.json()
    if request.method == "POST" :
        kategorija = request.form["kategorijas"]
        atbilde = requests.get(f"https://api.chucknorris.io/jokes/random?category={kategorija}")
        joks = atbilde.json()

    return render_template("index.html", joks = joks["value"], bilde = joks["icon_url"], kategorijas = kategorijas)

@app.route("/teksta_izvele", methods=["POST","GET"])
def teksta_izvele():
    atbilde = requests.get("https://api.chucknorris.io/jokes/random")
    joks = atbilde.json()
    
    if request.method == "POST" :
        search_text = request.form["izvelies_tekstu"]
        atbilde = requests.get(f"https://api.chucknorris.io/jokes/search?query={search_text}")
        joks = atbilde.json()
        print(joks)

        return render_template("teksta_izvele.html", joks = joks["result"][random.randint(0, joks["total"])]["value"] )
    return render_template("teksta_izvele.html", joks = joks["value"], bilde = joks["icon_url"])


@app.route("/jschats")
def chats():
    return render_template("chats.html")

@app.route("/jschats/suutiit", methods = ["POST"])
def suutiit():
    if sanemtais["saturs"] == "\clear":
        with open("chataZinas.txt", "w") as f:
            f.write("")
        return
    sanemtais = request.json
    with open("chataZinas.txt", "a") as f:
        f.write(sanemtais["vards"])
        f.write("----")
        f.write(sanemtais["saturs"])
        f.write('\n')
    return jsonify("OK")


@app.route("/jschats/lasiit")
def lasit():
    saturs = []
    with open("chataZinas.txt", "r") as f:
        saturs = f.readlines()
    return jsonify(saturs)

if __name__ == "__main__":
    app.run(port=5000)
