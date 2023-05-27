#list = [1,2,3,'str',False]
#print(list[-3])
#TUPLE{
#t = (1,2,3)
# #for loop
# list = [1,2,3,4,5]
 
#  fot i in list:
#     print(i)
#odd even count
# list = [2,5,6,7,6]
# oddCount = 0
# evenCount = 0
# for i in list:
#     if i% 2 == 0:
#         evenCount +=1
#     else:
#         oddCount +=1 
#print('even',evenCount, 'odd',oddCount)

# for i in range(0,6):
#     print(i)
# for j in range(-3,13,3):
#     print(j)
# print all the numbers between 1 to 100 
# that are divisible by 7 but not 10

# for i in range(0,101):
#     if (i % 7 == 0) and (i % 10!=0): 
#         print(i)
# for i in range(0,3001):
#         print('i am sorry',i)
#String
        # name = "nagarjuna"

        # print(name[0])
        # print(name[-1])
        # print(name[:])
        # print(name[2:-1])
        # print(name[3:])
        # print(name[:2])
# #Function
# def check(a):
#         print('check fxn',a)
#         return 4
# result = check(2)
# print(result)


#wap that takes a number as parameter and prints wheather it is odd or even.
# def checkOddEven(num):
#         if num%2==0:
#                 print("Given no is even")
#         else:
#                 print("Odd ")

# result = checkOddEven(5)

#WA function that takes a number as parameter and checks it is between 0-100
#or not.Return valid if it lies else return invalid
# def Validity(num):
#         if num >=0 and num <=100:
#                 return'Invaild'
#         else:
#                 return'Valid'
      
# result = Validity(123)
# print(result)
# def fxn(a,b):
#     print(a,b)
#     return 3

#fxn call
# retValue = fxn(3,4)
# print('return',retValue)

#wap a function that inputs a number and print whether it is less than 500 or not

# def check(a):
#     if a < 500: 
#         print('The number is greater than 500')
#     else:
#         print('Greater than')

#Write a function that inputs an array and prints positive and negative numbers count

# marks = [40,12,32,22,16,17]
# passCount = 0
# failCount = 0

# for i in marks:
#     if i >= 32:
#         passCount+=1
#     else:
#         failCount+=1
#         print("pass Count",passCount)
#         print("fail Count",failCount)

def Checkgreater(a,b):
    if a>b:
        print(a,"is greater than ",b)
    else:
        print(b,"is greater than ",a)
         




