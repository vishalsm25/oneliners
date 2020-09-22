# 31.Pattern print - right half pyramid
print(*["*"*i for i in range(1,6)],sep='\n')
print('\n'.join('*'*i for i in range(1,6)))

# 32.Pattern print - left half pyramid
print(*[" "*(5-i-1)+"*"*(i+1) for i in range(5)],sep='\n')
print('\n'.join(' '*(5-i-1)+'*'*(i+1) for i in range(5)))

# 33.Pattern print - inverse of right half pyramid
print(*['*'*i for i in range(5,0,-1)],sep='\n')
print('\n'.join('*'*i for i in range(5,0,-1)))

# 34.Pattern print - square of stars
print(*["*"*5 for i in range(1,6)],sep="\n")
print('\n'.join('*'*5 for i  in range(1,6)))

# 35.Pattern print - pyramid
for i in range(1, 6):
  print (' ' * (5 - i), '* ' * i)
#remove the space in first string u get right half pyramid
#remove the space in second string u get left halg pyramid
  
# 36.Pattern print - pyramid without gap
print("\n".join((i*"*").center(5*2) for i in range(1, 5*2, 2)))
#another method
for i in range(6):
    print (' '*(6-i-1)+'*'*(2*i+1))
#remove the space in first string u get right half pyramid
#remove the space in second string u get left halg pyramid
     
# 36.Pattern print -Inverse pyramid without gap
print("\n".join((2*i*"*").center(5*2) for i in range(5, 0, -1)))

# 37.Pattern print-right half pyramid with no.s
print('\n'.join(str(i)*i for i in range(1, 6)))
print(*[str(i)*i for i in range(1,6)],sep='\n')

# 37.Pattern print - Diamond shape
print("\n".join((i*"*").center(5*2) for i in range(1, 5*2, 2)))
print("\n".join((i*"*").center(5*2) for i in range(9, -1, -2)))

# 38.Pattern print - Half pyramid with series numbers
print('\n'.join([''.join(['{}'.format(i) for i in range(1,j)]
                         ) for j in range(2,7)]))

# 39.Pattern print - Heart symbol
print('\n'.join([''.join([('Love'[(x-y) % len('Love')] if (
    (x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' '
      ) for x in range(-30, 30)]) for y in range(30, -30, -1)]))
#copied still need to practice this one

# 40.Replace string word with other string
s = 'My name is viper'
print(s.replace('viper','vishalaaaa'))

