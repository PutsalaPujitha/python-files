Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
2+3
5
4*6
24
8/4
2.0
5//2
2
8+2*3
14
(8+2)*3
30
2**3
8
10%3
1
'PUJITHA'
'PUJITHA'
print('puji')
puji
print('puji'slaptop)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print("puji's laptop")
puji's laptop
10*puji
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    10*puji
NameError: name 'puji' is not defined
10*(puji)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    10*(puji)
NameError: name 'puji' is not defined
puji**2
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    puji**2
NameError: name 'puji' is not defined
puji
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    puji
NameError: name 'puji' is not defined
10*'puji'
'pujipujipujipujipujipujipujipujipujipuji'
10*'\npuji'
'\npuji\npuji\npuji\npuji\npuji\npuji\npuji\npuji\npuji\npuji'
10*\n'puji'
SyntaxError: unexpected character after line continuation character
10*'puji\n'
'puji\npuji\npuji\npuji\npuji\npuji\npuji\npuji\npuji\npuji\n'
print('c:\docs\navin')
c:\docs
avin
print(10*'\npuji')

puji
puji
puji
puji
puji
puji
puji
puji
puji
puji
print(r'c:\docs\navin')
c:\docs\navin
#variables in python
x=2
x+5
7
x-2
0
x*3
6
x\2
SyntaxError: unexpected character after line continuation character
x/2
1.0
x=4
x+5
9
abc
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    abc
NameError: name 'abc' is not defined. Did you mean: 'abs'?
'abc'
'abc'
y=5
x+y
9
x-y
-1
x*y
20
x/y
0.8
x%y
4
name='youtube'
name
'youtube'
name+'rocky'
'youtuberocky'
num='34'
num
'34'
num+'22'
'3422'
frnds='sri'
frnds
'sri'
frnds+'puji'
'sripuji'
frnds[0]
's'
frnds[4]
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    frnds[4]
IndexError: string index out of range
frnds[2]
'i'
frnds[-1]
'i'
frnds[0:2]
'sr'
frnds[0]='d'
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    frnds[0]='d'
TypeError: 'str' object does not support item assignment
#because string in python are immutable
#list in python
#we use square braces
num=[12,13,14,15]
num
[12, 13, 14, 15]
names=[puji,meena,mani,sri]
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    names=[puji,meena,mani,sri]
NameError: name 'puji' is not defined
names=['puji','meena','mani','sri']
names
['puji', 'meena', 'mani', 'sri']
#list operations
names.append('mallesh')
names
['puji', 'meena', 'mani', 'sri', 'mallesh']
names.copy()
['puji', 'meena', 'mani', 'sri', 'mallesh']
names.extend()
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    names.extend()
TypeError: list.extend() takes exactly one argument (0 given)
names.exttend('pujitha')
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    names.exttend('pujitha')
AttributeError: 'list' object has no attribute 'exttend'. Did you mean: 'extend'?
names.extend('pujitha')
names
['puji', 'meena', 'mani', 'sri', 'mallesh', 'p', 'u', 'j', 'i', 't', 'h', 'a']
names.insert('tej')
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    names.insert('tej')
TypeError: insert expected 2 arguments, got 1
names.insert('tej',0)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    names.insert('tej',0)
TypeError: 'str' object cannot be interpreted as an integer
names.insert('tej','0')
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    names.insert('tej','0')
TypeError: 'str' object cannot be interpreted as an integer
names.insert(1,'tej')
names
['puji', 'tej', 'meena', 'mani', 'sri', 'mallesh', 'p', 'u', 'j', 'i', 't', 'h', 'a']
num=[1,2,3,4]
num
[1, 2, 3, 4]
names.extend(num)
names
['puji', 'tej', 'meena', 'mani', 'sri', 'mallesh', 'p', 'u', 'j', 'i', 't', 'h', 'a', 1, 2, 3, 4]
names.pop()
4
names.remove()
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    names.remove()
TypeError: list.remove() takes exactly one argument (0 given)
names.remove('sri')
names
['puji', 'tej', 'meena', 'mani', 'mallesh', 'p', 'u', 'j', 'i', 't', 'h', 'a', 1, 2, 3]
del names
names.reverse()
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    names.reverse()
NameError: name 'names' is not defined. Did you mean: 'name'?
num.reverse()
num
[4, 3, 2, 1]
num.min()
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    num.min()
AttributeError: 'list' object has no attribute 'min'
min(nums)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    min(nums)
NameError: name 'nums' is not defined. Did you mean: 'num'?
min(num)
1
max(num)
4
num.sort()
num
[1, 2, 3, 4]
#tuples
tup(21,34,23)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    tup(21,34,23)
NameError: name 'tup' is not defined
tup
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    tup
NameError: name 'tup' is not defined
'tup'
'tup'
tup=(12,13,14)
tup
(12, 13, 14)
tup[1]
13
tup[1]=33
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    tup[1]=33
TypeError: 'tuple' object does not support item assignment
tup.count
<built-in method count of tuple object at 0x000001894F6B7280>















