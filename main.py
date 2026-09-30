#Operators in Python
def operators():
    while True:

        print()
        print("=" * 55)
        print("                 OPERATORS IN PYTHON")
        print("=" * 55)
        print(""" 
        Operators are symbols used to perform operations on values and variables.
 
        Python has several types of operators:
 
        1. Arithmetic Operators
        2. Assignment Operators
        3. Comparison Operators
        4. Logical Operators
        5. Bitwise Operators
        6. Identity Operators
        7. Membership Operators
        8. Go to Previous 
        9. Go to Next 
        10. Go to Main menu 
        """)
        choice = input("Enter your choice: ")

        if choice == "1":
            arithmetic()

        elif choice == "2":
            assignment()

        elif choice == "3":
            comparison()

        elif choice == "4":
            logical()

        elif choice == "5":
            bitwise()

        elif choice == "6":
            identity()

        elif choice == "7":
            membership()
        elif choice == "8":
            print("No previous topic found")
        elif choice == "9":
            variables()
            return
        elif choice == "10":
            return
        else:
            print("Invalid choice! Please try again.")

def arithmetic():
    print("""ARITHMETIC OPERATORS:
    •Definition: Used to perform mathematical calculations.
    •Operators: +, -, *, /, //, %, **
    •Syntax: a + b
    •Example: 10 + 5 = 15""")
    input("\nPress Enter to go back")

def assignment():
    print("""ASSIGNMENT OPERATORS:
    •Definition: Used to assign or update values in variables.
    •Operators: =, +=, -=, *=, /=, //=, %=, **=
    •Syntax: variable operator value
    •Example: x += 5""")
    input("\nPress Enter to go back")

def comparison():
    print("""COMPARISON OPERATORS:
    •Definition: Used to compare two values and return True or False.
    •Operators: ==, !=, >, <, >=, <=
    •Syntax: a > b
    •Example: 10 > 5 → True""")
    input("\nPress Enter to go back")

def logical():
    print("""LOGICAL OPERATOR:
    •Definition: Used to combine or reverse conditional expressions.
    •Operators: and, or, not
    •Syntax: condition1 and condition2
    •Example: 10 > 5 and 5 > 2 → True""")
    input("\nPress Enter to go back")

def bitwise():
    print("""BITWISE OPERATORS:
    •Definition: Used to perform operations on the binary representation of integers.
    •Operators: &, |, ^, ~, <<, >>
    •Syntax: a & b
    •Example: 5 & 3 → 1""")
    input("\nPress Enter to go back")

def identity():
    print("""IDENTITY OPERATORS:
    •Definition: Used to check whether two variables refer to the same object.
    •Operators: is, is not
    •Syntax: a is b
    •Example: a is b → True or False""")
    input("\nPress Enter to go back")

def membership():
    print("""MEMBERSHIP OPERATORS:
    •Definition: Used to check whether a value exists in a sequence.
    •Operators: in, not in
    •Syntax: value in sequence
    •Example: "a" in "apple" → True""")
    input("\nPress Enter to go back")



#Variables in Python 
def variables():
    print()
    print("=" * 55)
    print("                 VARIABLES IN PYTHON")
    print("=" * 55)
    print("Definition: A variable is a name used to store a value.")
    print("Example:")
    print('''
    age = 18"
    name = Abhay''')

    print('''
        1. Go to Previous
        2. Go to Next
        3. Go to Main Menu''')

    choice = input("Enter your choice: ").lower()

    if choice == "1":
        operators()
        return
    elif choice == "2":
        datatypes()
        return
    elif choice == "3":
        return()
    else:
        print("Invalid choice! Please try again.")



#Datatypes in Python 
def datatypes():
    print()
    print("=" * 55)
    print("                 DATATYPES IN PYTHON")
    print("=" * 55)
    print('''
    A data type tells Python what kind of value a variable is storing

    Python has several types of data types:
     
        1. Integer Data Type
        2. Float Data Type
        3. Complex Data Type
        4. Boolean Data Type
        5. String Data Type
        6. Go to Previous
        7. Go to Next
        8. Go to Main Menu 
        ''')
    choice = input("Enter your choice: ")

    if choice == "1":
        integer()
    elif choice == "2":
        float()
    elif choice == "3":
        complex()
    elif choice == "4":
        boolean()
    elif choice == "5":
        string()
    elif choice == "6":
        variables()
        return
    elif choice == "7":
        typeconversion()
        return
    elif choice == "8":
        return
    else:
        print("Invalid choice! Please try again.")
        
def integer():
    print('''INTEGER DATA TYPE:
    •Definition: The integer data type is used to store whole numbers
    •Syntax: variable = integer_value
    •Example: marks = 95
    •Checking the type: print(type(marks))
    •Output: <class 'int'>''')
    input("\nPress Enter to go back")

def float():
    print('''FLOAT DATA TYPE:
    •Definition: The float data type is used to store decimal numbers
    •Syntax: variable = decimal_value
    •Example: temperature = 36.5
    •Checking the type: print(type(temperature))
    •Output: <class 'float'>''')
    input("\nPress Enter to go back")

def complex():
    print('''COMPLEX DATA TYPE:
    •Definition: The complex data type is used to store numbers having a real part and an imaginary part
    •Syntax: variable = real + j(imaginary)
    •Example: number = 3 + 4j
    •Checking the type: print(type(number))
    •Output: <class 'complex'>''')
    input("\nPress Enter to go back")

def boolean():
    print('''BOOLEAN DATA TYPE:
    •Definition: The boolean data type stores either True or False
    •Syntax: variable = True or False
    •Example: question = True
    •Checking the type: print(type(question))
    •Output: <class 'bool'>''')
    input("\nPress Enter to go back")

