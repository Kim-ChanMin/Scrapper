from flask import Flask, render_template, request, redirect, send_file
from so import get_jobs
from save import save_to_file

app = Flask("Scrapper")

# make database outside from decorator.
db = {}

@app.route("/") # 'decorator' see under func.
def home() :
    return render_template("main.html")

@app.route("/report")
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        existingJobs = db.get(word)
        # if searched before, show immediately.
        if existingJobs :
            jobs = existingJobs
        else :
            jobs = get_jobs(word)
            db[word] = jobs
    else :
        return redirect("/") # Go back home

    return render_template("report.html", resultsNumber = len(jobs), searchingBy = word, jobs = jobs)

@app.route("/export")
def export() :
    try :
        word = request.args.get('word')
        if not word :
            raise Exception()
        word = word.lower()
        jobs = db.get(word)
        if not jobs :
            raise Exception()
        save_to_file(jobs)
        return send_file("jobs.csv")
    except :
        return redirect("/")

app.run(host = "0.0.0.0")