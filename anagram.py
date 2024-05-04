a=(input("enetr the string:"))
b=(input("enetr the string:"))
if len(a)!=len(b):
    print("it is not an anagram")
else:
    a=sorted(a)
    b=sorted(b)
if a==b:
    print("it is an anagram")
else:
    print("its is not an anagram")