def string():
    print('''STRING DATA TYPE:
    •Definition: The string data type is used to store text
    •Syntax: variable = 'text'
    •Example: state = 'Haryana'
    •Checking the type: print(type(state))
    •Output: <class 'str'>''')
    input("\nPress Enter to go back")



#Type Conversion in Python
def typeconversion():
    print()
    print("=" * 55)
    print("                 TYPE CONVERSION IN PYTHON")
    print("=" * 55)
    print('''Type conversion means changing a value from one data type into another data type
    
    Python has several types of type conversions:

    1. int()
    2. float()
    3. str()
    4. bool()
    5. list()
    6. tuple()
    7. Go to Previous
    8. Go to Next
    9. Go to Main Menu
    ''')
    choice = input("Enter your choice: ")
    
    if choice == "1":
        intconversion()
    elif choice == "2":
        floatconversion()
    elif choice == "3":
        stringconversion()
    elif choice == "4":
        booleanconversion()
    elif choice == "5":
        listconversion()
    elif choice == "6":
        tupleconversion()
    elif choice == "7":
        datatypes()
        return
    elif choice == "8":
        strings()
        return
    elif choice == "9":
        return
    else:
        print("Invalid choice! Please try again.")

def intconversion():
    print('''INT CONVERSION:
    •Definition: The int() function converts a value into an integer.
    •Syntax: int(value)
    •Example: age = int("18")
    •Checking the type: print(type(age))
    •Output: <class 'int'>''')
    input("\nPress Enter to go back")

def floatconversion():
    print('''FLOAT CONVERSION:
    •Definition: The float() function converts a value into a decimal number.
    •Syntax: float(value)
    •Example: number = float("10.5")
    •Checking the type: print(type(number))
    •Output: <class 'float'>''')
    input("\nPress Enter to go back")

def stringconversion():
    print('''STRING CONVERSION:
    •Definition: The str() function converts a value into a string.
    •Syntax: str(value)
    •Example: age = str(18)
    •Checking the type: print(type(age))
    •Output: <class 'str'>''')
    input("\nPress Enter to go back")

def booleanconversion():
    print('''BOOLEAN CONVERSION:
    •Definition: The bool() function converts a value into True or False.
    •Syntax: bool(value)
    •Example: result = bool(1)
    •Checking the type: print(type(result))
    •Output: <class 'bool'>''')
    input("\nPress Enter to go back")

def listconversion():
    print('''LIST CONVERSION:
    •Definition: The list() function converts an iterable value into a list.
    •Syntax: list(value)
    •Example: numbers = list((1, 2, 3))
    •Checking the type: print(type(numbers))
    •Output: <class 'list'>''')
    input("\nPress Enter to go back")

def tupleconversion():
    print('''TUPLE CONVERSION:
    •Definition: The tuple() function converts an iterable value into a tuple.
    •Syntax: tuple(value)
    •Example: numbers = tuple([1, 2, 3])
    •Checking the type: print(type(numbers))
    •Output: <class 'tuple'>''')
    input("\nPress Enter to go back")



#String In Python 
def strings():
    print()
    print("=" * 55)
    print("                 STRINGS IN PYTHON")
    print("=" * 55)
    print('''A string is a sequence of characters used to store text

    Python has different types of operations on strings:
    
    1. String definition & creation
    2. String indexing
    3. String slicing
    4. String concatenation
    5. String repetition
    6. Escape sequences
    7. len() function
    8. Go to Previous 
    9. Go to Next 
    10. Go to Main Menu
    ''')
    choice = input("Enter your choice: ")
    
    if choice == "1":
        stringdefinition()
    elif choice == "2":
        stringindexing()
    elif choice == "3":
        stringslicing()
    elif choice == "4":
        stringconcatenation()
    elif choice == "5":
        stringrepetition()
    elif choice == "6":
        escapesequences()
    elif choice == "7":
        stringlength()
    elif choice == "8":
        typeconversion()
        return
    elif choice == "9":
        lists()
        return
    elif choice == "10":
        return
    else:
        print("Invalid choice! Please try again.")  

def stringdefinition():
    print('''STRING DEFINITION AND CREATION:
    •Definition: A string is a sequence of characters used to store text
    •Syntax: variable = "text"
    •Example: name = "Abhay"
    •String can be written using:
      Single quotes (' ')
      Double quotes (" ")
      Triple quotes
    •Example: city = 'Dehradun'
    •Checking the type: print(type(city))
    •Output: <class 'str'>''')
    input("\nPress Enter to go back")

def stringindexing():
    print('''STRING INDEXING:
    •Definition: String indexing is used to access individual characters of a string.
    •Syntax: string[index]
    •Example: name = "Python"
              print(name[0], name[3])
    •Output: (P,h)
    •Important: String indexing starts from index 0.
    •Negative Indexing: Negative indexes access characters from the end.
    •Example: print(name[-1])
    •Output: n''')
    input("\nPress Enter to go back")

def stringslicing():
    print('''STRING SLICING:
    •Definition: String slicing is used to access a part of a string.
    •Syntax: string[start:stop]

    •Example: name = "Python"
              print(name[0:3])
    •Output: Pyt

    •Example: print(name[2:6])
    •Output: thon

    •Important: The stop index is not included.


    •Example: print(name[:3])
    •Output: Pyt''')
    input("\nPress Enter to go back")

def stringconcatenation():
    print('''STRING CONCATENATION:
    •Definition: String concatenation means joining two or more strings together.
    •Syntax: string1 + string2

    •Example: first = "Hello"
              second = "World"
              print(first + second)
    •Output: HelloWorld

    •Operator Used: +
    •Important: Strings can be joined using the + operator''')
    input("\nPress Enter to go back")

