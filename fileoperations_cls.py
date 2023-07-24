# fileoperations: Different operation that we can perform it on files..
# 

# Opening the file 
# 
# we have 2 syntaxies for opening the file...
# 
    # 1) open()
    # 2) with open()



# mode : its nothing but how i have to open the file.. 
    # read - r
    # write - w
    # append - a
# 1st syntax:
# open(path of the file,mode)

# open('C:\Users\DC\Desktop\Azure DevOps-Digital-Lync-Brochure.pdf') # we have to give the complete path when the file which i want to open and python file which i am execute are in different folder.. 

# file_object = open('dialogues.txt','r')

# print(file_object)

# print(file_object.closed) # checking whwtehr the file is closed.

# file_object.close() # TO close the file which is opened. 

# print(file_object.closed) # checking whwtehr the file is closed.

# 2nd Syntax:

# with open(path of file,mode) as object:
#     statements

# with open('dialogues.txt','r') as file_object:
#     print(file_object)


# print(file_object.closed)

# reading : 
    # read() - It will read the compelte content from the file on character by character basis. 
    # readline() - It will read one line of content at a time.. 
    # readlines() - It will read complete content by line by line basis which return as a list, where each element is a line inside the file. 

# with open('dialogues.txt','r') as file_object:
#     # read_data = file_object.read()
#     # for ele in read_data:
#         # print(ele)
#     # readline_data = file_object.readline()
#     # print(readline_data)
#     # print(file_object.readline())

#     readlines_data = file_object.readlines()
#     print(readlines_data[3])
#     print(readlines_data[1:4])

# Writing: It will overwrite the previous content and will write only the current content. 
    # write() - It is used for write the content into the file which will take a single string as an input..
    # writelines() - It is used for write the content into the file which will take list of elements as the input. 

# with open('dialogues_write.txt','w') as file_object:
#     file_object.write('Mokka kada ani peekestha peeka kostha.\nAnchana veyyadanike nuvvu emi polavaram dam aa patta seema tuma, pilla kaluva.\n')
#     # file_object.writelines(['Anchana veyyadanike nuvvu emi polavaram dam aa patta seema tuma, pilla kaluva.\n', 'Sound cheyyaku kantam kosestha\n', 'Medical test cheyyinchukodanike nee asthu ammukunna saripov.'])


# Appending: 
    # write() - It is used for write the content into the file which will take a single string as an input..
    # writelines() - It is used for write the content into the file which will take list of elements as the input. 

# with open('dialogues_append.txt','a') as file_object:
#     file_object.write('Mokka kada ani peekestha peeka kostha.\nAnchana veyyadanike nuvvu emi polavaram dam aa patta seema tuma, pilla kaluva.\n')
#     file_object.writelines(['Anchana veyyadanike nuvvu emi polavaram dam aa patta seema tuma, pilla kaluva.\n', 'Sound cheyyaku kantam kosestha\n', 'Medical test cheyyinchukodanike nee asthu ammukunna saripov.'])


# csv file:

# CSV - Comma Seperated Values

# import csv

# with open('student_info.csv','r') as file_object:
#     csv_data = csv.reader(file_object) # this will return an csv object.. 
#     # print(csv_data)
#     next(csv_data) # This will skip one line of content based on the cursor location.
