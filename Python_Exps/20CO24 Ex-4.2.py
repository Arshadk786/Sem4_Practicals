'''
                        Experiment 4.2 : Implementing Exception Handling
                                                            Name:  Khan Arshad Abdulla
                                                            Roll No: 20CO24
                                                            2021-2022
                                                        
THEORY:
Python has many built-in exceptions that are raised when your program encounters an error (something in the program goes wrong).

When these exceptions occur, the Python interpreter stops the current process and passes it to the calling process until it is handled. If not handled, 
the program will crash.

In Python, exceptions can be handled using a try statement.
The critical operation which can raise an exception is placed inside the try clause. The code that handles the exceptions is written in the except clause.

If no exception occurs, the except block is skipped and normal flow continues(for last value). But if any exception occurs, it is caught by the except block (first and second values).
A try clause can have any number of except clauses to handle different exceptions, however, only one will be executed in case an exception occurs.

The try-expect statement

If the Python program contains suspicious code that may throw the exception, 
we must place that code in the try block. The try block must be followed with 
the except statement, which contains a block of code that will be executed if
there is some exception in the try block.

'''

def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f


#driver code
def main():
    while True:
        try:
            n=int(input('Enter the number: '))
            break
        except (NameError,ValueError):
            print('Please enter a valid integer number...')
        else:
            pass
        finally:
            pass
    print('Factorial of',n,'is',fact(n))

if __name__=='__main__':
    main()
    
'''
OUTPUT:
Enter the number: 5
Factorial of 5 is 120

Enter the number: rty
Please enter a valid integer number...

CONCLUSION:
        In this particular experiment we have successfully implemented Exception Handling.Exception needs to be handled properly, else the program will stop abruptly. We use try block for code that may throw exception, except keyword to catch that exception and finally to execute the important part of the code.
'''