def stringrepetition():
    print('''STRING REPETITION:
    •Definition: String repetition means repeating a string multiple times.
    •Syntax: string * number

    •Example: word = "Ho"
              print(word * 3)
    •Output: HoHoHo

    •Operator Used: *
    •Important: The * operator repeats the string according to the given number.''')
    input("\nPress Enter to go back")

def escapesequences():
    print('''ESCAPE SEQUENCES:
    •Definition: Escape sequences are special characters used inside strings.
    •Syntax: \\escape_character

    •Common Escape Sequences:
      \\n = New line
      \\t = Tab
      \\\\ = Backslash
      \\' = Single quote
      \\" = Double quote

    •Example: print("Hello\\nWorld")
    •Output:
      Hello
      World

    •Example: print("Hello\\tWorld")
    •Output:
      Hello    World''')
    input("\nPress Enter to go back")

def stringlength():
    print('''STRING LENGTH:
    •Definition: The len() function is used to find the number of characters in a string.
    •Syntax: len(string)

    •Example: name = "Python"
              print(len(name))
    •Output: 6

    •Important: Spaces are also counted as characters.

    •Example: text = "Hello World"
              print(len(text))
    •Output: 11''')
    input("\nPress Enter to go back")



#List in python 
def lists():
    print()
    print("=" * 55)
    print("                 LISTS IN PYTHON")
    print("=" * 55)
    print('''A list is an ordered and changeable collection of items which is mutable
    
    Python has different types of operations on Lists:
    1. List definition and creation 
    2. List indexing 
    3. List slicing 
    4. List adding 
    5. List removing 
    6. List changing 
    7. List length
    8. Go to Previous 
    9. Go to Next 
    10. Go to Main Menu
    ''')
    choice = input("Enter your choice: ")
    
    if choice == "1":
        listdefinition()
    elif choice == "2":
        listindexing()
    elif choice == "3":
        listslicing()
    elif choice == "4":
        listadding()
    elif choice == "5":
        listremoving()
    elif choice == "6":
        listchanging()
    elif choice == "7":
        listlength()
    elif choice == "8":
        strings()
        return
    elif choice == "9":
        tuples()
        return
    elif choice == "10":
        return
    else:
        print("Invalid choice! Please try again.")

def listdefinition():
    print('''LIST DEFINITION AND CREATION:
    •Definition: A list is an ordered and changeable collection of items.
    •Syntax: variable = [item1, item2, item3]

    •Example: fruits = ["Apple", "Banana", "Mango"]
    •Output: ["Apple", "Banana", "Mango"]

    •Important: Lists are written using square brackets [ ].
    •Checking the type: print(type(fruits))
    •Output: <class 'list'>''')
    input("\nPress Enter to go back")

def listindexing():
    print('''LIST INDEXING:
    •Definition: List indexing is used to access individual elements from a list.
    •Syntax: list[index]

    •Example: fruits = ["Apple", "Banana", "Mango"]
              print(fruits[0], fruits[2])
    •Output: Apple, Mango

    •Important: List indexing starts from index 0.
    •Negative Indexing: Negative indexes access elements from the end.

    •Example: print(fruits[-1])
    •Output: Mango''')
    input("\nPress Enter to go back")

def listslicing():
    print('''LIST SLICING:
    •Definition: List slicing is used to access a part of a list.
    •Syntax: list[start:stop]

    •Example: numbers = [10, 20, 30, 40, 50]
              print(numbers[1:4])
    •Output: [20, 30, 40]

    •Important: The stop index is not included.

    •Example: print(numbers[:3])
    •Output: [10, 20, 30]

    •Example: print(numbers[2:])
    •Output: [30, 40, 50]''')
    input("\nPress Enter to go back")

def listadding():
    print('''ADDING ITEMS TO A LIST:
    •Definition: Items can be added to a list using append()
    •append(): Adds an item at the end of the list.

    •Example: numbers = [1, 2, 3]
              numbers.append(4)
    •Output: [1, 2, 3, 4]''')
    input("\nPress Enter to go back")

def listremoving():
    print('''REMOVING ITEMS FROM A LIST:
    •Definition: Items can be removed from a list using remove(), pop() and del.

    •remove(): Removes a specific value.
    •Example: numbers = [10, 20, 30]
              numbers.remove(20)
    •Output: [10, 30]

    •pop(): Removes an item using its index.
    •Example: numbers.pop(0)
    •Output: [20, 30]

    •del: Deletes an item using its index.
    •Example: del numbers[1]
    •Output: [10, 30]''')
    input("\nPress Enter to go back")

def listchanging():
    print('''CHANGING LIST ITEMS:
    •Definition: List elements can be changed because lists are mutable
    •Syntax: list[index] = new_value

    •Example: fruits = ["Apple", "Banana", "Mango"]
              fruits[1] = "Orange"
    •Output: ["Apple", "Orange", "Mango"]

    •Important: Lists are mutable, which means their elements can be changed after creation.''')
    input("\nPress Enter to go back")

def listlength():
    print('''LIST LENGTH:
    •Definition: The len() function is used to find the number of items in a list.
    •Syntax: len(list)

    •Example: numbers = [10, 20, 30, 40]
              print(len(numbers))
    •Output: 4

    •Important: len() counts the total number of items in the list.''')
    input("\nPress Enter to go back")



#Tuples in python 
def tuples():
    print()
    print("=" * 55)
    print("                 TUPLES IN PYTHON")
    print("=" * 55)
    print('''A tuple is an ordered and unchangeable collection of items

        Python has different types of operations on Tuple:
        1. Tuple definition and creation 
        2. Tuple indexing 
        3. Tuple slicing 
        4. Tuple length
        5. Go to Previous
        6. Go to Next 
        7. Go to Main Menu 
        ''')
    choice = input("Enter your choice: ")
    
    if choice == "1":
        tupledefinition()
    elif choice == "2":
        tupleindexing()
    elif choice == "3":
        tupleslicing()
    elif choice == "4":
        tupleslicing()
    elif choice == "5":
        lists()
        return
    elif choice == "6":
        sets()
        return
    elif choice == "7":
        return
    else:
        print("Invalid choice! Please try again.")

