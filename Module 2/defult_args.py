# def sum(num1,num2, num3=0):
#     result = num1+ num2 +num3
#     return result

# total = sum(10,20)
# print(total)


# def all(*nums):  # tuple hye jabe star dile
#     print(nums)
# total = all(1,2,3,4,5)
# print(total)


# def all(*nums):  
#     # print(nums)
#     for i in nums:
#         print (i)
# total = all(1,2,3,4,5)
# print(total)


def all(num1, num2, *nums):  
    # print(nums)
    sum =0
    for i in nums:
        print (i)
        sum = sum + i
    return sum
total = all(1,2,3,4,5)
print(total)