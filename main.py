from flask import Flask, render_template, request, redirect
from so import get_jobs

app = Flask("Scrapper")

@app.route("/") # 'decorator' see under func.
def home() :
    return render_template("main.html")

@app.route("/report")
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        jobs = get_jobs(word)
        print(jobs)
    else :
        return redirect("/") # Go back home

    return render_template("report.html", searchingBy = word)

app.run(host = "0.0.0.0")