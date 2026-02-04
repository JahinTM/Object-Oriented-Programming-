def full_name(first,last):
    name = f'{first} {list}'
    return name

name = full_name('alu','balo')
print(name)

name = full_name(last='tajowar',first='Jehin')
print(name)

# def famous_name(fast,last,title, *address):
#     name =f'{fast} {last} {title} {address}'
#     return name

# name = famous_name(fast='ali', last='baba',title='jin') #address='12/2')

# print(name) 



def cal(num1,num2):
    sum = num1 + num2
    mul = num1 * num2
    sub = num1 - num2
    return sum,sub,mul

jehin = cal(20,10)
print(jehin)
