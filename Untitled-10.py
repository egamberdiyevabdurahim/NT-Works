from collections import defaultdict


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 1


# def son(*args, **kwargs):
#     b = input("So'z Kiriting: ")
#     while not b.isalpha():
#         print("Harflardan iborat bo'lishi kerak")
#         b = input("Qayta Kiriting: ")
#     lists.append(b)
#     return b


# lists = []

# a = int(input('Nechta So\'z Kiritmoqchisiz: '))

# to_list = [son() for value in range(1, a+1)]

# maker = filter(lambda x: True if 'a' in x.lower() else False, lists)

# maker2 = [string for string in lists if 'a' in string.lower()]

# print(f"First Way: {list(maker)}")

# print(f"Second Way: {maker2}")



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 2


# def son(*args, **kwargs):
#     b = input("So'z Kiriting: ")
#     while not b.isalpha():
#         print("Harflardan iborat bo'lishi kerak")
#         b = input("Qayta Kiriting: ")
#     lists.append(b)
#     return b


# def makerr(string: str):
#     return True if string[0] == string[-1] else False


# lists = []
# l2 = []

# a = int(input('Nechta So\'z Kiritmoqchisiz: '))

# to_list = [son() for value in range(1, a+1)]

# maker = [string for string in lists if string.lower()[0]==string.lower()[-1]]
# maker2 = filter(makerr, lists)

# l2.append(list(maker2))

# print(f"Tuliq List: {lists}")

# print(f"First Way: {l2[0]} sum of strings: {len(l2[0])}")

# print(f"Second Way: {maker} sum of strings: {len(maker)}")



# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 3


# def son(*args, **kwargs):
#     b = int(input("Son Kiriting: "))
#     lists.append(b)
#     return b


# def makerr(string: int):
#     return True if string>0 else False


# lists = []
# l2 = []

# a = int(input('Nechta Son Kiritmoqchisiz: '))

# to_list = [son() for value in range(1, a+1)]

# maker = [string for string in lists if string>0]
# maker2 = filter(makerr, lists)

# l2.append(list(maker2))

# print(f"Tuliq List: {lists}")

# print(f"First Way: {l2[0]} sum of musbats: {len(l2[0])}, sum of manfiys: {len(lists)-len(l2[0])}")

# print(f"Second Way: {maker} sum of musbats: {len(maker)}, sum of manfiys: {len(lists)-len(maker)}")



# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 4


# def son(*args, **kwargs):
#     b = input("So'z Kiriting: ")
#     lists.append(b)
#     return b


# def makerr(string: str):
#     return True if string.isalpha() else False


# lists = []
# l2 = []

# a = int(input('Nechta So\'z Kiritmoqchisiz: '))

# to_list = [son() for value in range(1, a+1)]

# maker = [string for string in lists if string.isalpha()]
# maker2 = filter(makerr, lists)

# l2.append(list(maker2))

# print(f"Tuliq List: {lists}")

# print(f"First Way: {l2[0]} sum of sentences: {len(l2[0])}, sum of mixed sentences: {len(lists)-len(l2[0])}")

# print(f"Second Way: {maker} sum of sentences: {len(maker)}, sum of mixed sentences: {len(lists)-len(maker)}")



# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 5


# def son(*args, **kwargs):
#     b = input("So'z Kiriting: ")
#     lists.append(b)
#     return b


# def maker(lis: list):
#     string = ''
#     for x in lis:
#         string += f"{x} "
#     return string.capitalize()


# lists = []
# l2 = []

# a = int(input('Nechta So\'z Kiritmoqchisiz: '))

# to_list = [son() for value in range(1, a+1)]


# print(f"Input: {lists}")

# print(f"Output: {maker(lists)}")



# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 6


# a = input("So'z Kiriting: ")

# b = a.split(' ')


# maker = [len(string) for string in b]
# maker2 = map(lambda x: len(x), b)


# print(f"Tuliq So'z: {a}")

# print(f"First Way: {maker}")

# print(f"Second Way: {list(maker2)}")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
##############################################
# BONUS #
##############################################
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 6.2


# def son(*args, **kwargs):
#     b = input("So'z Kiriting: ")
#     lists.append(b)
#     return b


# def makerr(string: str):
#     return True if string[::] == string[::-1] else False


# lists = []
# l2 = []

# a = int(input('Nechta So\'z Kiritmoqchisiz: '))

# to_list = [son() for value in range(1, a+1)]

# maker = [string for string in lists if string[::] == string[::-1]]
# maker2 = filter(makerr, lists)

# l2.append(list(maker2))

# print(f"Tuliq List: {lists}")

# print(f"First Way: {l2[0]} sum of palindrom sentences: {len(l2[0])}, sum of other sentences: {len(lists)-len(l2[0])}")

# print(f"Second Way: {maker} sum of palindrom sentences: {len(maker)}, sum of other sentences: {len(lists)-len(maker)}")



# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 7


# def son(*args, **kwargs):
#     b = input("Son Kiriting: ")
#     while not b.isdigit() or b <= '1':
#         print("Invalid Number or you entered 1")
#         b = input("Qayta Kiriting: ")
#     lists.append(int(b))
#     return b


# def makerr(string: int):
#     message = True
#     for i in range(2, string):
#         if string % i == 0:
#             message = False
#             break
#     return message


# lists = []
# l2 = []

# a = int(input('Nechta Son Kiritmoqchisiz: '))

# to_list = [son() for value in range(1, a+1)]

# maker = filter(makerr, lists)

# l2.append(list(maker))


# print(f"Tuliq List: {lists}")

# print(f"Tub Sonlar Ro'yxati: {l2[0]}, soni: {len(l2[0])}")
