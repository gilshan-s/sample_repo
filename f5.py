import re
pattern=input("Enter the pattern:")
D1=re.match(pattern,"Django")
if(D1!=None):
    print(pattern,":Pattern  is matched ....")
else:
    print(pattern,":Pattern is not matched ...")
print()



 





