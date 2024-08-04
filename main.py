# age = input('vozrast: ')
# print(age)
#
# age = int(input('vozrast: '))
# if age < 18:
#     print('jashynyz 18den kichine')
# elif age == 18:
#     print()
# else:
#     print('jashynyz 18den chon')
#
# number_one = int(input('1 san: '))
# number_two = int(input('2 san: '))
# znak = input('tandoo (+, -, *, /): ')
#
#
# if znak == '+':
#     print(number_one + number_two)
# elif znak == '-':
#     print(number_one - number_two)
# elif znak == '*':
#     print(number_one * number_two)
# elif znak == '/':
#     print(number_one / number_two)
# else:
#     print('Error')
#
# num1 = int(input('number1:'))
# num2 = int(input('mumber2:'))
# item = input('choose one: (+, -, /, *):')
#
# if item == '+':
#     print(num1 + num2)
# elif item == '-':
#     print(num1 - num2)
# elif item == '*':
#     print(num1 * num2)
# elif item == '/':
#     print(num1 / num2)
# else:
#     print('error')
#

'''
write a name: Marlen
6

write a name: Asan
4
'''


# name = len(input('write a name:'))
# print(name)


'''
write a name: AsAn
'''
# name = input('write a name:')
# print(name.lower())


# number = int(input('san jaz:'))
#
# if number < 0:
#     print('minus san')
# elif number > 0:
#     print('plus san')
# elif number == 0:
#     print('barabar')
# else:
#     print('error')


# name = input('where are you from:')
#
# if name == 'kyrgyzstan'.lower():
#     print('salam')
# elif name == 'russian'.lower():
#     print('privet')
# elif name == 'usa'.lower:
#     print('hello')
# else:
#     print('error')


# number = int(input('Сан жаз: '))
#
# if number % 2 == 0:
#     print('Жуп сан')
# else:
#     print('Так сан')


# names = input ('names: ').lower()
# print(names.split())


# num1 = int(input('1 san : '))
# num2 = int(input('2 san: '))
#
# if num1 > num2:
#     print(num1)
# elif num2 > num1:#
#     print(num2)
# elif num1 == num2:
#     print('barabar')


# name = input('atyndy jaz: ')
# age = int(input('jashyndy jaz: '))
# person = []
# person.append(name)
# person.append(age)
# print(person)

# empty_list = []
# fruits = ['apple', 'banana', 'cherry', 'date']
# fruits.append('strawberry')
# print(fruits)

# my_list = [1, 2, 3]
# my_list.remove(3)
# print(my_list)



'''
name of car: audi
['tesla', 'bmw', 'byd', ]

name of car: tesla
['audi', 'bmw', 'byd', ]

name of car: porsche
Jok

'''



# cars = ['tesla', 'audi', 'bmw', 'byd', ]
# car_name = input('name of car: ')
#
# if car_name in cars:
#     cars.remove(car_name)
#     print(cars)
# else:
#     print('jok')






'''
name: ata   ata == ata
palindrom

name: kazak   kazak == kazak
palindrom

name: baike   baike == ekiab
palindrom emes

'''

# word = input('name: ')
#
# if word == word[::-1]:
#     print('palindrom')
# else:
#     print('palindrom emes')


# fruits = ['cherry', 'apple', 'apple', 'blueberry', 'banana', 'cherry' ,'apple']
# word = input('name: ')
#
# if word in fruits :
#     print(fruits.count(word))
# else:
#     print('JOK')



# numbers_one = [5, 9, 1]
# numbers_two = [8, 4, 6]
#
# word_list = numbers_one + numbers_two
# word_list.sort(reverse=True)
# print(word_list)


# fruits = ['cherry', 'blueberry', 'banana', 'apple']
#
# name = input('name of fruit:')
# if name in fruits:
#     print(fruits.index(name))
# else:
#     print('jok')


# numbers = [7,7,5,89,5,54,5]
#
# print(f'max: {max(numbers)} ')


