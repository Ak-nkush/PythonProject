# adding only one element in a tuple
# what is the difference between (1) and (1,) in tuple

first_tuple = ()
print("First tuple : " , first_tuple)
print(type(first_tuple))

second_tuple = ("Mon","Tue","Wed")
print("Second tuple : ", second_tuple)
print(type(second_tuple))


third_tuple = (1,2,3,4)
print("Third tuple : ", third_tuple)
print(type(third_tuple))

# BUILT IN FUNCTION FOR TUPLE :
fourth_tuple = tuple(("fri","sat","sun"))
print("Fourth tuple : ", fourth_tuple)
print(type(fourth_tuple))

# NESTED TUPLE :
fifth_tuple = (second_tuple , fourth_tuple)
print("Fourth tuple : ", fifth_tuple)
print(type(fifth_tuple))

# TYPECASTING LIST INTO A TUPLE
my_list = [10,20,30]
sixth_tuple = tuple(my_list)
print("Sixth tuple : ", sixth_tuple)
print(type(sixth_tuple))

seventh_tuple = (40,)
# here we are restricting tuple to a single element soo it is a single element tuple
# is it possible to append elements in a seventh tuple
print("Seventh tuple : ", seventh_tuple)
print(type(seventh_tuple))

eight_tuple = (90)
# NOTE : there isn't comma at the end soo it might be a single element tuple or not
print("Eight tuple : ", eight_tuple)
print(type(eight_tuple))

ninth_tuple = tuple(range(1,11))
print("Ninth tuple : ", ninth_tuple)
print(type(ninth_tuple))

# to append in a tuple , it has to be converted into a list or have to be cancate two tuple
# patten of the exam - trace the output or complete a code
#  1st assessment = 50 marks and there will be 3 chances
# 25 mark - lab assingment for python