def tupledefinition():
    print('''TUPLES:
    •Definition: A tuple is an ordered and unchangeable collection of items
    •Syntax: variable = (item1, item2, item3)
    •Example: fruits = ("Apple", "Banana", "Mango")
    •Output: ("Apple", "Banana", "Mango")
    •Important: Tuples are written using round brackets ()
    •Checking the type: print(type(fruits))
    •Output: <class 'tuple'>''')
    input("\nPress Enter to go back")

def tupleindexing():
    print('''TUPLE INDEXING:
    •Definition: Tuple indexing is used to access individual elements from a tuple
    •Syntax: tuple[index]

    •Example: fruits = ("Apple", "Banana", "Mango")
              print(fruits[0], print[2])
    •Output: Apple, Mango


    •Important: Tuple indexing starts from index 0
    •Negative Indexing: Negative indexes access elements from the end

    •Example: print(fruits[-1])
    •Output: Mango''')
    input("\nPress Enter to go back")

def tupleslicing():
    print('''TUPLE SLICING:
    •Definition: Tuple slicing is used to access a part of a tuple
    •Syntax: tuple[start:stop]

    •Example: numbers = (10, 20, 30, 40, 50)
              print(numbers[1:4])
    •Output: (20, 30, 40)

    •Important: The stop index is not include
    •Example: print(numbers[:3])
    •Output: (10, 20, 30)

    •Example: print(numbers[2:])
    •Output: (30, 40, 50)''')
    input("\nPress Enter to go back")

def tuplelength():
    print('''TUPLE LENGTH:
    •Definition: The len() function is used to find the number of items in a tuple
    •Syntax: len(tuple)

    •Example: numbers = (10, 20, 30, 40)
              print(len(numbers))
    •Output: 4

    •Important: len() counts the total number of items in the tuple''')
    input("\nPress Enter to go back")



#Sets in Python
def sets():
    print()
    print("=" * 55)
    print("                 SETS IN PYTHON")
    print("=" * 55)
    print('''A set is an unordered and changeable collection of unique items

    Python has different types of operations on Sets:

        1. Set definition 
        2. Set creation
        3. Set adding 
        4. Set removing
        5. Set union 
        6. Set intersection
        7. Set difference
        8. Set membership
        9. Set length
        10. Go to Previous
        11. Go to Next 
        12. Go to Main Menu
        ''')
    choice = input("Enter your choice: ")
    
    if choice == "1":
        setdefinition()
    elif choice == "2":
        setcreation()
    elif choice == "3":
        setadding()
    elif choice == "4":
        setremoving()
    elif choice == "5":
        setunion()
    elif choice == "6":
        setintersection()
    elif choice == "7":
        setdifference()
    elif choice == "8":
        setmembership()
    elif choice == "9":
        setlength()
    elif choice == "10":
        tuples()
        return
    elif choice == "11":
        dictionaries()
        return
    elif choice == "12":
        return
    else:
        print("Invalid choice! Please try again.")

def setdefinition():
    print('''SET DEFINITION:
    •Definition: A set is an unordered and changeable collection of unique items
    •Syntax: variable = {item1, item2, item3}

    •Example: numbers = {10, 20, 30}
    •Output: {10, 20, 30}

    •Important: Sets do not allow duplicate values
    •Checking the type: print(type(numbers))
    •Output: <class 'set'>''')
    input("\nPress Enter to go back")

def setcreation():
    print('''SET CREATION:
    •Definition: A set can be created by placing values inside curly brackets { }
    •Syntax: set_name = {values}

    •Example: fruits = {"Apple", "Banana", "Mango"}
    •Output: {"Apple", "Banana", "Mango"}

    •Important: An empty set is created using set(), not {}

    •Example: numbers = set()
    •Checking the type: print(type(numbers))
    •Output: <class 'set'>''')
    input("\nPress Enter to go back")

def setadding():
    print('''SET ADDING:
    •Definition: The add() method is used to add a single item to a set
    •Syntax: set.add(value)

    •Example: numbers = {1, 2, 3}
              numbers.add(4)
    •Output: {1, 2, 3, 4}

    •Important: If the item already exists, it will not be added again''')
    input("\nPress Enter to go back")

def setremoving():
    print('''SET REMOVING:
    •Definition: Items can be removed from a set using remove(), discard() and pop()
    •remove(): Removes a specific item.

    •Example: numbers = {1, 2, 3}
              numbers.remove(2)
    •Output: {1, 3}

    •discard(): Removes an item without giving an error if it does not exist
    •pop(): Removes an arbitrary item from the set.''')
    input("\nPress Enter to go back")

def setunion():
    print('''SET UNION:
    •Definition: Union combines all unique elements from two or more sets
    •Syntax: set1.union(set2)

    •Example: A = {1, 2, 3}
              B = {3, 4, 5}
              print(A.union(B))
    •Output: {1, 2, 3, 4, 5}''')
    input("\nPress Enter to go back")

def setintersection():
    print('''SET INTERSECTION:
    •Definition: Intersection returns the elements that are common in two or more sets
    •Syntax: set1.intersection(set2)

    •Example: A = {1, 2, 3}
              B = {2, 3, 4}
              print(A.intersection(B))
    •Output: {2, 3}''')
    input("\nPress Enter to go back")

def setdifference():
    print('''SET DIFFERENCE:
    •Definition: Difference returns the elements that are present in one set but not in another set
    •Syntax: set1.difference(set2)

    •Example: A = {1, 2, 3}
              B = {2, 3, 4}
              print(A.difference(B))
    •Output: {1}''')
    input("\nPress Enter to go back")

