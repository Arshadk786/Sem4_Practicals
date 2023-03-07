'''
                    Experiment 2.1 : Implementing for loop in python
                                                            Name:  Khan Arshad Abdulla
                                                            Roll No: 20CO24
                                                            2021-2022
THEORY:
        The flow of the programs written in any programming language is sequential by default. 
Sometimes we may need to alter the flow of the program.
The execution of a specific code may need to be repeated several numbers of times.
For this purpose, The programming languages provide various types of loops which are capable of
repeating some specific code several numbers of times.
The for loop in Python is used to iterate the statements or a part of the program several times.
It is frequently used to traverse the data structures like list, tuple, or dictionary.
The syntax of for loop in python is:
    for iterating_var in sequence:    
        statement(s)    
        
The range() function:
The range() function is used to generate the sequence of the numbers. If we pass the range(10),
it will generate the numbers from 0 to 9. The syntax of the range() function is given below.
Syntax:
    range(start,stop,step size)  
    
Nested for loop:
Python allows us to nest any number of for loops inside a for loop.
The inner loop is executed n number of times for every iteration of the outer loop.
Syntax:
    for iterating_var1 in sequence:  #outer loop  
        for iterating_var2 in sequence:  #inner loop  
            #block of statements     
    #Other statements    
'''

num=int(input("Enter a number: "))
fact=1
for i in range(1,num+1):
    fact=fact*i
print("Factorial of",num,"is",fact)

for row in range(1,6):
    for col in range(1,6):
        if col<=row:
           print(6-col,end='')
        else:
            print(end='')
    print()

s='*'*3+'\n'+'*'*2+'\n'+'*'
print(s)

'''
OUTPUT:
Enter a number: 5
Factorial of 5 is 120
5
54
543
5432
54321
***
**
*

CONCLUSION:
            In this perticular experiment we have sucessfully implemented for loop. for loop
provides code re-usability. Using loops, we do not need to write the same code again and again.
Using loops, we can traverse over the elements of data structures (array or linked lists).
'''