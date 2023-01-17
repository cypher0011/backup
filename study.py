x = abs(-7.25) #absolute value of the specified number.
print(x)
x = 5
print(callable(x)) #returns True if the specified object is callable,in the def, otherwise it returns False.

string = "Python is interesting."

# string with encoding 'utf-8'
arr = bytes(string, 'utf-8') #The bytes() method returns a bytes object of the given size and initialization values.
print(arr)

print(chr(0x69))

x = dict(name = "John", age = 36, country = "Norway",moaz = "test")
#The dict() function creates a dictionary.
print(x)

x = divmod(11, 2) #11//2 = 5 | 11%2=1
print(x)



x = ('apple', 'banana', 'cherry')
y = enumerate(x)
print(list(y))

x = 'print(1)'
eval(x)

x = 'name = "John"\nprint(name)'
exec(x)

x = float(3)
print(x)
x = float("3.500")
print(x)

x = isinstance("moaz", str) #The isinstance() function returns True if the specified object is of the specified type, otherwise False.


print(x)


txt = "50"

x = txt.zfill(10)

print(x)


a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = zip(a, b)

a = ('apple', 'banana', 'cherry')
b = "Hello World"
c = 33

x = type(a)
y = type(b)
z = type(c)

print(x)
print(y)
print(z)

a = (1, 2, 3, 4, 5)
x = sum(a)
print(x) #sum all the numbers

x = str(3.5)
print(x) # now it's a string


a = ("b", "g", "a", "d", "f", "c", "h", "e")
x = sorted(a)
print(x)


a = ("a", "b", "c", "d", "e", "f", "g", "h")

x = slice(2)

print(a[x])

#slice(start end, step),
a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(3, 5)
print(a[x])


x = round(5.76543, 2)
print(x)

print(round(5.423423))
print(round(5.743453))

x = pow(4, 3) #Return the value of 4 to the power of 3 (same as 4 * 4 * 4)
print(x)


mylist = ["apple", "orange", "cherry"]

x = len(mylist)

print(x)


# create a list
prime_numbers = [2, 3, 5, 7, 9, 11]

# remove 9 from the list
prime_numbers.remove(9)


# Updated prime_numbers List
print('Updated List: ', prime_numbers)

# Output: Updated List:  [2, 3, 5, 7, 11]



# animals list
animals = ['cat', 'dog', 'rabbit', 'guinea pig']

# 'rabbit' is removed
animals.remove('rabbit')


# Updated animals List
print('Updated animals list: ', animals)


a = ["apple", "banana", "cherry"]

b = ["Ford", "BMW", "Volvo"]

a.extend(b)

print(a)




x = 5

if x % 2 ==0:
    print("ood")

else:
    print("even")

x = 5.19054
y = str(x)
z = len(y)
print(int(z-2))

str1 = 'test'
print(type(str1))

s = 'a123b'

for char in s:
    print(char, char.isalpha())




num = 13
x = sum(range(1,num+1))
print(x)


#s.replace

def remove(s):
    s = s.replace("!","")

    s = s + "!"

    return s

print(remove("He!!llo! world!!"))

txt = "apple#banana#cherry#orange"

x = txt.split("#")

print(x)

txt = "appl banana cherry orange"

x = txt.split(" ")

print(x)


a = []
for i in range(10):
    a.append(str(i))
print(a)
a =' '.join(a)
print(a)


firstName = 'Ahmad'
contains = 'A'


for i in range(len(firstName)):
    if firstName[i] == contains:
        print("true")
if firstName[i] != contains:
    print("false")



x = "HI!! M!O!A!Z"
x = x.replace("!","")
print(x+"!")