def setmembership():
    print('''SET MEMBERSHIP:
    •Definition: Membership operators are used to check whether an item exists in a set
    •Operators: in, not in

    •Example: numbers = {1, 2, 3}
              print(2 in numbers)
    •Output: True

    •Example: print(5 not in numbers)
    •Output: True''')
    input("\nPress Enter to go back")

def setlength():
    print('''SET LENGTH:
    •Definition: The len() function is used to find the number of items in a set
    •Syntax: len(set)

    •Example: numbers = {10, 20, 30, 40}
              print(len(numbers))
    •Output: 4

    •Important: Duplicate values are not counted because sets contain only unique items''')
    input("\nPress Enter to go back")



#Dictionaries in Python
def dictionaries():
    print()
    print("=" * 55)
    print("                 DICTIONARIES IN PYTHON")
    print("=" * 55)
    print('''A dictionary is a collection of key-value pairs used to store data
    
    Python has different operations on dictionaries:
    
    1. Dictionary definition
    2. Dictionary accessing
    3. Dictionary adding
    4. Dictionary changing
    5. Dictionary removing
    6. Dictionary keys and values
    7. Dictionary length
    8. Dictionary checking keys
    9. Go to Previous 
    10. Go to Next 
    11. Go to Main menu 
    ''')
    choice = input("Enter your choice: ")
    
    if choice == "1":
        dictionarydefinition()
    elif choice == "2":
        dictionaryaccessing()
    elif choice == "3":
        dictionaryadding()
    elif choice == "4":
        dictionarychanging()
    elif choice == "5":
        dictionaryremoving()
    elif choice == "6":
        dictionarykeysandvalues()
    elif choice == "7":
        dictionarylength()
    elif choice == "8":
        dictionarycheckingkeys()
    elif choice == "9":
        sets()
        return
    elif choice == "10":
        inputfunction()
        return
    elif choice == "11":
        return
    else:
        print("Invalid choice! Please try again.")

def dictionarydefinition():
    print('''DICTIONARY DEFINITION:
    •Definition: A dictionary is a collection of key-value pairs used to store data
    •Syntax: variable = {key: value}

    •Example: student = {"name": "Abhay", "age": 18}
    •Output: {"name": "Abhay", "age": 18}

    •Important: Dictionaries are written using curly brackets { }
    •Checking the type: print(type(student))
    •Output: <class 'dict'>''')
    input("\nPress Enter to go back")

def dictionaryaccessing():
    print('''ACCESSING DICTIONARY VALUES:
    •Definition: Dictionary values can be accessed using their keys
    •Syntax: dictionary[key]

    •Example: student = {"name": "Abhay", "age": 18}
              print(student["name"])
    •Output: Abhay

    •Example: print(student["age"])
    •Output: 18

    •Important: We use the key to access its corresponding value''')
    input("\nPress Enter to go back")

def dictionaryadding():
    print('''ADDING ELEMENTS IN A DICTIONARY:
    •Definition: A new key-value pair can be added to a dictionary by assigning a value to a new key
    •Syntax: dictionary[key] = value

    •Example: student = {"name": "Abhay"}
              student["age"] = 18
    •Output: {"name": "Abhay", "age": 18}

    •Important: Dictionaries are changeable, so new items can be added''')
    input("\nPress Enter to go back")

def dictionarychanging():
    print('''CHANGING DICTIONARY VALUES:
    •Definition: The value of an existing key can be changed by assigning a new value
    •Syntax: dictionary[key] = new_value

    •Example: student = {"name": "Abhay", "age": 18}
              student["age"] = 19
    •Output: {"name": "Abhay", "age": 19}

    •Important: The key remains the same while its value is changed''')
    input("\nPress Enter to go back")

def dictionaryremoving():
    print('''REMOVING ITEMS FROM A DICTIONARY:
    •Definition: Dictionary items can be removed using pop(), popitem() and del

    •pop(): Removes an item using its key
    •Example: student = {"name": "Abhay", "age": 18}
              student.pop("age")
    •Output: {"name": "Abhay"}
    •popitem(): Removes the last inserted key-value pair

    •del: Deletes an item using its key
    •Example: del student["name"]
    •Output: {}''')
    input("\nPress Enter to go back")

def dictionarykeysandvalues():
    print('''DICTIONARY KEYS AND VALUES:
    •Definition: Keys identify the data, while values are the data stored with those keys

    •Example: student = {"name": "Abhay", "age": 18}
    •Key: "name"
    •Value: "Abhay"

    •Key: "age"
    •Value: 18

    •Important: Keys must be unique, but values can be repeated''')
    input("\nPress Enter to go back")

def dictionarylength():
    print('''DICTIONARY LENGTH:
    •Definition: The len() function is used to find the number of key-value pairs in a dictionary
    •Syntax: len(dictionary)

    •Example: student = {"name": "Abhay", "age": 18}
              print(len(student))
    •Output: 2

    •Important: len() counts the number of key-value pairs''')
    input("\nPress Enter to go back")

def dictionarycheckingkeys():
    print('''DICTIONARY MEMBERSHIP:
    •Definition: The in and not in operators are used to check whether a key exists in a dictionary
    •Syntax: key in dictionary

    •Example: student = {"name": "Abhay", "age": 18}
              print("name" in student)
    •Output: True

    •Example: print("marks" not in student)
    •Output: True

    •Important: Membership checking in dictionaries is done on keys''')
    input("\nPress Enter to go back")



#Input in Python
def inputfunction():
    print()
    print("=" * 55)
    print("                 INPUT IN PYTHON")
    print("=" * 55)
    print('''
    •Definition: The input() function is used to take data from the user.
    •Syntax: input("message")

    •Example: name = input("Enter your name: ")
    •Input: Abhay
    •Output: Abhay

    •Important: The input() function always takes the entered value as a string.''')



