from flask import render_template, request
from app import app
from files import FilesManager
import os

file = FilesManager()

@app.route("/viewer")
def viewer():
    target = request.args.get("path")
    if (target is not None):
        try:
            os.chdir(target)
            file.set_path()
            file.set_split_path()
        except:
            print("Bad path")
    file.set_dirs()
    file.set_files()
    return render_template("viewer.html", path=file.get_split_path(),
                                        dirs=file.get_dirs(),
                                        files=file.get_files())

@app.route("/file")
def fileviewer():
    file = request.args.get("file")
    content = None
    try:
        with open(file, "r") as fd:
            content = fd.read()
    except IOError:
        pass
    return render_template("file.html", content=content, title=file)

@app.route("/")
def index():
    """ Index route / """
    return render_template("index.html")
