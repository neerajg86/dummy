#--------------*
#--------------* * *
#--------------* * * * *
#--------------* * * * * * *
#--------------* * * * * * * * *
print("\n")
print("\n")

k = 1
for i in range(0, 5):
    for j in range(0, k):
        print("* ", end="")
    k = k + 2
    print()
print("\n")
print("\n")
#------------------A
#------------------B C D
#------------------E F G H I
#------------------J K L M N O P
#------------------Q R S T U V W X Y


incr = 1
val = 65
for i in range(0, 5):
    for j in range(0, incr):
        ch = chr(val)
        print(ch, end=" ")
        val = val + 1
    incr = incr + 2
    print()
print("\n")
print("\n")

#-------------------------        A
#-------------------------      C B
#-------------------------    F E D
#-------------------------  J I H G
#-------------------------O N M L K

decr = 8
count = 64
val = 65
for i in range(0, 5):
    for k in range(0, decr):
        print(end=" ")
    for j in range(0, i+1):
        count = count + 1
    val = count
    temp = val
    for j in range(0, i+1):
        ch = chr(val)
        print(ch, end=" ")
        val = val - 1
    val = temp
    decr = decr - 2
    print()

print("\n")
print("\n")
#-----------------------1
#-----------------------2 3 4
#-----------------------5 6 7 8 9
#-----------------------10 11 12 13 14 15 16
#-----------------------17 18 19 20 21 22 23 24 25

num = 1
incr = 1
for i in range(0, 5):
    for j in range(0, incr):
        print(num, end=" ")
        num = num + 1
    print()
    incr = incr + 2
















