from gemini_service import analyze_career
from flask import Flask, render_template, request
from flask import flash, redirect, url_for
app = Flask(__name__)
app.secret_key = "careercompassai"
analysis_data = {}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/routes")
def routes():
    return render_template("routes.html")

@app.route("/guidance")
def guidance():

    return render_template(
        "guidance.html",
        data=analysis_data
    )

@app.route("/analyze", methods=["POST"])
def analyze():

    try:

        user_input = request.form["user_input"]

        analysis_data["user_input"] = user_input

        analysis_result = analyze_career(user_input)

        analysis_data.update(analysis_result)

        return render_template(
            "routes.html",
            data=analysis_data
        )

    except Exception as e:

        print("ERROR:", e)

        flash(
            "Career Compass AI is currently Busy in recalculating routes. Please try again in a few minutes."
        )

        return redirect(url_for("home"))


@app.route("/how-it-works")
def how_it_works():
    return render_template("how_it_works.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/resources")
def resources():
    return render_template("resources.html")


if __name__ == "__main__":
    app.run(debug=True)