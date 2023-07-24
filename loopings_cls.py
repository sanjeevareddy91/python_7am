# loopings or iterations: Executing certain set of statements multple no.of times

# while
# for loop

# While loop: Loop which will execute the statement based on the condition..

"""
while condition:
    statements
"""

# a = int(input("Enter a value:"))

# if a>30:
#     print(a,"is greatherthan 30")
# else:
#     print(a,"is lessthan 30")


# while a>30:
#     print(a,"is greatherthan 30")
#     a -= 1
# else:
#     print(a,"is lessthan 30")


# for loop:

# For loop will be performed only on sequences..

"""
for element in sequence:
    statements
"""

# str1 = "Python is the best programming language"

# for ele in str1:
#     print(ele)

# list1 = ['mahesh','naresh','suresh','subash']

# for ele in list1:
#     print(ele)

# range -- This will create a sequence from the number we have provided..

# range()

# range(43) -- it will consider from 0 to 42
# range(2,43) -- it will start from 2 and ends at 42

# range(2,43,2) -- 3rd argument can be called as offset or jump..

# print(tuple(range(2,43)))

# for ele in range(2,43):
#     print(ele)

# for ele in range(43):
#     print(ele)

# for ele in range(2,42,3): # [2,5,8,11,14,17,20,23,26,29,32,35,38,41]
#     print(ele)


# for ele in range(42,2,-1):
#     print(ele)

# control flow statements... -- Contorlling the flow of iteration..

# break -- It will stop all the iteration and will go outside of the loop..
# continue -- It will skip the current iteration and will go back to the next iteration directly..
# pass


# list1 = ['7383785433','6473637322','7763764743','83736447732','584733677','637463222']

# for ele in list1:
#     if ele[0] == '6':
#         print(ele)
#         # break
#         continue
#     print('conditions not satisfied')
# print("outside of loop")