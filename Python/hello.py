# # print("hello world")
# # a="hello" 
# # num = 10
# # @= 4
# # 2=2
# # age =22
# # age =23
# # print("age")
# # print("age")
# # Break =22
# # print =22
# # print(print)

# name = "Piyush"
# print(name)
# print("name dtyoes:-",type(name))
# print("len of name:-",len(name))

# ### indexing
# print(name[0])
# print(name[2])
# print(name[len(name)-1])

##slicing in python

# name = "piyush"
# print(name[0:3])


# home work 

### operation
# name ="piyush"
# last = "kumar"

# upper case = name ,upper()  ### uper function ka use upper case ke liye kerte h

# print(upper_case)
# lower_last_name=last.lower()
# print(lower_last_name)

# print(name.count("p"))

# name="Piyush"
# last="kumar"
# print(name,title())
# print(name.capitalline())
# print(name+" "+last)


# list>>>

# list =
# list =[1,2,3,4,5,6,7,"rohit",2.3,]#### >>>>>list
# array or list>>>>>>>
# mutable
# duplicate values
# ##hearto
# order
# array>>>>   list =[1,2,3,4,5,6]
# #  array
# print("my first list:-",lst)
# print("len of list:-",len(lst))
# print("type of list:-",type(lst))
# list =[1,2,3,4,5]
# print(list)
# print(list[0])
# print(list[5])

# print(list[0:5])
# lst = [1,2,3,4,5,6,7,2.3,]
# lst.pop()
# print(lst)
# lst.append(100)
# print(lst)
# lst.insert(0,1000)
# print(lst)
# copy_lstb=lst.copy()
# print(copy_lst)
# lst.reverse()
# lst.remove(2.3)
# print(lst)
# lst.sort()
# lst=[1,2,3,4,5,6,7, 2.3,] #####>>>>>>>>list

# print(lst.count(2))
# print(lst)
 # home work banana ha list ka   



# >>>>>>>>>>>>>tuple<<<<<<<<<<<<<<<<

# tuple=
# a=1,2,58,5,5,85,2
# print(a)
# print(type(a)) ##<class'tuple'>
# print(len(a)) 


# >>>>>>>>>>>>>dict<<<<<<<<<<<<<<<<

# my_dict ={
#   "name":"rohit",
#   "class":"2nd year",
#   "roll no.":"21EAWCSE055",
#    "Adress":"jaipur","name":"rohit"


# }
# print("my first dict:-",my_dict)
# print("len of dict :-",len(my_dict))
# print("type of dict:-",type(my_dict))
# print(my_dict['name'])
# print(my_dict['class'])
# print(my_dict['roll no.'])
# print(my_dict['adress'])



# my_dict ={
#   "name":"rohit",  ####name,class,roll number and address >>>>keys

#   "class":"2nd year",#### rohit,2nd year ,21EAWCSE055 and jaipur >>>values

#   "roll no.":"21EAWCSE055",
#    "Adress":"jaipur","name":"rohit" ###>>>"name":"Rohit"item
# }

# my_dict['branch']="Cse"
# print(my_dict)


# access element 6

# lst = [1,2,3,4,[6],7]
# print("full lst:-",lst)
# nested = lst[4]
# print("nested lst:-",nested)
# six = nested[0]
# print("access element:-",six)



# my_dict ={
#   "name":"rohit",  ####name,class,roll number and address >>>>keys

#   "class":"2nd year",#### rohit,2nd year ,21EAWCSE055 and jaipur >>>values

#   "roll no.":"21EAWCSE055",
#    "Adress":"jaipur","name":"rohit" ###>>>"name":"Rohit"item
# }

# my_dict['branch']="Cse"
# print(my_dict)


# task1 >>>>>>>>update function
# get function >>>>>5 example minimum or []   

# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())


# copy_dict


# my_dict.clear()
# print(my_dict)

# a = input("enter a number")
# b= input("enter second number")
# print(a*b)
# print(type(a))
# print(type(b))

# type casting
# a = input("enter a number")
# b= input("enter second number")
# print(a*b)

# list =[1,2,6,8,5,58]
# print("this is my list:-",list)
# print("type of list:-",type(list))
# tpl =tuple(list)
# print("this is my tuple:-",tpl)
# print("type of tuple:-",type(tpl))



# >>>>>>>>>>>>>>>>>>>>Set <<<<<<<<<<<<

# my_set ={1,2,3,5,41,6,1,5,"jai"}
# print("this is my set:-",my_set)
# print("len of my set:-",len(my_set))
# print("type of set:-",type(my_set))

# task>>>>>
# my_set.union()
# my_set.intersection()
# my_set.difference()

# lst = list(my_set)

# lst.append(1000)
# print(set(lst))


####  Operator

#1
# student_scores = {"Alice": 95, "Bob": 88, "Charlie": 72}
# score_alice = student_scores.get("Alice")
# print(f"Alice's score: {score_alice}")


# 2

# student_scores = {"Alice": 95, "Bob": 88, "Charlie": 72}
# score_dave = student_scores.get("Dave")
# print(f"Dave's score: {score_dave}")

#3
# student_scores = {"Alice": 95, "Bob": 88, "Charlie": 72}
# score_eve = student_scores.get("Eve", 0)
# print(f"Eve's score: {score_eve}") # Output will be 0

#4
# config = {"debug_mode": True, "port": 8080}
# is_logging_enabled = config.get("enable_logging", False)
# print(f"Logging enabled: {is_logging_enabled}")

#5
# data = {
#         "user_info": {
#             "name": "Piyush",
#             "contact": {"email": "piyu@example.com"}
#         }
#     }
# user_email = data.get("user_info", {}).get("contact", {}).get("email")
# print(f"User email: {user_email}")


