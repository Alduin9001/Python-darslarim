# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 22:18:51 2025

@author: smann
"""
''' Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang.
 Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating'''
 
# print('Yaxshi ko\'rgan kitoblaringizni kiriting: ' )
# savol='To\'xtatish uchun "stop" ni kiriting!'
# book= ''
# books=[]
# while book != 'stop':
#     book= input(savol)
#     if book!='stop':
#         books.append(book)
# print(f'Sevimli kitoblaringiz: {books} ')

''' Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 
7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 65 dan kattalarga bepul. Shunday while tsikl 
yozingki, dastur foydalanuvchi yoshini so'rasin va chipta narhini chiqarsin. Foydalanuvchi 
exit yoki quit deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).
Yuqoridagi dasturni turli usullarda yozib ko'ring (break, ishora, yoki shart tekshirish)'''

# greeting=('Xush kelibsiz!')
# savol='\n(Chiqish uchun "exit" yoki "quit" kalitini kiriting)'
# flag=True
# narx=0
# while flag:
#     print(greeting+savol)
#     yosh =(input('Iltimos, yoshingizni kiriting: '))
#     if yosh=='exit' or yosh =='quit':
#         flag=False
#     else: 
#         yosh=int(yosh)
#         if yosh<=7:
#             narx=2000
#         elif yosh>=7 and yosh<=18:
#             narx=3000
#         elif yosh>=18 and yosh <=65:
#             narx=10000
#         else:
#             narx=0
#         print(f'Chipta narxi {narx} so\'m')

''' Quyidagi dasturda bir nechta mantiqiy xatolar bor. 
Jumladan, xusisiy holatlarda tsikl abadiy qaytarilib qolmoqda. 
Xatolarni to'g'rilay olasizmi?'''

## Xato variant
# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat<0:
#         continue
#     elif qiymat=='Exit':
#         break
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")

## To'g'rilangan

# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat=='exit':
#         break
#     else: 
#         qiymat=float(qiymat)
#         if qiymat<0:
#             continue
#         else:
#             ildiz = float(qiymat)**(0.5)
#             print(f"{qiymat} ning ildizi {ildiz} ga teng")

''' Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini 
birma-bir qabul qilib, yangi ro'yxatga joylang. '''

# print('Buyurtmalarni qabul qilishga tayyormiz!')
# buyurtmalar=[]
# n=1
# while True:
#     buyurtma=input(f'{n}-buyurtmangizni kiriting: ')
#     buyurtmalar.append(buyurtma)
#     n+=1
#     shart=input('Yana buyurtma berishni xohlaysizmi? (ha/yo\'q)')
#     if shart!='ha':
#         break
# print("Buyurtmalaringiz ro'yxati:")
# print(buyurtmalar)

''' e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi 
dastur yozing. Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) 
kiritishni so'rang. '''

# mahsulotlar={}
# ishora=True
# while ishora:
#     mahsulot=input('Mahsulotni kiriting: ')
#     narx=float(input(f'{mahsulot.title()}ning narxini kiriting: '))
#     mahsulotlar[mahsulot]=narx
#     shart=input('Yana mahsulot qo\'shishni xohlaysizmi: ')
#     if shart!='ha':
#         ishora=False
# print("Mahsulotlar ro'yxati: ")
# print(mahsulotlar)

''' Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi 
har bir mahsulotni e-bozordagi mahsulotlar bilan solishitiring (tayyor ro'yxat 
ishlatishingiz mumkin). Agar mahsuot e-bozorda mavjud bo'lsa mahuslot narhini chiqaring, 
aks holda "Bizda bu mahsulot yo'q" degan xabarni kor'sating. '''

buyurtmalar = ['olma','anjir','uzum','qovun']
mahsulotlar = {'olma':20000,
               'shaftoli':25000,
               'tarvuz':18000,
               'uzum':22000}

while buyurtmalar:
    buyurtma=buyurtmalar.pop()
    if buyurtma in mahsulotlar:
        print(f'{buyurtma.title()}ning narxi: {mahsulotlar[buyurtma]}')
    else:
        print(f"Bizda bu mahsulot yo'q: {buyurtma.title()}")