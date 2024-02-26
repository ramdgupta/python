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

# Python Data Type 
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
    - Dictionary : {'food': 'spam', 'taste':'yum'}, dict (hours=10)
        - Dictionary we use curly bases  it's have key and value
        - dict is use for defining dictinary
    - Set :set('abc'), {'a', 'b', 'c'}
        - Set always keep unique value 
        - Set don't show if there is duplicate value
    - File : open('eggs.txt'), open(r'C:\jam.bin', 'wb')
    - Boolean : True , False
    - None : None
    - Functions, Modules, Classes 
    - Advance : Decorators, Generators, Iterators, MetaPrograming
# 






