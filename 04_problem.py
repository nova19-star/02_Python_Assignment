# 4. Write a python program to accept six subjects of one students and calculate its percentage.

s1=int(input("Enter mark for Odia: "))
s2=int(input("Enter mark for English: "))
s3=int(input("Enter mark for Math: "))
s4=int(input("Enter mark for Science: "))
s5=int(input("Enter mark for Biology: "))
s6=int(input("Enter mark for IT: "))

percentage = (s1+s2+s3+s4+s5+s6)/600*100
print("The percentage of the student is: ", percentage)
       
