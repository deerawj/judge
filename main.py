from os.path import exists
from os import listdir
from subprocess import check_output
from sys import argv
from timeit import timeit

import subprocess

lang: dict = {
    'py'  : "python3 :",
    'py3' : "python3 :",
    'py2' :  "python2 :",
    'c'   : "gcc -o # : ; ./#",
    'cpp' : "g++ -o # : ; ./#",
    'rs'  : "rustc -o # : ; ./#",
    'go'  : "go run :",
    'java': "java :"
}

name: dict = {
    'py'  : "Python3",
    'py3' : "Python3",
    'py2' : "Python2",
    'c'   : "C",
    'cpp' : "C++",
    'rs'  : "Rust",
    'go'  : "Go",
    'java': "Java"
}

def run_run(c):
    return timeit(lambda:subprocess.run(c, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL),number=4)

def run_com(n, c):
    cm_tm = 0
    if len(c) == 2: #compilling
        cm_tm = timeit(lambda:subprocess.run(c.pop(0), shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL),number=1)
        c = c[0]

    o = subprocess.run(c, shell=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    print(n+(10-len(n))*" ","\t", o.stdout, end="\t")
    return run_run(c), cm_tm

def str_round(num,pos=0):
    if num:
        s = str(round(num,pos))
        return s+(pos+2-len(s))*"0"
    return num

cmds = []
for f in argv[1:]:
    for i in listdir(f):
        p = f"{f}/{i}"
        e = p[::-1].split(".",1)[0][::-1]
        x = f"{f}/exe_{e}"
        if e not in lang:
            continue

        c = lang[e].replace(':',p,1).replace('#',x)
        c = c.split(";")
        cmds.append([name[e],c])

for n,c in cmds:
    #o = check_output(c)
    #, stderr=subprocess.STDOUT)
    t = run_com(n, c)
    print(*[str_round(i,10) for i in t])