#Output in Python
def outputfunction():
    print()
    print("=" * 55)
    print("                 OUTPUT IN PYTHON")
    print("=" * 55)
    print('''
    •Definition: The print() function is used to display information on the screen.
    •Syntax: print(value)

    •Example: print("Hello World")
    •Output: Hello World

    •Example: age = 18
              print(age)
    •Output: 18

    •Important: print() can display text, numbers, variables and expressions.''')



#Conditional Statements in Python
def conditionalstatements():
    print()
    print("=" * 55)
    print("                 CONDITIONAL STATEMENTS IN PYTHON")
    print("=" * 55)
    print('''A conditional statement tells python to make a decision on whether a specific condition is true or false
    
    Python has three different conditional statements:
    1. if conditional statement 
    2. elif conditional statement
    3. else conditional statement
    4. Go to Previous 
    5. Go to Next 
    6. Go to Main Menu 
    ''')

    choice = input("Enter your choice: ")
    
    if choice == "1":
        ifconditional()
    elif choice == "2":
        elifconditional()
    elif choice == "3":
        elseconditional()
    elif choice == "4":
        outputfunction()
        return
    elif choice == "5":
        loops()
        return
    elif choice == "6":
        return
    else:
        print("Invalid choice! Please try again.") 

def ifconditional():
    print('''IF STATEMENT:
    •Definition: The if statement is used to execute a block of code when a condition is True
    •Syntax: if condition:
                  statement

    •Example: age = 18
              if age >= 18:
                  print("You are an adult")
    •Output: You are an adult

    •Important: The code inside the if statement runs only when the condition is True''')
    input("\nPress Enter to go back")

def elifconditional():
    print('''ELIF STATEMENT:
    •Definition: The if-else statement is used to execute one block when a condition is True and another block when it is False

    •Syntax: if condition:
                  statement
              else:
                  statement
    •Example: age = 16
              if age >= 18:
                  print("Adult")
              else:
                  print("Minor")
    •Output: Minor

    •Important: Either the if block or the else block is executed''')
    input("\nPress Enter to go back")

def elseconditional():
    print('''ELSE STATEMENT:
    •Definition: The if-elif-else statement is used to check multiple conditions

    •Syntax: if condition:
                  statement
              elif condition:
                  statement
              else:
                  statement
    •Example: marks = 75
              if marks >= 90:
                  print("A")
              elif marks >= 60:
                  print("B")
              else:
                  print("C")
    •Output: B

    •Important: Python checks the conditions from top to bottom and executes the first True condition''')
    input("\nPress Enter to go back")



#Loops in Python
def loops():
    print()
    print("=" * 55)
    print("                 LOOPS IN PYTHON")
    print("=" * 55)
    print('''
    •Definition: A loop is used to repeatedly execute a block of code
    •Types of Loops: 
    1. for loop
    2. while loop
    3. Go to Previous 
    4. Go to Next 
    5. Go to Main Menu

    •Example: for i in range(5):
                  print(i)
    •Output:
      0
      1
      2
      3
      4

    •Important: Loops are useful when we need to repeat a task multiple times.''')
    choice = input("Enter your choice: ")

    if choice == "1":
        forloop()
    elif choice == "2":
        whileloop()
    elif choice == "3":
        conditionalstatements()
        return
    elif choice == "4":
        precedence()
        return
    elif choice == "5":
        return
    else:
        print("Invalid choice! Please try again.") 

def forloop():
    print()
    print("=" * 55)
    print("                 FOR LOOP IN PYTHON")
    print("=" * 55)
    print('''
    •Definition: A for loop is used to iterate over a sequence or a range of values
    •Syntax: for variable in sequence:
                  statement

    •Example: for i in range(5):
                  print(i)
    •Output:
      0
      1
      2
      3
      4

    •Important: The for loop automatically moves to the next item after each iteration''')
    input("\nPress Enter to go back")

def whileloop():
    print()
    print("=" * 55)
    print("                 WHILE LOOP IN PYTHON")
    print("=" * 55)
    print('''
    •Definition: A while loop repeatedly executes a block of code as long as a condition is True
    •Syntax: while condition:
                  statement

    •Example: i = 1
              while i <= 5:
                  print(i)
                  i += 1
    •Output
      1
      2
      3
      4
      5

    •Important: The condition is checked before every iteration''')
    input("\nPress Enter to go back")



#Precedence in Python
def precedence():
    print()
    print("=" * 55)
    print("                 PRECEDENCE IN PYTHON")
    print("=" * 55)
    print('''
    •Definition: Operator precedence determines the order in which operators are evaluated in an expression

    •Example: result = 10 + 5 * 2
    •Calculation: Multiplication is performed first.
                  10 + (5 * 2)
                  10 + 10
    •Output: 20

    •Important: Operators with higher precedence are evaluated before operators with lower precedence''')
    input("\nPress Enter to go back")



#Associativity in Python
def associativity():
    print()
    print("=" * 55)
    print("                  ASSOCIATIVITY IN PYTHON")
    print("=" * 55)
    print('''
    •Definition: Associativity determines the order in which operators with the same precedence are evaluated
    •Types: Left-to-right and Right-to-left

    •Example: result = 10 - 5 + 2
    •Calculation: (10 - 5) + 2
                  5 + 2
    •Output: 7

    •Important: Most Python operators are evaluated from left to right''')
    input("\nPress Enter to go back")



#Practise Codes 
def program1():
    # 1) Sum of list items
    list_1 = [1,2,3,4,5]
    total = 0
    for i in range(len(list_1)):
        total = total + list_1[i] 
    print("List:", list_1)    
    print("Total Sum=", total)    
    print()

