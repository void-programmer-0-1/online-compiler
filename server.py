from flask import Flask,render_template
from Compiler.compiler import compiler

server: Flask = Flask(__name__)
server.register_blueprint(compiler,url_prefix="/compiler")

@server.get("/")
def homepage():
    return render_template("homepage.html")


