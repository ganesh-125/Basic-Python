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

# isdigit
print(MyString.isdigit())

# lower
MyString ='GANESH'
print(MyString.lower())

# upper
MyString ='ganesh'
print(MyString.upper())

# splitlines
MyString ='ganesh\nprajapati'
print(MyString.splitlines())

# split (Default it will space to split string and return into list)
MyString ='ganesh prajapati'
print(MyString.split())

# strip to remove all leading and trailing whitespace from string
MyString ='  ganesh  '
print("Before strip : ",len(MyString))
MyString = MyString.strip()
print("After strip : ",len(MyString))

