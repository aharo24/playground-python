                # RETURN     
# def mult(num1,num2):
#     res = num1*num2
#     return res


# # print(mult(2,3))
# x = mult(2,3)
# print(x)

# ---- ----
# def mult(num1,num2):
#     return num1 * num2

# print(mult(2,2))

                # KEYWORD ARGS
# def hello(first,middle,last):
#     print("Hello " + first + " " + middle + " " + last)

# #hello("Angel","J","Haro")
# hello(last="Angel",first="Haro",middle="J")

                # NESTED FUNCTION CALLS
# # num = input (" Enter a whole positive number : ")
# # num = float(num)
# # num = abs(num)
# # num = round(num)
# # print(num)
#         # SAME AS ABOVE
# print(round(abs(float(num = input (" Enter a whole positive number : ")))))


                # VARIABLE SCOPE

# name = "Yare"       # gloval scope
# def display_name():
#     name = "Angel"   # local scope
#     print(name)     # only inside func


# display_name()
# print(name)


                # *ARGS --> TUPLE
# def add(*stuff): # common conventaion *args 
#     sum = 0
#     # stuff[0] = 24 # dont work
#     stuff = list(stuff)
#     stuff[0] = 0
#     for i in stuff:
#         sum += i
#     return sum

# print(add(10,2,3))

                # **KWARGS --> HASHMAPS
# def hello(**dic):
#     #print("Hello " + kwargs['first'] + " " + kwargs['last'])
#     print("Hello", end=" ")
#     for key,val in dic.items():
#         print(val, end=" ")

# hello(tres="Angel",quang="Haro",middle="J")

                # STR.FORMAT() --> str.format() <--> System.out.printf()
# animal = "cow"
# item = "moon"
# #print ("The " + animal + " jumped over the " + item)
# # print("The {} jumved over the {}".format(animal,item) , end="\n")
# # print("The {1} jumved over the {0}".format(animal,item) , end="\n") #positional arg
# # print("The {animal_keyword} jumved over the {item_keyword}".format(animal_keyword="frog",item_keyword="lake") , end="\n") # keyword arg

# # text = "The {} jumped over the {}"
# # print(text.format(animal,item))

# name = "aharo"
# print("Hello, my name is {}".format(name))
# print("Hello, my name is {:<10}. Nice to meet you".format(name))
# print("Hello, my name is {:>10}. Nice to meet you".format(name))
# print("Hello, my name is {:^10}. Nice to meet you".format(name))

# first_name = "Angel"
# last_name = "Haro"
# full_name = "\nHi my first name is {} and last name is {}, nice to meet you ".format(first_name,last_name)
# print(full_name)

#numer = 3.14159




number = 1000
print("The number pi is {:.3f}".format(number))
print("The number pi is {:,}".format(number))
print("The number pi is {:b}".format(number))  # binary
print("The number pi is {:o}".format(number))  # octol
print("The number pi is {:x}".format(number))  # hexa/Hexa
print("The number pi is {:E}".format(number))  # scientific notation


print("Hello Angel")