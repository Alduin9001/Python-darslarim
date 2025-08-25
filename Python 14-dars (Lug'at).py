# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 13:48:12 2025

@author: smann
"""
""" otam (onam, akam, ukam, va hokazo) degan lug'at 
yarating va lug'atga shu inson haqida kamida 3 ta m'alumot kiriting 
(ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi ma'lumotni 
 matn shaklida konsolga chiqaring: Otamning ismi Mavlutdin, 1954-yilda, 
 Samarqand viloyatida tug'ilgan """
 
# myself = {'ism': 'Kamoliddin', 'date_birth': '2003', 'city': 'Navoiy'}
# print(f"Ismim {myself['ism']}, {myself['date_birth']} -yilda {myself['city']} \
# shahrida tug'ilganman")

""" Oila a'zolaringizning sevimli taomlari lug'atini tuzing. 
Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin. 
Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh"""

# favorite_meal={'dad':'palov', 'mom':'norin', 'myself':'manti','brother1':'lavash',
#                'brother2': 'somsa', 'brother3': 'cakes'
#                }
# print(f'My dad\'s favorite food is {favorite_meal['dad']}')
# print(f'My mom\'s favorite food is {favorite_meal['mom']}')
# print(f'My brother1\'s favorite food is {favorite_meal['brother1']}')

""" Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. 
Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo ketma-ketligida 
chiroyli qilib konsolga chiqaring. """

# python_dict={'list':'ro\'yhat', 'tuple':'o\'zgarmas ro\'yhat', 'set':'to\'plam' ,
#              'dictionary':'lug\'at', 'for':'takrorlanish', 'if':'Shartlarni tekshirish operatori',
#              'boolean':"Mantiqiy qiymat",
#              'integer':'Butun son',
#              'float': "O'nlik son"}
# for key, value in sorted(python_dict.items()):
#     print(f'Kalit: {key} - Qiymat: {value}')

""" Davlatlar va ularning poytaxtlari lug'atini tuzing. 
Avval lug'atdagi davlatlarni, keyin poytaxtlarni alohida-alohida, 
alifbo ketma-ketligida konsolga chiqaring. """

# countries={"Oʻzbekiston": "Toshkent",
#     "Qozogʻiston": "Astana",
#     "Qirgʻiziston": "Bishkek",
#     "Tojikiston": "Dushanbe",
#     "Turkmaniston": "Ashxobod",
#     "Rossiya": "Moskva",
#     "Xitoy": "Pekin",
#     "Yaponiya": "Tokio",
#     "Janubiy Koreya": "Seul",
#     "Hindiston": "Yangi Dehli",
#     "Pokiston": "Islomobod",
#     "Turkiya": "Anqara",
#     "Germaniya": "Berlin",
#     "Fransiya": "Parij",
#     "Italiya": "Rim",
#     "Ispaniya": "Madrid",
#     "Buyuk Britaniya": "London",
#     "AQSh": "Vashington",
#     "Kanada": "Ottava",
#     "Misr": "Qohira"}

# for key in sorted(countries.keys()):
#     print(key)
# print('-----------------------------')
# for value in sorted(countries.values()):
#     print(value)
    
""" Foydalanuvchidan istalgan davlatni kiritishni so'rang va 
shu davlatning poytaxtini konsolga chiqaring. 
Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, 
"Bizda bunday ma'lumot yo'q" degan xabarni chiqaring."""

# countries={"Oʻzbekiston": "Toshkent",
#     "Qozogʻiston": "Astana",
#     "Qirgʻiziston": "Bishkek",
#     "Tojikiston": "Dushanbe",
#     "Turkmaniston": "Ashxobod",
#     "Rossiya": "Moskva",
#     "Xitoy": "Pekin",
#     "Yaponiya": "Tokio",
#     "Janubiy Koreya": "Seul",
#     "Hindiston": "Yangi Dehli",
#     "Pokiston": "Islomobod",
#     "Turkiya": "Anqara",
#     "Germaniya": "Berlin",
#     "Fransiya": "Parij",
#     "Italiya": "Rim",
#     "Ispaniya": "Madrid",
#     "Buyuk Britaniya": "London",
#     "AQSh": "Vashington",
#     "Kanada": "Ottava",
#     "Misr": "Qohira"}

# # 1-usul
# # country= input('Istalgan davlatni kiriting: ')
# # capital = countries.get(country)
# # if capital==None:
# #     print('Kechirasiz, bizda bu haqida ma\'lumot yo\'q')    
# # else:
# #     print(f"{country.upper()}ning poytaxti {capital.title()} shahri")

# # 2-usul

# davlatlar = {
#     "Germaniya": "Berlin",
#     "Fransiya": "Parij"
# }

# davlat = input("Davlat nomini kiriting: ").strip().lower()

# # Kalitlarni tekshiramiz
# topildi = False
# for k, v in davlatlar.items():
#     if k.lower() == davlat:   # har ikkalasini lower() qilib solishtiramiz
#         print(f"{k} poytaxti: {v}")
#         topildi = True
#         break

# if not topildi:
#     print("Bizda bunday ma'lumot yo'q")

""" Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). 
Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. 
Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, 
agar taom menuda bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q" 
degan xabarni chiqaring. """

# menu = {
#     "osh": 25000,
#     "shashlik": 18000,
#     "lag'mon": 22000,
#     "manti": 20000,
#     "norin": 28000,
#     "somsa": 8000,
#     "sho'rva": 15000,
#     "mastava": 16000,
#     "beshbarmoq": 30000,
#     "qozon kabob": 35000
# }

# orders=[]
# for i in range(3):
#     a=input(f'{i+1}-taomni kiriting: ').lower()
#     orders.append(a)
# for order in orders:
#     if order in menu:
#         print(f'{order} - {menu[order]} turadi')
#     else:
#         print(f'Bizda {order} yo\'q')

""" Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi
 ma'lumotlarni lug'at ko'rinishida saqlang. Lug'atlarni bitta ro'yxatga joylang, 
 va har bir shaxs haqidagi ma'lumotni konsolga chiqaring. """
 
# person1={'name':"Anvar Narzullayev", 
#          'date_birth': 2000, 
#          'occupation':'programmer', 
#          'address':'toshkent'}

# person2={'name':"Leo Messi", 
#          'date_birth': 1987, 
#          'occupation':'footballer', 
#          'address':'USA'}

# person3={'name':"Abdukarim Mirzayev", 
#          'date_birth': 1989, 
#          'occupation':'journalist', 
#          'address':'toshkent'}

# person4={'name':"Sirojiddin Rahmatullayev", 
#          'date_birth': 2000, 
#          'occupation':'English teacher', 
#          'address':'Navoiy'}

# celebrities=[person1, person2, person3, person4]

# for person in celebrities:
#     print(f"{person['name'].title()} {person['date_birth']}-yilda \
# tug'ilgan. Kasbi {person['occupation'].title()},\
# {person['address'].title()}da yashaydi")

""" Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing. 
For tsikli yordamida muallifning ismi va uning asarlarini konsolga chiqaring."""

# person1={'name':"Anvar Narzullayev", 
#          'date_birth': 2000, 
#          'occupation':'programmer', 
#          'address':'toshkent',
#          'asarlar': ['Python', 'C#', 'C++', 'Java']}

# person2={'name':"Leo Messi", 
#          'date_birth': 1987, 
#          'occupation':'footballer', 
#          'address':'USA',
#          'asarlar':['FIFA','UEFA','LA LIGA','SUPER LIGA']}

# person3={'name':"Abdukarim Mirzayev", 
#          'date_birth': 1989, 
#          'occupation':'journalist', 
#          'address':'toshkent',
#          'asarlar':['You tube', 'Instagramm']}

# person4={'name':"Sirojiddin Rahmatullayev", 
#          'date_birth': 2000, 
#          'occupation':'English teacher', 
#          'address':'Navoiy',
#          'asarlar':['IELTS','CEFR']}

# celebrities=[person1, person2, person3, person4]
# for person in celebrities:
#     print(person['name'])
#     for asar in person['asarlar']:
#         print(asar)

"""Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang.
Do'stingiz ismi kalit, uning sevimli kinolarini esa ro'yxat ko'rinishida 
lug'artga saqlang. Natijani konsolga chiqaring."""

# kinolar = {
#     'ali':['Terminator','Rambo','Titanic'],
#     'vali':['Tenet','Inception','Interstellar'],
#     'hasan':['Abdullajon','Bomba','Shaytanat'],
#     'husan':['Mahallada duv-duv gap','John Wick']
#     }

# for ism, kino in kinolar.items():
#     print(f'{ism} quyidagi kinolarni yoqttiradi')
#     for k in kino:
#         print(k)

""" Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida 
ma'lumotlarni lug'at ko'rinishida saqlang. Har bir davlat haqida ma'lumotni konsolga 
chiqaring."""

# davlatlar = {
#     "o'zbekiston":{'poytaxt':"toshkent",
#                    'maydon':448978,
#                    'aholi':33_000_000,
#                    'pul birligi':"so'm"
#                    },
#     "rossiya":{'poytaxt':"moskva",
#                    'maydon':17_098_246,
#                    'aholi':144_000_000,
#                    'pul birligi':"rubl"
#                    },
#     "aqsh":{'poytaxt':"vashington",
#                    'maydon':9_631_418,
#                    'aholi':327_000_000,
#                    'pul birligi':"dollar"},
#     "malayziya":{'poytaxt':"kuala-lumpur",
#                    'maydon':329750,
#                    'aholi':25_000_000,
#                    'pul birligi':"rinngit"}
#     }

# for davlat, info in davlatlar.items():
#     if davlat.lower()=='aqsh':
#         davlat = davlat.upper()
#     else:
#         davlat = davlat.capitalize()
#     print(f"\n{davlat}ning poytaxti {info['poytaxt'].title()}"
#           f"\nHududi: {info['maydon']} kv.km"
#           f"\nAholisi: {info['aholi']}"
#           f"\nPul birligi: {info['pul birligi']}")

""" Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas,
foydalanuvchi so'ragan davlat haqida ma'lumot bering. Agar davlat sizning lug'atingizda
 mavjud bo'lmasa, "Bizda bu davlat haqida ma'lumot yo'q" degan xabarni chiqaring."""
 
davlatlar = {
    "o'zbekiston":{'poytaxt':"toshkent",
                   'maydon':448978,
                   'aholi':33_000_000,
                   'pul birligi':"so'm"
                   },
    "rossiya":{'poytaxt':"moskva",
                   'maydon':17_098_246,
                   'aholi':144_000_000,
                   'pul birligi':"rubl"
                   },
    "aqsh":{'poytaxt':"vashington",
                   'maydon':9_631_418,
                   'aholi':327_000_000,
                   'pul birligi':"dollar"},
    "malayziya":{'poytaxt':"kuala-lumpur",
                   'maydon':329750,
                   'aholi':25_000_000,
                   'pul birligi':"rinngit"}
    }

country= input('Davlatni kiriting: ')
if country.lower() in davlatlar:
    info=davlatlar[country]
    if country=='aqsh':
        country=country.upper()
    else:
        country = country.capitalize()
    print(f"\n{country}ning poytaxti {info['poytaxt'].title()}"
              f"\nHududi: {info['maydon']} kv.km"
              f"\nAholisi: {info['aholi']}"
              f"\nPul birligi: {info['pul birligi']}")
else: print('Bizda bunday davlat yo\'q')
    