# numbers = [66, 44, 10, 60, 70, 100]
#
# total = sum(numbers) / len(numbers)
#
# print(f'орточо баасы: {round(total, 2)} сом')



# name = input('words:').split()
# print(len(name[-1]))



'''
TUPLE , neizmenyaemiy
'''
# окшош сандардын саны 3

# numbers_one = (6, 8, 4, 3, 9)
# numbers_two = (8, 0, 13, 3, 6)
#
# name = set(numbers_one)
# name2 = set(numbers_two)
# intersection_set = name.intersection(name2)
# print(set(intersection_set))  #1


# numbers_one = (6, 8, 4, 3, 9)
# numbers_two = (8, 0, 13, 3, 7)
#
# total = set(numbers_one).intersection(numbers_two)
#
# print(f'окшош сандардын саны {len(total)}')    #2



# nums1 = [5, 7, 2, 4]
# nums2 = [0, 5, 2, 6]
#
# name_union = set(nums1).union(nums2)
# print (sorted(list(name_union), reverse=True))


# [7, 6, 5, 4, 2, 0]





# student = {'first_name': 'Aktan', 'last_name': 'Kubarbekov', 'age': 44}
#
# name = student['first_name']
# print(f'write a key: {name}')
#
# '''
# write a key: age
# 44
#
# write a key: aGe
# 44
#
# write a key: first_name
# Aktan
#
# write a key: name
# error
#
# '''

# student = {'first_name': 'Aktan', 'last_name': 'Kubarbekov', 'age': 44}
# keyword = input('write a key').lower()
# if keyword in student:
#     print(student[keyword])
#
# else:
#     print('error')



# fruits = ['apple', 'cherry', 'banana', 'strawberry']
#
# for name in fruits:
#     print(name.upper())

# for i in reversed()

# word = 'hello world'
# for i in range(10000):
#     print(word)


# for i in range(1,1001):
#     print(i)


# numbers = [6, 7, 8, 2, 5]
#
# for i in numbers:
#     print(i*2)


# numbers = [-6, 7 -8, 2, -5]
# new_list = []
#
# for n in numbers:
#     if n < 0:
#         new_list.append(n)
# print(new_list)


# numbers = [6, 7, 9, 8]
# total = 0
#
# for number in numbers:
#     total += number
#
# print(f'summa: {total}')


# word = input('word:')
# if word == word[::-1]:
#     print('palindrom')
# else:
#     print('palindrom emes')   #1



# name = [4, 6, 8, 5, 4, 5, 4, 5]
#
# name = set(name)
# print(sorted(list(name)))     #2



# number = int(input('number:'))
#
# if number % 2 == 0:
#     print('jup san')
# else:
#     print('tak san')    #3


# numbers = [7, 8, 34, 2, 98, 12]
# max_num = 0
# for num in numbers:
#     if num > max_num:
#         max_num = num
# print(f'max number is: {max_num}')



# number = int(input('number:'))
#
# for i in range( 1, 11):
#     print( f'{i} * {number} = {i * number}')


# count = 0
#
# while count < 5:
#     count += 1
#     print(count)


# while True:
#     number1 = int(input('1 san: '))
#     number2 = int(input('2 san: '))
#     znak = input('+ * - /: ')
#
#     if znak == '+':
#         print(number1 + number2)
#     elif znak == '-':
#         print(number1 - number2)
#     elif znak == 'k':
#         break



#
# '''
# write a number: 10
# Start
# 10
# 9
# 8
# ...
# 0
# The End
#
# '''




# name = int(input('write a  num:'))
#
# n = 1
# while n < name+1:
#     print('hello')
#     n+=1

#
# count = 10
# while count >= 0:
#     print(count)
#     count = count - 1


# a = input('parol:')
# password = 'qwerty'
# while a != password:
#     print('nepravilniy parol')
#     a = input()


# number = int(input('number:'))
# count = 10
# while count >= 0:
#     print(count)
#     count -= 1


# number = int(input('number:'))
# print('Start')
#
# while number >= 0:
#     print(number)
#     number -= 1
# print('The end')


