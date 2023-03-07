'''
Experiment 10 : Programs on Threading using python.
                 Name : Khan Arshad Abdulla
                 Roll No : 20CO24
                 Academic Year : 2021-22
 
THEORY:

Thread:
In computing, a process is an instance of a computer program that is being executed. Any process 
has 3 basic components.

Multithreading:
Multiple threads can exist within one process where:
Each thread contains its own register set and local variables (stored in stack).

All thread of a process share global variables (stored in heap) and the program code.

Multithreading is defined as the ability of a processor to execute multiple threads concurrently.

In Python, the threading module provides a very simple and intuitive API for spawning multiple 
threads in a program.
'''
from threading import *


class A(Thread):
    def run(self):
    for i in range(50):
    print('A')


class B(Thread):
    def run(self):
    for i in range(50):
    print('B')


def main():
    a = A()
    b = B()
    #b = Thread(target=B.run, args=(B(),))
    a.start()
    b.start()
    a.join()
    b.join()
    print('Done')


if __name__ == '__main__':
    main()

'''
OUTPUT:
A
AB
B
B
B
B
AB
B
A
A
A
A
A
A
A
A
B
AB
A
A
A
A
B
B
A
A
B
A
A
A
A
A
A
B
B
B
B
B
B
B
B
B
B
B
B
B
A
B
A
A
B
B
B
B
A
A
A
A
B
B
B
A
A
A
A
B
B
A
B
A
A
A
A
A
A
A
A
A
AB
B
A
A
A
B
B
B
B
B
B
B
B
B
B
B
B
Done

CONCLUSION: In this experiment we have successfully implemented Multithreading with Python.
'''
