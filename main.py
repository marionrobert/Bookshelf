from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    return render_template("index.html", books=all_books, nb_books=len(all_books))


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = {
            "title": request.form["title"],
            "author": request.form["author"],
            "rating": int(request.form["rating"])
        }
        all_books.append(new_book)
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

