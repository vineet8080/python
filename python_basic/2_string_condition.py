# string 
# escape squence character
# 1.\n
# 2.concatenation (adding two string)
# 3.length(kitna word ya lanba hai )
# 4.indexing(position pe kya hai pata chalta h)
# 5.slicing

# 1.(line ko change karne ke liye)
# str="the nuber is good.the number is large"
# print(str)
# str="the nuber is good.\nthe number is large"
# print(str)

# 2.(jo string ko jodhnsa hoga to)
# str1="vineet "
# str2="yadav"
# print(str1+str2)

# 3.
# str2="yadav"
# print(len(str2))

# 4.(0 se start hota hai, sdqare bracket me position daal dene ka)
# str2="yadav"
# print(str2[4])

# 5.(slicinfg kaha se kaha tak karna hai use sqare braket me daal do )
# str="vineet yadav"
# print(str[4:9])
# print(str[4:])
# print(str[:9])

# string function

# 1.str.endswith("er.") last wala er rha to return karega
# 2.str.capitalize()   pahila letter ko capalize kr dega 
# 3.str.replace(old,new)   word or letter ko replace kr deta h 
# 4. str.find(word)         find at first iterantion uska position batata h
# 5.str.counrt("the")        kitni baar wo chiz hai use count kr dega 
# more........



# pratice question
# 1.wap to input user first name & print its lemgth

# a=str(input("write your name"))
# print(len(a))

# 2.wap to find the occurrance of '$' in a string

# a=input("enter the setence which inbuild with a '$' ")
# print(a.count("$"))

# str=input("enter the setence which inbuild with a '$' ")
# print(str.count("$"))





####### CONDITIONAL STATEMENT #####
 
# 1. IF STATEMENT
# age=78
# if(age>=18):
#     print("he can vote")
#     print("he can drive")

# 1. IF elif STATEMENT
# age=101
# if(100>age>=80):
#     print("he cannot vote")  
# elif(age<18):
#     print("he cannot vote")
# elif(80>age>18):
#     print("he can vote")
#     print("he can drive")   
# else:
#     print("invalide data")


# problem
# marks=float(input("enter your marks: "))
# if(marks>=90):
#     print("grade A")
# elif(marks>=80):
#     print("grade b")
# elif(marks>=70):
#     print("grade c")
# elif(marks>=60):
#     print("grade d")
# elif(marks>=40):
#     print("grade pass")
# else:
#     print("fail")

# 2.wap to check if the number is even or odd
# a=int(input("enter the number"))
# if(a%2==0):
#     print("the number is even")
# else:
#     print("the number is old")

# 3.wap to find the largest number of 4 number entered by  user 