tup.count()
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    tup.count()
TypeError: tuple.count() takes exactly one argument (0 given)
s={23,24,25,26}
s
{24, 25, 26, 23}
#set is mutable same as list
#but diff is it does not follow the sequence
data={1:'puji',2:'mani',3:'meena'}
data
{1: 'puji', 2: 'mani', 3: 'meena'}
data.keys()
dict_keys([1, 2, 3])
data.values()
dict_values(['puji', 'mani', 'meena'])
data[2]
'mani'
data.get(1)
'puji'
keys=['puji','meena','ammu']
values=['python','java','cotlin']
dict(zip(keys,values))
{'puji': 'python', 'meena': 'java', 'ammu': 'cotlin'}



data['meena']='c'
data
{1: 'puji', 2: 'mani', 3: 'meena', 'meena': 'c'}
num=5
id(num)
1689253249392

type(pi)
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    type(pi)
NameError: name 'pi' is not defined
type(PI)
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    type(PI)
NameError: name 'PI' is not defined
pi
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    pi
NameError: name 'pi' is not defined
'pi'
'pi'
type('pi')
<class 'str'>
type(pi)
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    type(pi)
NameError: name 'pi' is not defined
pi=3.14
pi
3.14
type(pi)
<class 'float'>
a=5.6
b=int(a)
b
5
k=float(b)
k
5.0
c=complex(b,k)
c
(5+5j)
int(true)
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    int(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
int(True)
1
int(False)
0
range(10)
range(0, 10)
list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list(range(100))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
#operartors
x=2
y=3
x+y
5
x-y
-1
x*y
6
x/y
0.6666666666666666
x,y=3,4
x
3
y
4
x+=4
x
7
y+=4
y
8
x-=3
x
4
x>y
False
x<y
True
a=6
a==b
False
a=5
b=5
a<6&b<8
False
a<6&b<6
False
a<8andb<9
SyntaxError: invalid decimal literal
a<8&b<9
False
a<6 OR b<8
SyntaxError: invalid syntax. Perhaps you forgot a comma?
c=6
c
6
d=6
d
6
c<8 and d<5
False
c<8 and d<8
True
c<8 or d<5
True
bin(25)
'0b11001'
0b11001
25
bin(2)
'0b10'
oct(25)
'0o31'
hex(10)
'0xa'
#swap variables
a=5
b=6
a=b
b=a
print(a)
6
print(b)
6
a=5
b=6
temp=a
a=b
b=temp
print(a)
6
print(b)
5
#swapping without temp variable
a=6
b=9
a=a+b
a
15
a=a-b
a
6
b=a-b

b
-3
a=a+b
a
3
#bitwise operators
12&13
12
12/13
0.9230769230769231
12\13
SyntaxError: unexpected character after line continuation character
12|13
13
12^13
1
10<<2
40
10>>2
2
~12
-13
~1
-2
