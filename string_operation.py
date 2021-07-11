MyString = "my Name is Ganesh prajapti"

# capitalize which will convert first later of string into capital later
print(MyString.capitalize())

# O/P - My name is ganesh prajapti.

# casefold
print(MyString.casefold())

# O/P - my name is ganesh prajapti.

# count the later in string
print(MyString.count('a'))

# O/P - 4

# encode which convert string into byte
print(MyString.encode())

# O/P - b'my Name is Ganesh prajapti.'

# endswith return True or Flase 
print(MyString.endswith('i'))

# O/P - True

# isalnum
print(MyString.isalnum())

MyString ='ganesh'
# isalpha
print(MyString.isalpha())

# isascii
print(MyString.isascii())

# isdecimal
MyString = '123'
print(MyString.isdecimal())

# O/P - True

# isdigit
print(MyString.isdigit())

# O/P - True

# lower
MyString ='GANESH'
print(MyString.lower())

# O/P - ganesh

# upper
MyString ='ganesh'
print(MyString.upper())

# O/P - GANESH

# splitlines
MyString ='ganesh\nprajapati'
print(MyString.splitlines())

# O/P - ['ganesh', 'prajapati']

# split (Default it will space to split string and return into list)
MyString ='ganesh prajapati'
print(MyString.split())

# O/P - ['ganesh', 'prajapati']

# strip to remove all leading and trailing whitespace from string
MyString ='  ganesh  '
print("Before strip : ",len(MyString))
MyString = MyString.strip()
print("After strip : ",len(MyString))

# O/P -
# Before strip :  10
# After strip :  6