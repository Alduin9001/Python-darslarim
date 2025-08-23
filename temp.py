# davlatlar=['England', 'Marokash', 'Daniya', 'Uzbekistan', 'Brasil', 'France', 'Russia', 'China', 'Japan', 'Korea', 'USA']
# print(davlatlar)
# print(sorted(davlatlar, reverse=True))
# even_numbers=list(range(120, 1201, 2))
# print(even_numbers[-20:-1])
# taomlar=[]
# taomlar.append('osh')
# taomlar.append('manti')
# taomlar.append('kabob')
# taomlar.append('chuchvara')
# taomlar.append('norin')
# taomlar.append('burger')
# print(taomlar)
# nonushta=taomlar[:]
# print(nonushta)
# nonushta.remove('osh')
# del(nonushta[1])
# nonushta=tuple(nonushta)
# print(nonushta)
# ismlar=['Ali', 'Vali', 'Soli', 'Karim', 'Kamol']
# sanovchi=0
# for ism in ismlar:
#     print(f"Assalomu alaykum {ism}. Xush kelibsiz!!!")
#     sanovchi +=1
# print(f'Kod {sanovchi} marta takrorlandi')
# toq_sonlar=list(range(11, 100, 2))
# for son in toq_sonlar:
#     print(f"{son} sonining kubi {son**3} ga teng")
# favorite_movie=[]
# print("5 ta eng sevimli kinongiz qaysi?")
# for n in range(5):
#     favorite_movie.append(input(f"{n+1} -sevimli kinongizni kiriting: "))
# print(favorite_movie)

# a='Dasturlash '*3
# b=' ni uqiymiz'
# print(a+b)
# a = ("kitob", "daftar", "ruchka") 
# b = ("qalam", "qog'oz") 
 
# c = a + b 
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car=='gm':
#         print(car.upper())
#     else:
#         print(car.title())
# print(cars)

# user_name=input("Foydalanuvchi nomingizni kiriting: ")
# if user_name.lower()=='admin':
#     print('Xush kelibsiz Admin! Foydalanuvchilar ro\'yxatni ko\'rishni xoxlaysizmi?')
# else:
#     print(f"Xush kelibsiz {user_name}")

# x=float(input('x qiymatlarni kiriting: '))
# y=float(input('y qiymatlarni kiriting: '))
# if x==y: print('Bu sonlar teng ekan!')

# a=float(input('Sonni kiriting: '))
# print(f"{a**(1/2)} musbat son!") if a>0 else print('Musbat son kiriting')
# user_age=int(input('yshingizni kiriting: '))
# if user_age<4 or user_age>65:
#     print('Sizga kirish bepul')
# elif 18>user_age:
#     narh=10000
#     print(f'Kirish narxi {narh}')
# elif 18<user_age:
#     narh=20000
#     print(f'Kirish narxi {narh}')
# products=['olma', 'sabzi', 'guruch', 'makka', 'qoshiq', 'igna', 'sut','ruchka', 'qalam','daftar']
# basket=[]
# a=5
# for i in range(5):
#     q=input(f'{i+1}-mahsulotni kiriting: ')
#     basket.append(q)
# bor_m=[]
# yoq_m=[]
# for product in basket:
#     if product.lower() in products:
#         print(f'{product} do\'konda bor')
#         bor_m.append(product)
#     else:
#         print(f'{product} do\'konda yo\'q')
#         yoq_m.append(product)
# if  yoq_m:
#     print(f'Quyidagi ma\'hsulotlar do\'konimizda bor: {yoq_m}')
# else: print('Barcha ma\'hsulotlar do\'konimizda mavjud')
# users=['kamol', 'asi', 'anvar', 'shaxi', 'diyor', 'jaxon']
# user_name=input('Iltimos, foydalanuvchi logini kiriting: ')
# if user_name in users:
#         print('Bu login band! Iltimos boshqa login kiriting: ')
# else:
#         print(f'Xush kelibsiz {user_name}')

# son=int(input('Ixtiyoriy butun son kiriting: '))
# for i in range(2,11):
#     if son%i==0:
#         print(f'Bu son {i} ga bo\'linadi')
# else:
#    print('Bu son raqamlarga bo\'linmaydi')



users = ['alisher1983','aziza','yasina', 'umar']

login = input("Yangi login tanlang:" )

if login in users:
    print('Login band, yangi login tanalng!')
else:
    print("Xush kelibsiz!")    






























