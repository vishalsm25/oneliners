# 1.Palindrome 
# use string[::-1]==string[:]
Palindrome=lambda x:"PALINDROME" if x[::-1]==x[:] else "NOT PALINDROME"
print(Palindrome("MALAYALAM"))

# 2.Swap Two Variables
a,b=10,20
a,b=b,a #swapping
print(a,b)

# 3.Factorial of a number
n=5
from functools import reduce  #it is compulsory to import reduce from functools
print(reduce(lambda x, y: x * y, range(1, n+1)))
#another method
import math
print(math.factorial(5)) 

# 4.Fibonacci value and sequence for a number
fib=lambda x:x if x<=1 else fib(x-1)+fib(x-2) #displays fibonacci value
print(fib(5)) 
fib_seq=[fib(s) for s in range(fib(5))] #displays fiboncacci series
print(fib_seq)
#above two oneliners best for small values for large values it take long time
#it is better to avoid recursion in oneliners

# 5.Fibonacci series of no. without recursion
fib=lambda x,y=[1,1]:[1]*x if (x<2) else (
[y.append(y[q-1] + y[q-2]) for q in range(2,x)],y)[1]
print(fib(10))

# 6.Read a file
print([line.strip() for line in open("D:\\VIPER\\pyprograms\\programs\\file1.txt")])
#path name should always have double backslash

# 7.Find All Indices of an Element in a List
lst=[1,2,3,"viper","dboss",25,"viper",100,"viper"]
print([i for i in range(len(lst)) if lst[i]=='viper'])

# 8.Returns Set of all subsets
from functools import reduce
f = lambda l: reduce(lambda z, x: z + [y + [x] for y in z], l, [[]])
print(f([1,2,3]))

# 9.Returns combination of subsets of a set
from itertools import combinations 
print(list(combinations([1, 2, 3], 2)))

# 10.Print file extionsion
print('~/python/one-liners.py'.split('.')[-1])
print('~/python/one-liners.txt'.split('.')[-1])

# 11.Sorting the elements in the list
lst=[10,2,33,4,5,66,70,1]
lst.sort() #put reverse=True for ascending order
print(lst)

# 12.Get Multiple inputs from user with map and list comprehension
x =list((map(int, input("Enter a multiple value: ").split()))) 
print("values: ", x) 
x = [int(x) for x in input("Enter multiple value: ").split()] 
print("values: ", x)  

# 13.Get even and odd no.s list
print("even:",[x for x in range(20) if x%2==0])
print("even:",list(filter(lambda x:x%2==0,range(20))))
print("odd:",[x for x in range(20) if x%2!=0])

# 14.Square of even or odd numbers
evn_values=[x*x for x in range(21) if x%2==0]
odd_values=[x*x for x in range(21) if x%2!=0]
print(evn_values,odd_values)


# 15.Prime no.s between 1 to 100
prime_no=[x for x in range(2, 20) if all(x%y!=0 for y in range(2, x))]
print(prime_no)
prime_no1=list(filter(lambda x:all(x%y!=0 for y in range(2,x)),range(2,30)))
print(prime_no1)

# 16.Reverse a string
print("vishalsm"[::-1])

# 17.Sum of n numbers i.e 0 to 10
from functools import reduce
print(reduce(lambda x,y:x+y,range(11)))
#another method
print(10*(10+1)/2)
#easy method
print(sum(range(11)))

# 18.Display Calender
import calendar
calendar.prcal(2020)

# 19.Display Current date and Time
from datetime import datetime
now = datetime.now()
print(now.strftime("%d-%m-%Y %H:%M:%S"))

# 20.Get words having more than 4 characters
txt="i am creating powerful python one liners"
print([x for x in txt.split() if len(x)>4 ])

# 21.Display characeter and index in a string
a='abcdefg'
print([(i,a.index(i)) for i in a])
print([(a[i],i) for i in range(len(a))])

# 22.Display character and negative index of a string
a='abcdefg'
print([(a[i],i) for i in range(-len(a),0,1)])

# 23.Display no. from 0 to 20 in reverse order
print([n for n in range(20,-1,-1)])

# 24.Display all nos divisble by 5 and 7 between 1 to 150
print([n for n in range(1,151) if n%5==0 and n%7==0])

# 25.Count of every Character in a string
s='abcdeacdefhacbc'
print({i:s.count(i) for i in s})

# 26.Count of every Word in a string
s='ab bc abc dc ab abc dc bc bc abc dc ac'.split()
print({i:s.count(i) for i in s})

# 27.Remove duplicate values from list or string
lst=[1,2,3,"a","b","c",2,"a",1,"c",3]
st="abcd acdddd aaaabbbbcccdddd"
print("lst:",set(lst),"string:",set(st))
#easy method
lst=[1,2,3,"a","b","c",2,"a",1,"c",3]
print(*set(lst))

# 28.Replace values in string
import re
print(re.sub('man','women','ironman batman antman spiderman'))

# 29.Greatest common divisor between 2 no.s using recursion
gcd_no=lambda a,b:a if b==0 else gcd_no(b,a%b) 
print(gcd_no(24,18))

# 30.Generate any random no. between 0 to 20
import random
print(random.randint(0,20))
#every time it will display different values
