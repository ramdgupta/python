# python great
Python project

    
# 
    - Python run any plateform without changing any behaviour in javascript behaviour change when run browser and node
    - def us as function declaration def chai(n) :
    - indentation is most important in python
    - __pychache__  hello_cpython-312.pyc

# Python inner working
    - first need install python interprater 
    - and then need to give our script(program) then interprater complete the program instruction
    - first work is need to convert Byte code
    - .pyc contain the byte code (this is not java byte code but simmilar to that)
    - When install python after byte code PYthon VM also created 
    - Compile to ByteCode (this is intermidatory step)
    - Bytecode is low level code and it's plateform independent
    - to run this we need python VM 
    - Byteocode run faster than your program
    - __pychache__ is compile bytecode also said frozen binaries
    - __pychache__ folder (__) it's internal use for pythan 
    - hello_chai.cpython-312.pyc in two thing is important Source change and version 
    - standard version of python is cpython 
    - 312 is the python 3.12 version this is usese python standard version cpyton and we have frozen    binary from there
    - .pyc only created in imported file not come at top level file means if you have single file 
    - .pyc  created when doing import and export  because of optmization of code
    
# PVM (Python Vertual Machine) 
    - For the resion of PVM we call Python interprated language code run line by line
    - PVM also caller run time Engine
    
# Byte code is Not Machine Code 
    - Machine code is direct instruction
    - Machine code prduce by Assembly Language which give instruction direct to Machine
    - It,s instruction for Python 
# Standard Python
    - Cpython, jythan, IronPyathon, Stackless, PyPy
    - Standard Python means Cpython

# Python  Shell
    - Indention required always 
    - shell can use to test code 
    - you can perform oneliner and multiner code 
    - you can import and use all method of that class
    - import os all method comes with this os.getcwd(); will give current working directory
    - loop if you want to print letter of a word
    - chai > c  h a i 
    - for c in "chai" : Enter for indent use tab and write print(c) 
    - if there is not indentation then it's give IndentationError
    - if we import a file in python in current directory  use there all method using file name.mehtod
    - but if you define new method then new method is not accessble due to byte code is not avilable for them 
    - if you run you get error AttributeError 
    - it's mean we need to relaod the file again so we need to import reload method
    - from importlib import reload
    - reload(hello_chai)
    - then think our newly created method come or not
    - yes they come
    - import os  os.getcwd()
    - import sys  sys.platform

# Mutable and Imutable 
    - Mutable : List, Set, Dictionary, Bytearray, Array
    - Immutable : Integers, Floating , Boolean, String, Tuples, Forzen set, Bytes
    - Everthing is object in Python
    - Immutable are created variable as reference 
    - Mainly it's happen in python
    - if we define a username = "Ram" and newUserName  =userName 
    - then you print username its' show Ram and newUserName also show Ram 
    - but if you again assign a new value to username="Ashu" and print then it's how Ashu 
    - newUserName show "Ram" because of newUserName getting value from reference not from variable 
    - means wehn assing new value "Ashu" to username then it's created a different reference and assign it's to user
    - while newUserName showing first reference this the immutability 
    - we are not changing value we are updating reference 
    - python have garbage colletion which remove the unusable referece 

# Python Comment
    - comment :# single line or ''' ''' multiline
