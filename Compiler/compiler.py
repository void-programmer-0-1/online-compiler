from flask import Blueprint,render_template,request
import subprocess
from typing import List

compiler: Blueprint = Blueprint("compiler",__name__)

@compiler.get("/")
def ide() -> str:
    return render_template("ide.html")

@compiler.post("/compile")
def compile() -> None:
    language: str = request.form.get("language")
    code: str = request.form.get("code")
    extension: str = find_extension(language.lower())
    filename: str = f"main{extension}"
    path: str = f"Code/{filename}"
    with open(path,"w+") as file:
        file.write(code)
    cmd: List[str] = get_compiler_cmd(language,path)
    output: str = subprocess.run(cmd, stdout=subprocess.PIPE, text=True).stdout
    if extension == ".cpp" or extension == ".c":
        run: str = subprocess.run(f"./{cmd[3]}",stdout=subprocess.PIPE,text=True).stdout
        return run
    return output

def find_extension(language: str) -> str:
    if language == "python":
        return ".py"
    elif language == "c":
        return ".c"
    elif language == "cpp":
        return ".cpp"
    elif language == "php":
        return ".php"
    elif language == "node":
        return ".js"
    else:
        return ".txt"


def get_compiler_cmd(language: str,path: str) -> List[str]:
    if language == "python":
        return ["python", f"{path}"]
    elif language == "c":
        o_filename: str = f"{path[0:-2]}.o"
        return ["gcc", f"{path}", "-o", f"{o_filename}"]
    elif language == "cpp":
        o_filename: str = f"{path[0:-4]}.o"
        return ["g++", f"{path}", "-o", f"{o_filename}"]
    elif language == "php":
        return ["php", f"{path}"]
    elif language == "node":
        return ["node", f"{path}"]
    else:
        return "none"


'''
#include <stdio.h>

int main(){
    int a = 10;
    int *b = &a;
    printf("*b = %d",*b);
    return 0;
}
'''