# numbers = [6, 4, 78, -4, -7, 2]
#
# new_list = []
# for i in numbers:
#     if i > 0:
#         new_list.append(i)
# print(new_list)



# number_one = int(input('1 san: '))
# number_two = int(input('2 san: '))
#
# total = 0
# for i in range(number_one, number_two + 1):
#     total += i
# print(f'summa = {total}')



# number_one = int(input('1 san: '))
# number_two = int(input('2 san: '))
#
# total = 0
# for i in range(number_one, number_two + 1):
#     total += i
# print(f'summa = {total}')



# summa = 0
# while True:
#     number = int(input('number: '))
#     summa += number
#
#     if number == 0:
#         print(f'summa is {summa}')
#         break



# import random
#
# print(random.randint(5, 10))





# Томонку диапазон:10
# Жогорку диапазон:100
# 10 жана 100 ортосундагы санды табыныз:50
# Сиз жазган сан чон
# 10 жана 100 ортосундагы санды табыныз:15
# Сиз жазган сан кичине
# 10 жана 100 ортосундагы санды табыныз:40
# Сиз жазган сан кичине
# 10 жана 100 ортосундагы санды табыныз:48
# Куттуктайбыз сиз 48 санын 5 иретте таптыныз




# import random
#
# number1 = int(input('Томонку диапазон:'))
# number2 = int(input('Жогорку диапазон:'))
#
# secret_number = random.randint(number1, number2)
# col = 1
#
# while True:
#     numbers = int(input(f'{number1} жана {number2} ортосундагы санды табыныз:'))
#     col += 1
#
#     if numbers > secret_number:
#         print('Сиз жазган сан чон')
#     elif numbers < secret_number:
#         print('Сиз жазган сан кичине')
#     else:
#         print(f'Куттуктайбыз сиз {numbers} санын {col} иретте таптыныз')
#         break




# def new_numbers(num1, num2):
#     numbers = num1 + num2
#     numbers.sort(reverse=True)
#     return numbers
#
#
# print(new_numbers([6, 4, 8], [8, 3, 1]))


# def check_index(name):
#     fruits = ['cherry', 'blueberry', 'banana', 'apple']
#
#     if name in fruits:
#         return fruits.index(name)
#     else:
#         return 'Jok'
#
# name = input('name of fruit: ')
# print(check_index(name))


# def check_word(word):
#     if word == word[::-1]:
#         return 'Palindrom'
#     else:
#         return 'Palindrom emes'
#
# word = input('name: ')
# print(check_word(word))

'''
domashka but zadaniyany def menen jazuu
'''


# def numbers(a, b):
#     total = set(a).intersection(b)
#     return f'окшош сандардын саны {len(total)}'
#
#
# print(numbers((6, 8, 4, 3, 9, 0), (8, 0, 13, 3, 7)))
# 
#



def find_largest():
    numbers = [3, 8, 1, 6, 4, 2]
    max(numbers)

print(find_largest())



# def numbers (number):
#     if number % 2 != 0:
#         return('t')
#     else:
#         return('j')
# number = int(input('number:'))
# print(numbers(number))



# def check_list(name):
#     fruits = ['cherry', 'blueberry', 'banana', 'apple']
#
#     name = input('name of fruit: ')
#
#     if name in fruits:
#         return fruits.index(name)
#     else:
#         return 'Jok'
# print(check_list(name))




# persons = {'name': 'aidana', 'country': 'kg', 'age': 22}
#
# def check_key(word):
#     if word in persons:
#         return persons[word]
#     else:
#         return 'jok'
#
# key_word = input('write a key: ').lower()
# print(check_key(key_word))



# check_number = lambda a: print('+ san') if a > 0 else print('- san')
#
# check_number(55)



# number = int(input('write a number: '))
#
# def counter(number):
#     print('Start')
#     while number != -1:
#         print(number)
#         number -= 1
#
#     print('The end')
#
# counter(number)



#1