# Python Data Type
    - Number: 1234, 3.1444, 3+4j, 0b111, Decimal(), Fraction()
    - String: 'spam' , "Bob's", b'a\x01c, u'sp\xc4m'
        - String can be written single and dboule quote and also special and unicharactor are also string
    - List: [1,2,3,['abc, 'two' 1.2, 1], 'new'], list(range(10)):method
        - Continues memory space avilable value on index
        - it's start from 0
        - in list can be nested with list in list and all other type data in python 
        - list have method
    - Tupel : (1, 'spam' 4, 'U'), tuple('spam'), namedtuple 
        - Tuple we use parenthesis seprate with comma 
    - Dictionary food= {'food': 'spam', 'taste':'yum'}, dict (hours=10)
        - Dictionary we use curly bases  it's have key and value
        - dict is use for defining dictinary
        - in dict value not start from 0 index
        - in dict always value have an key
        - dictionary keys enclose in '' or "" because they are string
        -  to access dictionary value need to do call key food["test"]

    - Set :set('abc'), {'a', 'b', 'c'}
        - Set always keep unique value 
        - Set don't show if there is duplicate value
        -
    - File : open('eggs.txt'), open(r'C:\jam.bin', 'wb')
    - Boolean : True , False
    - None : None
    - Functions, Modules, Classes 
    - Advance : Decorators, Generators, Iterators, MetaPrograming

# Internal working of python
    - if we make a variable score = 10
    - and a_score = score 
    - At reference 10 associated with two variable 
    - now you have assign a varialbe id =5 
    - Suppose id use is finish then you remove the id  
    - now reference 5 have no use 
    - python do not keep unused reference internly
    - Internaly python working in this case is differently
    - Because python compilar treat differently number and string
    - there is any method where reference counted
    - But you can't see if you want then you want manipulate so many thing
    - python use to garbase collection 
    - but it's not remove 5 immidiately
    - import sys and sys.getrefcount() it's give constant number output
    - this is method which tell you refrence count 
    - sys.getrefcount('ram') //4294967295
    - intenaly compliter loop run and give this number repeteadly
    - there is no way to reference count
    - you know the reference count exist but no way you proof with print
    - supoose i have a variable a =3
    - we know behind the seen 3 reference assign to a
    - Behind the seen variable don't have data type while memory value which is called reference have data type
    - now a ="chaiandcode"
    - now 3 reference remove now a have assign to a new reference "chaiandcode"
    - now there is 3 no use but python not collect this 3 in garbase collection imidiataly take some time to do that but you can do it forcefully
    - python think may be in case of number and string immidiatly call previous reference
    - a= 5 and b =2 now a = a+2 now a  have the value 7 
    - Now a have  new reference 7 , memory reference is 5 is free with variable now it's ready for garbase collection
    -in this case a = a+2 , first happen calculation  
    - myListone =[1,2,3] and myListTwo = myListone
    - now both are have same memory reference internly
    - myListOne == myListTwo : True :[1,2,3]
    -myListOne ="Chia"
    -myListOne == myListTwo : False
    - myListOne : Chai
    - myListTwo = [1,2,3]
    - again assign myListOne=[1,2,3]
    -myListOne == myListTwo : True
    - myListOne is myListTwo: False
    -myListOne[0]=33
    -myListOne : [33,2,3]
    -myListTwo :[1,2,3]
    - now see reference l1 = [1,2,3]
    - l2 = l1
    - l1==l2 : True
    -l1[0]=44
    -l1  : [44,2,3]
    -l2  : [44,2,3]
    -l1 is l2 : True
    -p1 = [1,2,3]
    -p2=p1
    -p2=[1,2,3]
    -p1[0]=55
    -p1:[55,2,3]
    -p2:[1,2,3]
    -These need to understand mutable and unmutable 
    -slicing List  h1 =[1,2,3] 
    -h2=h1[:] when you do slicing you have made a copy , copy , deepcopy
    -h1 : [1,2,3]
    -h2 :[1,2,3]
    -h1[0]=55
    -h1 : [55,2,3]
    -h2 :[1,2,3]
    - import copy h2 = copy.copy(h1)
    -h2 = copy.deepcopy(h1) [to copy nested lists]





    
# Revison
    - 12 + 12 o/p :24
    - 2.5 + 5 o/p: 12.5 - if a single value in decimal then result should be decimal
    - python support high value
    - 2 ** 2 o/p : power - ** use for calulate power
    -Suppose you calculate any digit power of hundred number then python shine because it's handle a big ammount of number like: 2** 14284
    - username ="chaiaurcode"
    - len(username) :11
    - username[0] : 'c' string also treat as list 
    - username[0] = 'A'
    - error: TypeError : 'str' object does not support item assignment 
    - string is immutable so we unable to replace value on prticular index
    - we can do these thing in List but not string
    - username[0] : c
    - username[-1]: 'e'
    - username[-2] : 'd'
    - username[1:3]: 'ha'
    - when we talk about imutable and mutable then you need to think object and memory so you need to know concept of behind the seen.
    - 
# Numbers in depth in python
    - Number is not single object it's a group of object
    - Number is strong game of Python
    - String also strong in python but no match of Number
    - for Number python have best library Numphy
    - what are the number and type of number
    - python carry decimle, complex , boolean , Set also treat as number in internaly
    - under the hood python compiler is writen in c++
    - First we talk about expression
    - +, -, /(give decimal resul),%,//(for int result),**(power)
    - use pranthesis for operation that good way of writing code
    - x + (y*z)
    - always keep in mind in operation keep all data type are same in inital 
    - don't use mismatch data type in project level it's create a big different and not the good way of writing
    code
    - operator overloading : "chai" + "code" o/p: chaicode
    -x = 1 x=2 x=3 print(x,y,z) : (1,2,3) when we print comma seprated variable means we get output in tuple
    - x+1, y*2 : (2,6)
    - to calculate power ** :2**2 : 4
    - result =1/3.2 output come 0.3125 then you need to decide to what decimal precision value you want to take
    - repr(s) will give a representation that includes quotes and escape sequences if present.
    - str(s) will give a clean representation without escape sequences.
    - print(s) will print the string as it is, without quotes or escape sequences.
        s = "Hello\nWorld!"
        print(repr(s))  # Output: 'Hello\nWorld!'
        print(str(s))   # Output: Hello
                #         World!
        print(s)        # Output: Hello
                #         World!
    - 










