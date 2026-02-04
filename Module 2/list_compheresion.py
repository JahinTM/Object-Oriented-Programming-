numbers = [45,26,61,14,43,63]
odd =[]
for num in numbers :
    if num % 2 !=0 and num % 5==0:
        odd.append(num)
print(odd)
