a = 5
b= 6

# permuttation 
a = a + b # a devient 11
b = a - b # b devient 5 ( 11 - 6)
a = a - b # a devient 6 ( 11 - 5)

print("a = ", a)
print("b =" ,b)



a,  b = b , a

print("a = ", a)
print("b =" ,b)