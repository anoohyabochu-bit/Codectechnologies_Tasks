from flask import Flask, render_template, request
from database import create_database, get_metrics
from monitor import monitor_api

app = Flask(__name__)

# Create database when application starts
create_database()


@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        api_url = request.form.get("api_url")

        if api_url:
            result = monitor_api(api_url)

    metrics = get_metrics()

    return render_template(
        "index.html",
        result=result,
        metrics=metrics
    )


if __name__ == "__main__":
    app.run(debug=True)