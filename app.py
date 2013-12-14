# -*- coding: utf-8 -*-
from flask import Flask,redirect,url_for,session,request,g,render_template

from model import OneIssue

app = Flask(__name__)





@app.route("/")
@app.route("/issue/<int:issuenumber>")
def show_issue(issuenumber=1):
    # get issue
    return render_template("issue.html", 
                            issue=OneIssue.get_issue_by_issue_number(issuenumber))

if(__name__ == "__main__"):
    app.debug = True
    app.run(host= '0.0.0.0')
