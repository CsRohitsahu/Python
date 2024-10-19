# multiplication of entered no. using recursion
def tab_rec(n,i):
    if(i>10):
        return 15
    print(n,"*",i,"=",n*i)    
    return tab_rec(n,i+1)
num=int(input("Enter no. you want to print table of:")) 
print("\nTable of "+str(num)+"is:")
tab_rec(num,1)



