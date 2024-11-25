from flask import Flask, request, render_template
import requests




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
    
    # if request.method == "POST" :
    #     search_text = request.form["izvelies_tekstu"]
    #     atbilde = request.get("https://api.chucknorris.io/jokes/search?query={search_text}")

    return render_template("teksta_izvele.html", joks = joks["value"], bilde = joks["icon_url"]  )
    




if __name__ == "__main__":
    app.run(port=5000)
