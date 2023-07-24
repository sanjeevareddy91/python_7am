# # Operator: 

# # 1) Arthimetic Operators(+,-,*,/,//,%,**)
# # 2) Relational or comparison Operators(==,!=,>,<,>=,<=)
# # 3) Logical Operators(and,or,not)
# # 4) Assignment Operators(=,+=,-=,*=....)
# # 5) Membership Operators(in.not in)
# # 6) Identity Operators(is,is not)
# # 7) Bitwise Operators(BitwiseAND(&),BitwiseOR(|),BitwiseXOR(^),Left Shift (<<),RIght SHift(>>),bitwise Not(~))

# a=12
# b=42

# # print(a+b)

# # print(a-b)
# # print(a*b)



# 17/3 -  5.6667

# # 3)17(5.6667
# #   15
# # -----
# #    20
# #    18
# # ------
# #     2


# # 17//3 -- 5

# # 3)17(5.667
# #   15
# # ------
# #    20
# #    18
# # ------
# #     2

# # 17%3 -- 2

# # 3)17(5
# #   15
# # ------
# #    2


# # 178%3 -- 1

# # 3)178(59
# #   15
# # -----
# #    28
# #    27
# # ------
# #     1

# # print(17/3)
# # print(17//3)
# # print(17%3)
# # print(178%3)


# # print(2**4)

# # Relational or comparison operators(==,!=,>,<,>=,<=)- output for this operators will be boolean(True/False).

# # a=12
# # b=54

# email = "ramesh@gamil.com"
# email1 = "ramesh@gMail.com"

# # print(a == b)
# # print(a != b)
# # print(a > b)
# # print(a < b)
# # print(a <= b)
# # print(a >= b)


# # print(email == email1)
# # print(email != email1)
# # print(email > email1)
# # print(email < email1)
# # print(email <= email1)
# # print(email >= email1)

# # Comparsion between the string data will be performed based on ASCII values..


# # Logical Operators(and,or,not)

# # BODMAS -- 

# # A     B     A and B   A or B   not(A)  not(A and B)  not((A or B) and (A and B))
# # ----------------------------------------------------------------------------------
# # T     F        F        T        F          T                   T 
# # F     T        F        T        T          T                   T 
# # T     T        T        T        F          F                   F 
# # F     F        F        F        T          T                   T 

# a=12
# b=13

# # print(a ==14 and b < 15) # False


# # hero = "Balayya"
# # dialogue = "Dabidi Debidaaa"

# # print(hero == 'Balayya' and dialogue == "Dabidi Debidaaa")

# # print(hero == 'Chiru' and dialogue == "Dabidi Debidaaa")


# # print(hero == 'Balayya' or dialogue == "Dabidi Debidaaa")

# # print(hero == 'Chiru' or dialogue == "Dabidi Debidaaa")

# # Assignment Operators:

# # a = 14 # basic assignment operator..

# # print(a)
# # # a = a+2 # manually 

# # # print(a)
# # a += 2 # a = a+2
# # print(a)


# # Membership Operators(in,not in): Output for this will be boolean(True/False)

# message = "Python is best programming langauge for web development"

# search = "python"


# # print(search in message)

# # print('p' in message)

# # print(search not in message)

# # print('p' not in message)

# # emails = ["Ramesh@gmail.com",'suresh@gmail.com','mahesh@gamil.com']

# # print('ramesh@gmail.com' in emails)

# # print('ramesh@gmail.com' not in emails)

# # print('suresh' not in emails)

# # Identity Operators(is, is not) -- This will work based on the memory allocation of the values..

# # a=13
# # b=13

# # print(id(a))
# # print(id(b))


# # print(a is b)

# # print(a == b)

# # name = 'mahesh'
# # name1 = 'mahesh'

# # print(id(name))
# # print(id(name1))
# # print(name is name1)
# # print(name == name1)

# # tuple1 = (1,2,3,4)
# # tuple2 = (1,2,3,4)


# # print(id(tuple1))
# # print(id(tuple2))
# # print(tuple1 is tuple2)
# # print(tuple1 == tuple2)

# # list1 = [1,2,3,4]
# # list2 = [1,2,3,4]

# # print(id(list1))
# # print(id(list2))

# # print(list1 is list2)
# # print(list1 == list2)

# # dict1 = {'name':"mahesh","email":"mahesh@gmail.com"}

# # dict2 = {'name':"mahesh","email":"mahesh@gmail.com"}

# # print(dict1 is dict2)
# # print(dict1 == dict2)


# # Bitwise Operators:(Bitwise AND(&),Bitwise OR(|),Bitwise XOR(^),LEFT shift(<<),Right Shift(>>),Bitwise NOT(~))

# # A        B         A & B        A|B      A^B 
# # --------------------------------------------------------
# # 1        0          0            1        1
# # 0        1          0            1        1
# # 1        1          1            1        0
# # 0        0          0            0        0 


# a=14
# b=17

# # print(a&b)


# # a=23
# # b=32

# # print(a&b)


# # a=23
# # b=36

# # print(a&b)


# # print(bin(14))
# # print(bin(17))

# # 2) 14 (
# #     2) 7 -- 0
# #        2)3 -- 1
# #          1 -- 1

# # 2) 17 (
# #     2) 8 - 1
# #        2)4 - 0
# #          2)2 - 0
# #            1 - 0

# # 14 -- 01110
# # 17 -- 10001
# # ---------------
# #       00000 - 0
# #       11111 - 31
# #       11111 - 31
# # print(a|b)

# # print(int('11111',2))

# # 11111

# # 16,8,4,2,1

# # 101011
# # 32 16 8 4 2 1
# # 32+8+2+1 == 43

# # print(a^b)


# # Left Shift(<<)

# # 00001110 --> 00011100 --> 11100000

# # print(a<<4)

# # print(a<<5)

# # print(bin(448))

# # print(a>>1)

# # print(a>>2)

# # print(a>>3)

# # print(a>>4)

# a = 32

# print(~a)


# b=-34

# print(~b)