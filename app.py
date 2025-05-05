from flask import Flask, render_template, request
from utils.logic import map_answers_to_tags, get_matching_quote

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    quote = None
    username = None
    if request.method == "POST":
        username = request.form.get("username")
        answers = [
            request.form.get("q1"),
            request.form.get("q2"),
            request.form.get("q3")
        ]
        tags = map_answers_to_tags(answers)
        quote = get_matching_quote(tags)
    return render_template("index.html", quote=quote, username=username)

if __name__ == "__main__":
    app.run(debug=True)
