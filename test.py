a = [5,7,8]
b = a
b[0]=1
print(a)
print(b)


ma_liste = [1,2,3]

testMap = map(lambda x : x+2, ma_liste)
testResult = set(testMap)
print(ma_liste)
print("res" , testResult)

