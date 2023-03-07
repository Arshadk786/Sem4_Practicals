'''
			        Experiment 2.2 : Implementing Functions in Python.
                                                            Name: Khan Arshad Abdulla
                                                            Roll No: 20CO24
                                                            2021-2022

THEORY: 
	Functions are the most important aspect of an application. A function can be defined as the organized block of reusable code, which can be called whenever required. Python allows us to divide a large program into the basic building blocks known as a function. The function contains the set of programming statements enclosed by {}. A function can be called multiple times to provide reusability and modularity to the Python program. Python provide us various inbuilt functions like range() or print(). Although, the user can create its functions, which can be called user-defined functions.
There are mainly two types of functions.
	1)User-define functions - The user-defined functions are those define by the user to perform the specific task.
	2)Built-in functions - The built-in functions are those functions that are pre-defined in Python.
Python provides the def keyword to define the function. The syntax of the define function is 
	def my_function(parameters):  
    	    function_block  
	return expression 
In this programwe have used 3 diffrent functions fact(factorial), Palin(Palindrome) and fibo(fibonacci)

Factorial:
	Factorial is a non-negative integer. It is the product of all positive integers less than or equal to that number you ask for factorial. It is denoted by an exclamation sign (!).
Example:
    n! = n* (n-1) * (n-2) *........1  
    4! = 4x3x2x1 = 24  
    
Palindrome:
	A palindrome is a number or letter that remains the same even if the number and letters are inverted.
For example:
121, 11, 414, 1221, 74747 are the palindrome numbers.
12, 41, 12332, are not the palindrome numbers.
MOM, DAD, MADAM, REFER are the palindrome letters.
THE, PROGRAM, are not the palindrome letters.

Fibonacci:
	Fibonacci sequence specifies a series of numbers where the next number is found by adding up the two numbers just before it. 
0 and 1 are default numbers.
'''
def fact(num):
   f=1
   for i in range(1,num+1):
       f=f*i
   return f
def fibo(num):
    a=0
    b=1
    if num==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,num):
            c=a+b
            a=b
            b=c
            print(c)
def palin(num):
    rev=0
    q=num
    while q>0:
        
        rev=rev*10+q%10
        q=q//10
        
    if num==rev:
        print(f"{n} is a Palindrome number")
    else:
        print(f"{n} is not a palindrome number")
        

if __name__=='__main__':
     while True:
        print("Menu:\n\t1.Factorial\n\t2.Fibonacci\n\t3.Palindrome\n\t4.Exit")
        ch=int(input("Please Enter Your Choice ::"))
        if ch==1:
            n=int(input("Enter a number::"))
            print(f"The factorial of {n} is {fact(n)}")
        elif ch==2:
            f=int(input("Enter a number::"))
            print(f"The fibonacci series of {f} is ")
            fibo(f)
        elif ch==3:
            n=int(input("Enter a number::"))
            palin(n)
        elif ch==4:
         	print("Thank you!")
         	exit()
        else:
         	print("Please enter a correct number")
'''
OUTPUT:
Menu:
        1.Factorial
        2.Fibonacci
        3.Palindrome
        4.Exit
Please Enter Your Choice ::1
Enter a number::5
The factorial of 5 is 120
Menu:
        1.Factorial
        2.Fibonacci
        3.Palindrome
        4.Exit
Please Enter Your Choice ::2
Enter a number::6
The fibonacci series of 6 is 
0
1
1
2
3
5
Menu:
        1.Factorial
        2.Fibonacci
        3.Palindrome
        4.Exit
Please Enter Your Choice ::3
Enter a number::25
25 is not a palindrome number
Menu:
        1.Factorial
        2.Fibonacci
        3.Palindrome
        4.Exit
Please Enter Your Choice ::3
Enter a number::121
121 is a Palindrome number
Menu:
        1.Factorial
        2.Fibonacci
        3.Palindrome
        4.Exit
Please Enter Your Choice ::4
Thank you!

CONCLUSION:
	In this perticular experiment we have sucessfully implemented functions in python.The Function helps to programmer to break the program into the smaller part. It organizes the code very effectively and avoids the repetition of the code. As the program grows, function makes the program more organized.

'''