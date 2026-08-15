import random
alphabet = ["a", "b","c","d"]
number= ["1","2","3","4","5"]
symble =["@","#","$"]
letters_num = int(input ("how many letters do you want your password to have?"))
symble_num =int (input (" how many symbles do you want your password to have?"))
int_num = int (input ("how many numbers do you want your password to have?"))
password_list=[]
for i in range(0,letters_num ):
    password_list.append(random.choice(alphabet))
for i in range(0,symble_num ):
    password_list.append(random.choice(symble))
for i in range(0,int_num ):
    password_list.append(random.choice(number))

random.shuffle(password_list)
password=""
for char in password_list:
    password+=char
print (password)