def program2():
    # 2) Average of list elements 
    list_2 = [1,3,5,7,9]
    total = 0
    for i in range(len(list_2)):
        total = total + list_2[i]
    print("List:", list_2)  
    print("Average:", total/len(list_2))  
    print()

def program3():
# 3) Maximum element in a list 
    list_3 = [1,1,6,10,12]
    maximum = list_3[0]
    for i in range(len(list_3)):
        if list_3[i] > maximum:
            maximum = list_3[i]
    print("List:", list_3)    
    print("Maximum element in the list is:", maximum)        
    print()

def program4():
    # 4) Minimum element in a list
    list_4 = [1,3,4,9,1]
    minimum = list_4[0]
    for i in range(len(list_4)):
        if list_4[i] < minimum:
            minimum = list_4[i]
    print("List:", list_4)
    print("Minimum element in the list is:", minimum)
    print()    

def program5():
    # 5) Count even and odd numbers in a list 
    list_5 = [1,2,3,4,5,6,7,8,9,10]
    even = 0
    odd = 0
    for i in range(len(list_5)):
        if list_5[i] % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1
    print("Even numbers in the list:", even)  
    print("Odd numbers in the list:", odd)      
    print()

def program6():
    # 6) Reverse a list
    list_6 = [1,2,3,4,5]
    len(list_6)
    list_7 = []
    for i in range(len(list_6)):
        list_7.append(list_6[len(list_6)-1-i])
    print("Original List:", list_6)    
    print("Reversed List:", list_7)
    print()

def program7():
# 7) Linear search in a list
    list_8 = [1,2,3,4,5]
    n = int(input("Enter a number: "))
    found = False
    for i in range(len(list_8)):
        if list_8[i] == n:
            found = True 
            print(f"Number is found at {i} index")
        else:
            print(f"Number is not found at {i} index")
            found = False 
    print()    

def program8():
    # 8) Bubble sort a list
    list_9 = [9,4,5,1,8,0]
    for i in range(len(list_9)):
        for j in range(len(list_9) - 1):
            if list_9[j] > list_9[j + 1]:
                list_10 = list_9[j]
                list_9[j] = list_9[j + 1]
                list_9[j + 1] = list_10
        print(list_9)

def program9():
    # 9) Count the occurence of an element in the list 
    list_11 = [1,2,2,2,3,1,4,3,4,1,6,7]
    a = int(input("Enter your number: "))
    count = 0
    for i in range(len(list_11)):
            if list_11[i] == a:
                count = count + 1
    print("List: ", list_11)            
    print(f"Occurence of {a} is:", count)

def program10():
    # 10) Second largest element in a list
    list_12 = [1,2,3,4,5,6,7]
    for i in range(len(list_12)):
        swapped = False 
        for j in range(len(list_12) - 1 - i):
            if list_12[j] > list_12[j + 1]:
                list_12[j], list_12[j + 1] = list_12[j + 1], list_12[j]
                swapped = True 
        if swapped == False:
            break        
    print("List: ", list_12)    
    print("The second largest number is:", list_12[len(list_12) - 2])  
    print()    

def program11():
    # 11) Sum of elements in a tuple 
    tuple_1 = (1,2,3,4,5)
    total = 0
    for i in range(len(tuple_1)):
        total = total + tuple_1[i]
    print("The sum of elemnts:", total)    
    print()

def program12():
    # 12) Swap two elements in a tuple
    tuple_2 = (1,2,3,4,5,6)
    list_2 = list(tuple_2)
    print(list_2)
    a = int(input("Enter the index value to change from: "))
    b = int(input("Enter the index value to change to: "))
    if a and b in range(len(list_2)):
        list_2[a] , list_2[b] = list_2[b] , list_2[a]
        
    temp = tuple(list_2)
    print("The swapped tuple is: ", temp)    
    print()

def program13():
    # 13) Find max and min in a tuple
    tuple_3 = (1,2,3,4,5)
    maximum = tuple_3[0]
    minimum = tuple_3[0]
    for i in range(len(tuple_3)):
        if tuple_3[i] > maximum:
            maximum = tuple_3[i]
    print("The maximum in this tuple is:", maximum)
    for j in range(len(tuple_3)):
        if tuple_3[i] < minimum:
            minimum = tuple_3[i]
    print("The minimum in this tuple is:", minimum)
    print()

def program14():
    # 14) Convert list into a tuple and tuple into a list
    a = list(map(int, input("Enter your list elements here: ").split()))
    b = tuple(map(int, input("Enter your tuple elements here: ").split()))
    print("List:", a)
    print("Tuple:", b)
    print("From list to tuple:", tuple(a))
    print("From tuple to list:", list(b))
    print()

def program15():
    #15) Concatentaion of two tuples
    tuple_2 = tuple(map(int, input("Enter your tuple1 elements here: ").split()))
    tuple_3 = tuple(map(int, input("Enter your tuple2 elements here: ").split()))
    tuple_4 = (tuple_2 + tuple_3)
    print(tuple_4)
    print()

def program16():
    # 16) Check whether a number is prime or not 
    n = int(input("Enter your number here: "))
    for i in range(2,n):
        if n % i == 0:
            print(f"{n} is not a prime number")
            break
    else:
        print(f"{n} is a prime number")
    print()

def program17():
    #17) Check for Armstrong number 
    n = int(input("Enter your three digit number here: "))
    hundreds = n // 100
    tens = (n - (hundreds*100)) // 10
    ones = (n - (hundreds*100) - (tens*10))
    if (hundreds**3) + (tens**3) + (ones**3) == n:
        print(f"{n} is an Armstrong Number")
    else:
        print(f"{n} is not an Armstrong Number") 
    print()    

