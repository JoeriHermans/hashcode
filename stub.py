import math
import numpy as np

filename="file"
commands=[]

var1,var2
objects=[]

class Dummy(object):

    def __init__(self, x):
        self.x=x
        self.y=5

    def __str__(self):
        return 'x: %d, y: %d' %(
        self.x, self.y
        )

    def method(self):
        global commands
        commands.append("x x x")
        commands=[]
        return 0


def main():
    f = open(filename+".in","rb")
    meta = f.readline().split()
    meta=map(int,meta)

    global var1, var2
    var1 = meta[0]
    var2 = meta[1]

    d=Dummy(3)
    d.method()
    print d

    global objects
    #parse

    write()

def write():
    output = open(filename+".out","w")
    output.write(str(len(commands))+"\n")
    for command in commands:
        output.write(command+"\n")

    output.close()
    print "done"
    exit()

if __name__ == '__main__':
    #global filename
    #filename=
    #filename=
    main()