# def calculator (num1, num2, znak)
#     if znak == '+':
#         return num1 + num2
#     elif znak == '-':
#         return num1 - num2
#     elif znak == '*':
#         return num1 * num2
#     else:
#         return num1 / num2
# num1 = int(input('number1:'))
# num2 = int(input('number2:'))
# znak = input('znak : +, -, /, *')
#
# print(calculator(num1 , num2, znak))



# numbers = [7, 8, 34, 2, 98, 12]
# max_number = numbers[0]
#
# def counter (max_number):
#
#     for i in numbers[1:]:
#         if i > max_number:
#             max_number = i
# print(counter(max_number))


# w = input('word: ')
# number = int(input('number: '))
#
# def check_word(w, number):
#     for i in range(number):
#         print(w)
# print(check_word(w, number))

# def find_max(numbers):
#     max_number = numbers[0]
#     for i in numbers[1:]:
#         if i > max_number:
#             max_number = i
#     return max_number
#
# numbers = [7, 8, 34, 2, 98, 12]
# max_number = find_max(numbers)
# print(f'max number is {max_number}')





# def find_largest(numbers):
#     return max(numbers)
#
# numbers = [3, 8, 1, 6, 4, 2]
# print(find_largest(numbers))



# def common_elements(list1, list2):
#     return list(set(list1) & set(list2))
#
# list1 = [1, 2, 3]
# list2 = [3, 4, 5]
#
# print(common_elements(list1, list2))



def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

word = input('word: ')
print(is_palindrome(word))



# number_one = int(input('1 san: '))
# number_two = int(input('2 san: '))
# total = 0
#
# def check_num (number_one, number_two, total):
#     for i in range(number_one, number_two + 1):
#         total += i
#         print(f'summa = {total}')
#
#
# check_num(number_one, number_two)



# class Car:
#     def __init__(self, name, price, country):
#         self.name = name
#         self.price = price
#         self.country = country
#
#     def get_info(self):
#         return f'Name {self.name}, price is {self.price}, country {self.country}'
#
#
# car1 = Car('Honda', 34545, 'KG')
# car2 = Car('BMW', 54645, 'KG')
# car3 = Car('MERS', 34325, 'USA')
#
# print(car1.get_info())



# class Product:
#     def __init__(self, product_name, description, price):
#         self.product_name = product_name
#         self.description = description
#         self.price = price
#
#     def get_info(self):
#         return f'product_name: {self.product_name}, description: {self.description}, price: {self.price}'
#
#
# product1 = Product('macbook', 'laptop', '1000$')
# product2 = Product('iphone', 'telephone', '1000$')
#
# print(product1.get_info())




# class Computer:
#     def __init__(self, computer_name, description, price, model):
#         self.computer_name = computer_name
#         self.description = description
#         self.price = price
#         self.model = model
#
#     def get_info(self):
#         return f'product_name: {self.computer_name}, description: {self.description}, price: {self.price}, model: {self.model}'
#
#
# computer1 = Computer('macbook', 'laptop', '1000$', 'm3')
# computer2 = Computer('Acer', 'laptop', '1000$', 'm3')
# computer3 = Computer('Dell', 'laptop', '1000$', 'm3')
#
# print(computer1.get_info())
# print(computer2.get_info())
# print(computer3.get_info())



# class Animal:
#     def __init__(self, name ):
#         self.name = name
#
#     def get_info(self):
#         return f'name:{self.name}'
#
# animal = Animal('dog')
# print(animal.get_info())
#
#
# class Dog(Animal):
#     def __init__(self , name, sound):
#         super(). __init__(name)
#         self.sound = sound
#
#     def get_info(self):
#         return f'name:, {self.name}, sound: '




# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def sound(self):
#         pass
#
# class Dog(Animal):
#     def sound(self):
#         return 'gaf gaf'
#
# dog1 = Dog('Rex')
# print(dog1.sound())#gaf gaf


# class Cat(Animal):
#     def __init__(self, name, color):
#         super().__init__(name)
#         self.color = color
# #
#     def sound(self):
#         return 'miay miay'
#
# cat1 = Cat('Felix', 'Brown')
# print(cat1.sound())#miay miay