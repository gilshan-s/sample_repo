def Test_Case1(obj2):
    return obj2*5
if(__name__=="__main__"):
    obj2=[12,15,17,18,21,22,23,24,25]
    l1=list(map(Test_Case1,obj2))
    print("The result is:",l1)
print()