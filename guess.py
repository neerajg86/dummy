# you guess number and enter the number

b=50
num_guess=1
print("\t number of guesss is 5:\n ")
while(num_guess):
    guess_num=int(input("\t guess the number:\n"))# print number 
    if guess_num<50:
        print("\t give number high \n")# if number less then print
    elif guess_num>50:
        print("\t give number less \n")# if number high then print 
    else:
        print("you won ")# if number 50 then print
        break

    print(5-num_guess,"\t number of guess left \n")
    num_guess=num_guess+1


    if(num_guess>5):
        print("\t end game \n")
        break
