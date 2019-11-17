for row in range(10):
    for col in range(11):
        if(row!=0)and(col==0)or(row-col==0)or(row!=0)and(col==10) :
            print("#",end=" ")
        else:
            print(" ",end=" ")

    print()




