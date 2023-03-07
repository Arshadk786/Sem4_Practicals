'''
Experiment 601 : Python program to append data to existing file and then display the entire file.
           Name : Khan Arshad Abdulla
           RollNo : 20O24
           Academic Year : 2021-22

THEORY:

File Handling in Python:
Python too supports file handling and allows users to handle files i.e., to read and write files, along with many other file handling options, to operate on files. The concept of file handling has stretched over various other languages, but the implementation is either complicated or lengthy, but like other concepts of Python, this concept here is also easy and short. Python treats file differently as text or binary and this is important. Each line of code includes a sequence of characters and they form text file.

Working of open() function:
Before performing any operation on the file like read or write, first we have to open that file. For this, we should use Python’s inbuilt function open()
But at the time of opening, we have to specify the mode, which represents the purpose of the opening file.

f = open(filename, mode)

Where the following mode is supported:

r: open an existing file for a read operation.
w: open an existing file for a write operation. If the file already contains some data then it will be overridden.
a:  open an existing file for append operation. It won’t override existing data.
r+:  To read and write data into the file. The previous data in the file will not be deleted.
w+: To write and read data. It will override existing data.
a+: To append and read data from the file. It won’t override existing data.

Working of read() mode:
There is more than one way to read a file in Python. If you need to extract a string that contains all characters in the file then we can use file.read(). 

'''


def write(filename):
    with open(filename+".txt", "a+") as f:
        data = input("Enter Data : ")
        f.write(data)


def read(filename):
    with open(filename+".txt", "r") as f:
        print(f.read())


def main():
    filename = input("Enter Filename : ")
    while 1:
        print("\t\t\tMENU\t\t\t")
        print("1. Write\n2. Read\n3. Exit")
        ch = int(input("Enter Your Choice : "))
        if ch == 1:
            write(filename)
        elif ch == 2:
            read(filename)
        elif ch == 3:
            break
        else:
            print("Invalid Choice")


if __name__ == '__main__':
    main()

'''
OUTPUT:

Enter Filename : exp6
                        MENU
1. Write
2. Read
3. Exit
Enter Your Choice : 1       
Enter Data : I am Arshad And my Roll no is 20CO24.
                        MENU
1. Write
2. Read
3. Exit
Enter Your Choice : 2
I am Arshad And my Roll no is 20CO24.
                        MENU
1. Write
2. Read
3. Exit
Enter Your Choice : 3

CONCLUSION:
In this experiment we have successfully appended data into the file and display entire file using append(a) and read(r) mode.
'''