def program18():
    #18) Check for a palindrome number
    n = input("Enter your number here: ")
    reverse = ""
    for i in range(len(n) -1, -1, -1):
        reverse = reverse + n[i]
    if n == reverse:
        print("The number is a palindrome")
    else:
        print("The number is not a palindrome")
    print()                

def program19():
    #19) Sum of digits of a number
    n = input("Enter your number here: ")
    total = 0
    for i in range(0, len((n))):
        total = total + int(n[i])
    print(" =", total)
    print()    

def program20():
    #20) Factorial of a number
    n = int(input("Enter your number here: "))
    total = 1
    for i in range(1, n+1):
        total = total * i
    print(f"Factorial {n}! =", total) 
    print()       

def program21():
    #21) Fibonacci Series 
    n = int(input("Enter your number here: "))
    fib = [0,1]
    total = 0
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    print(fib)    
    for j in range(len(fib)):
        total = total + fib[j]
    print("Sum:", total)    
    print()    

def program22():
    #22) Multiplication table of a given number 
    n = int(input("Enter your number here: "))
    for i in range(1,11):
        print(f"{n} X {i} =", n*i)
    print()    

def program23():
    # 23) Largest of the three numbers
    a = int(input("Enter your first number here: "))
    b = int(input("Enter your second number here: "))
    c = int(input("Enter your third number here: "))
    if a > b and a > c:
        print(f"{a} is the largest number")
    elif b > c and b > a:
        print(f"{b} is the largest number")
    else:
        print(f"{c} is the largest")        
    print()    

def program24():
    # 24) Check for leap year 
    year = int(input("Enter your year: "))
    if year % 4 == 0:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
    print()        

def program25():
    #25) Grade Calculator 
    marks = int(input("Enter your marks here: "))
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "F"
    print("Marks:", marks)
    print("Grade:", grade)
    print()



#Home Page 
def learn_concept():
    while True:

        print()
        print("=" * 55)
        print("                 LEARN CONCEPT")
        print("=" * 55)

        print('''
        Choose a topic to learn:
        1. Operators 
        2. Variables
        3. Data Types
        4. Type Conversion
        5. Strings
        6. Lists
        7. Tuples
        8. Sets
        9. Dictionaries
        10. Input
        11. Output
        12. Conditional Statements
        13. Loops
        14. Precedence 
        15. Associativity

        16. Back to main menu''')

        choice = input("Enter your choice: ").lower()
        if choice == "1":
            operators()
        elif choice == "2":
            variables()
        elif choice == "3":
            datatypes()
        elif choice == "4":
            typeconversion()
        elif choice == "5":
            strings()
        elif choice == "6":
            lists()
        elif choice == "7":
            tuples()
        elif choice == "8":
            sets()
        elif choice == "9":
            dictionaries()
        elif choice == "10":
            inputfunction()
        elif choice == "11":
            outputfunction()
        elif choice == "12":
            conditionalstatements()
        elif choice == "13":
            loops()
        elif choice == "14":
            precedence()
        elif choice == "15":
            associativity()
        elif choice == "16":
            return
        else:
            print()
            print("Invalid choice ❌")
            print("Please choose a topic from the menu.")

def practise_codes():
    while True:

        print()
        print("=" * 60)
        print("                  PRACTISE CODES")
        print("=" * 60)

        print('''
        Choose a program:
        1. Sum of list items
        2. Average of list elements
        3. Maximum element in a list
        4. Minimum element in a list
        5. Count even and odd numbers
        6. Reverse a list
        7. Linear search
        8. Bubble sort
        9. Count occurrence of an element
        10. Second largest element
        11. Sum of tuple elements
        12. Swap two tuple elements
        13. Maximum and minimum in tuple
        14. Convert list and tuple
        15. Concatenation of two tuples
        16. Prime number
        17. Armstrong number
        18. Palindrome number
        19. Sum of digits
        20. Factorial
        21. Fibonacci series
        22. Multiplication table
        23. Largest of three numbers
        24. Leap year
        25. Grade calculator
        
        26. Back to main menu''')

        choice = input("Enter your choice: ")

        if choice == "1":
            program1()

        elif choice == "2":
            program2()

        elif choice == "3":
            program3()

        elif choice == "4":
            program4()

        elif choice == "5":
            program5()

        elif choice == "6":
            program6()

        elif choice == "7":
            program7()

        elif choice == "8":
            program8()

        elif choice == "9":
            program9()

        elif choice == "10":
            program10()

        elif choice == "11":
            program11()

        elif choice == "12":
            program12()

        elif choice == "13":
            program13()

        elif choice == "14":
            program14()

        elif choice == "15":
            program15()

        elif choice == "16":
            program16()

        elif choice == "17":
            program17()

        elif choice == "18":
            program18()

        elif choice == "19":
            program19()

        elif choice == "20":
            program20()

        elif choice == "21":
            program21()

        elif choice == "22":
            program22()

        elif choice == "23":
            program23()

        elif choice == "24":
            program24()

        elif choice == "25":
            program25()

        elif choice == "0":
            return

        else:
            print()
            print("Invalid choice ❌")
            print("Please choose a program from 1 to 25.")
    
def main_menu():
    while True:

        print()
        print("=" * 60)
        print("          PYTHON LEARNING & PRACTICE TOOL")
        print("=" * 60)

        print("""
        Welcome to the Mini Python Encyclopedia!

        What would you like to do?

        1. Learn Concept
        2. Practise Codes
        3. None
        """)

        choice = input("Enter your choice: ").lower()
        if choice == "1":
            learn_concept()
        elif choice == "2":
            practise_codes()
        elif choice == "3" or choice == "none":
            print()
            print("You either learn or you practise, none was never an option 🔥")
            input("Press Enter to return to the Main Menu!")
            
main_menu()