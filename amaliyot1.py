# -*- coding: utf-8 -*-
"""
Created on Sat Aug 23 20:58:24 2025

@author: smann
"""


"""Daraja 1 — Juft/Yoq

Kirish: bitta butun son n.

Vazifa: n juft bo‘lsa "Juft", aks holda "Toq" chiqarish.

Misol: Input: 8 → Output: Juft"""

# n=int(input('Bitta butun n sonini kiriting: '))
# print(f"{n} soni juft") if n%2==0 else print(f"{n} soni toq")

"""Daraja 2 — Ro‘yxat yig‘indisi

Kirish: bitta qatorda bo‘shliq bilan ajratilgan sonlar.

Vazifa: ularning yig‘indisini toping.

Misol: "1 2 3 4" → 10"""

# sonlar=list(map(int, input("Sonlar ketma-ketligini kiriting: ").split()))
# yigindi=0
# for son in sonlar:
#     yigindi+=son
# print(sonlar)
# print(yigindi)

# # print("Yig‘indi:", sum(sonlar)) # optimal variant

"""Daraja 3 — Unli harflar soni

Kirish: satr s. (unlilar: a, e, i, o, u, A, E, I, O, U)

Vazifa: s ichidagi unlilar sonini chiqaring.

Misol: "Salom" → 2"""

# satr=input("Satrni kiriting: ")
# unlilar=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
# sanash=0
# for harf in satr:
#     if harf in unlilar:
#         sanash+=1
# print(f"{satr} >>> {sanash}")

# Optimal variant

# s = input("Matn kiriting: ")
# unlilar = "aeiouAEIOU"
# hisob = sum(1 for belgi in s if belgi in unlilar)
# print("Unli harflar soni:", hisob)

'''Daraja 4 — Ikki eng katta

Kirish: n va keyin n ta butun son.

Vazifa: ro‘yxatdagi eng katta va ikkinchi eng katta qiymatni tartibda chiqaring.

Cheklov: kamida 2 ta element bor.

Misol: [3, 9, 9, 1] → "9 9"'''

# sonlar=list(map(int, (input("Butun sonlarni kiriting: ").split())))
# big1=max(sonlar)
# sonlar.remove(big1)
# big2=max(sonlar)
# print(big1, big2)

# optimal variant

# n = int(input("Nechta son kiritasiz: "))
# sonlar = list(map(int, input("Sonlarni kiriting: ").split()))

# sonlar.sort(reverse=True)
# print("Eng katta:", sonlar[0], "Ikkinchi eng katta:", sonlar[1])

'''Daraja 5 — Tub tekshirish va keyingi tub

Kirish: butun n (n ≥ 2).

Vazifa: n tub bo‘lsa "YES", aks holda "NO" va n dan katta eng yaqin tubni ham chiqarish.

Misol: 10 → "NO 11"; 13 → "YES"'''

# n= int(input("2 dan katta butun son kiriting: "))
# sanovchi=0
# if n>=2:
#     for i in range(n//2+1):
#         if i!=0 and i!=1 and i!=n:
#             if n%(i)==0:
#                 print(f"{n} soni {i} ga bo'linadi")
#                 sanovchi+=1    
#     if sanovchi==0:
#         print(f'Kiritilgan son {n} tub son')
#     else:
#         print(f'Kiritilgan son {n} tub son emas')
# else:
#     print('Kiritilgan son 2 dan katta yoki teng bo\'lsin')

# Optimal variant
# def tubmi(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True

# n = int(input("Son kiriting: "))

# if tubmi(n):
#     print("YES")
# else:
#     m = n + 1
#     while not tubmi(m):
#         m += 1
#     print("NO", m)
    
        