def Test_Case1(obj1):
    if(obj1%2==0):
        return True 
    else:
        return False 
if(__name__=="__main__"):
    obj1=[1,2,3,4,5,6,7,9,10,11,12,13,14,15]
    l1=list(filter(Test_Case1,obj1))
    print("The result is:",l1)
print()   

    
