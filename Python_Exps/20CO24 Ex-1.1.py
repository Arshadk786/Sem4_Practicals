'''
            Experiment 1.1 : Implementing the conditional statments like if,elif and else.
                                                            
                                                            Name:  Khan Arshad Abdulla
                                                            Roll No: 20CO24
                                                            2021-2022
THEORY:
        Decision making is the most important aspect of almost all the programming languages.
decision making allows us to run a particular block of code for a particular decision.
Here, the decisions are made on the validity of the particular conditions.

If Statement:-The if statement is used to test a specific condition. If the condition is true,
            a block of code (if-block) will be executed.
The syntax of the if-statement is
if expression:  
    statement  
    
If - else Statement:-The if-else statement is similar to if statement except the fact that,
                it also provides the block of the code for the false case of the condition 
                to be checked. If the condition provided in the if statement is false,
                then the else statement will be executed.
The syntax of the if-else statement is
if condition:  
    block of statements   
else:   
    another block of statements (else-block)   

Elif Statement:-The elif statement enables us to check multiple conditions and 
            execute the specific block of statements depending upon the true condition 
            among them. We can have any number of elif statements in our program
            depending upon our need. However, using elif is optional. 
            The elif statement works like an if-else-if ladder statement in C.
            It must be succeeded by an if statement.
The syntax of the elif statement is
f expression 1:   
     block of statements   
elif expression 2:   
     block of statements   
elif expression 3:   
     block of statements   
else:   
     block of statements  
'''

i=10
print(f"Data is {i} and its address is{id(i)} and its type is {type(i)}")
f=20.5
print(f"Data is {f} its address is {id(f)} and its type is {type(f)}")
s="AIKTC"
print(f"Data is {s} its address is {id(s)} and its type is{type(s)}")
var1=int(input("Enter the data:"))
print(f"Scanned data is {var1} and its type is {type(var1)}")
var2=int(input("Enter the data:"))
print(f"Scanned data is {var2} and its type is {type(var2)}")
var3=int(input("Enter the data:"))
print(f"Scanned data is {var3} and its type is {type(var3)}")
if var1>var2 and var1>var3:
    print("1st number is greatest")
elif var2>var3:
    print("2nd number is greatest")
elif var1==var2==var3:
    print("All numbers are equal")
else:
    print("3rd num is greater")
'''
OUTPUT:

Data is 10 and its address is2866203224656 and its type is <class 'int'>
Data is 20.5 its address is 2866209196976 and its type is <class 'float'>
Data is AIKTC its address is 2866209071344 and its type is<class 'str'>  
Enter the data:10
Scanned data is 10 and its type is <class 'int'>
Enter the data:30
Scanned data is 30 and its type is <class 'int'>
Enter the data:0
Scanned data is 0 and its type is <class 'int'>
2nd number is greatest

CONCLUSION: 
            In this perticular experiment we have sucessfully implemented the if,elif and
else conditional statements. Conditional statement is quite useful when it comes to
decision-making in programs to run a certain piece of code based on the values of the
conditionals.
'''