# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 3

# a = int(input('Nechta Son Kiritmoqchisiz: '))
# l = []
# for i in range(1, a+1):
#     def son(*args, **kwargs):
#         b = int(input('Son Kiriting: '))
#         if b<2:
#             return False
#         l.append(b)
#         return True
#     while not son():
#         print('2 yoki 2 dan katta son kiriting')

# tuliq = 0
# quwiw = 0
# listt = []
# for s in l:
#     tub = True
#     for j in range(2, s):
#         if s % j == 0:
#             tub = False
#     if tub:
#         tuliq += 1
#         quwiw += s
#         listt.append(s)

# print(f"Tuliq List: {l}")

# print(f"Tub Sonlar Joylashtirilgan List: {listt}")

# print(f"Listdagi Nechta Son Tub: {tuliq}")

# print(f"Tub Sonlarning Yig'indisi: {quwiw}")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 4

# a = int(input('Nechta Son Kiritmoqchisiz: '))
# l = []
# for i in range(1, a+1):
#     def son(*args, **kwargs):
#         b = int(input('Son Kiriting: '))
#         if b<2:
#             return False
#         l.append(b)
#         return True
#     while not son():
#         print('2 yoki 2 dan katta son kiriting')

# tuliq = 0
# quwiw = 1
# listt = []
# for s in l:
#     tub = True
#     for j in range(2, s):
#         if s % j == 0:
#             tub = False
#     if tub:
#         tuliq += 1
#         quwiw *= s
#         listt.append(s)

# print(f"Tuliq List: {l}")

# print(f"Tub Sonlar Joylashtirilgan List: {listt}")

# print(f"Listdagi Nechta Son Tub: {tuliq}")

# print(f"Tub Sonlarning Ko'paytmasi: {quwiw}")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 5

# a = input('Menga Malumot Bering Va Men Sizga Nechta Katta Harf Va Nechta Kichkina Harf Borligini Aniqlab Beraman: ')

# l = []
# s = []

# for i in a:
#     if i.isupper():
#         l.append(i)
    
#     elif i.islower():
#         s.append(i)

# sum_l = 0
# sum_s = 0

# for i in l:
#     sum_l += 1

# for i in s:
#     sum_s += 1


# print(f"Kiritilgan So'z: {a}")

# print(f"Kiritilgan So'zdagi Katta Harflar: {l}")

# print(f"Kiritilgan So'zdagi Katta Harflar Soni: {sum_l}")

# print(f"Kiritilgan So'zdagi Kichkina Harflar: {s}")

# print(f"Kiritilgan So'zdagi Kichkina Harflar Soni: {sum_s}")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 6

# a = input('Menga Malumot Bering Va Men Sizga Nechta Katta Harf Va Nechta Kichkina Harf Borligini Aniqlab Beraman: ')

# d = a
# a = a.lower()

# l = []

# for i in a:
#     if i in ('a', 'e', 'i', 'o', 'u'):
#         l.append(i)

# sum_l = 0

# for i in l:
#     sum_l += 1

# print(f"Kiritilgan So'z: {d}")

# print(f"Kiritilgan So'zdagi Unli Harflar: {l}")

# print(f"Kiritilgan So'zdagi Unli Harflar Soni: {sum_l}")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 7

# a = input("So'z Kiriting: ")

# def son(*args, **kwargs):
#         b = int(input("Kiritilgan So'zdan Nechinchi Harfini O'chirmoqchisiz Kiriting: "))
#         if b>len(a):
#             return False
#         l = []
#         count = 0
#         for i in a:
#             count += 1
#             if b == count:
#                  o = i
#             else:
#                  l.append(i)
#         print(f"Kiritilgan So'z - {a}")
#         print(f"Kiritilgan So'zdan '{o}' - Harfi Olib Tashlandi")
#         f = ''
#         for x in l:
#              f += x
#         print(f"Qolgan So'z - {f}")
#         return b
# while not son():
#     print('Siz Kiritilgan So\'zning Uzunligidan Kattaroq Son Kirityapsiz!')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 8

# a = int(input('Nechta Gap Yozmoqchisiz: '))
# l = []
# for i in range(1, a+1):
#     def son(*args, **kwargs):
#         b = input('Gap Kiriting: ')
#         l.append(b)
#         return True
#     son()

# d = ''
# c = 0
# for x in l:
#     if c<len(x):
#         c = len(x)
#         d = x

# print(f"Tuliq List: {l}")

# print(f"Kiritilgan Gapning Uzunligi: {c}")

# print(f"Kiritilgan Eng Uzun Gap: {d}")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 