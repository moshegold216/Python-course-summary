# # number = 22
# # while number <20:
# #     print(number)
# #     # זה כמו יף רק בלולאה התנאי התקיים רק אם זה המצב כי אני לא יודע מראש עם זה נכון \לא
# tickets = int(input("הכנס מספר כרטיסים: "))
#
# if tickets < 0:
#     print("מספר כרטיסים שגוי")
# else:
#     if tickets > 100:
#         price = 43
#     else:
#         price = 48
#
#     total = tickets * price
#     print("הסכום הכולל לתשלום הוא:", total, "שח")
#
# num = int(input("הכנס מספר: "))
#
# if num >= 5 and num < 10:
#     print(num)
#
# print("bye")
#
# umb = int(input("הקלד מספר : "))
# if 100 <= abs(umb) <= 999:
#     print("three digits")
# else:
#     print("not three digits")
#
# gpd = int(input("wich numner: "))
# if gpd == 1 and gpd == 2 or gpd == 5 or gpd == 6:
#     print("we go to the restrunt")
# else:
#     print("go to watch movies")
#
# mo = int(input("wich number :"))
# if  not mo > 10:
#     print(mo)
# if mo >= 10:
#     print(mo)
#
passeord = str(input("password please :"))
if passeord =="Ayelt234":
    print("welcome home")
else:
    print("wrong password")

total = 0

while True:
    num = int(input("הכנס מספר: "))
    total += num

    if 100 <= abs(num) <= 999:
        break

print("סכום המספרים שנקלטו:", total)

num = int(input("הכנס מספר שלם גדול מ-1: "))

for i in range(2, num + 1):
    if num % i == 0:
        print(i)
        break


n = int(input("הכנס מספר טבעי: "))

factorial = 1

for i in range(1, n + 1):
    factorial *= i

print("העצרת של", n, "היא:", factorial)



n = int(input("הכנס אורך צלע הריבוע: "))

for i in range(n):
    for j in range(n):
        print("*", end="")
    print()
