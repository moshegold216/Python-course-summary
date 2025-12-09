def my_function(letter):
    print("Hello king == ",letter)
#     וזוהי בעצם פונקציה בסיסית פונקציה זו יצירת פעולה ללא צורך לחזור אליה במידה ואנחנו רוצים להשתמש בה פשוט קוראים לפונצקיה פונקציה צריכה לעשות פעולה אחת בלבד פונקציה יכולה לקחת פרמטרים מפונרציה אחרת בשביל זה קיימות ה() שים לב לאחר יצירת הפונהקציה צריך לקרוא לה וזה נעשה עי כתית שם הפונקציה ו()
for i in "abcdefghij":
    my_function(i)
# ניתן ליצור בפונקציה גם לולאת FOR +RANGE שזה גורם לחזור כמה פעמים במקרה שלנו  על המספר האותיוות
#
def my_function2(n):
    print("Hello king == " +str(n))
for k in range(7):
    my_function2(k)
# יצירת לולאה המשוואה למספר
def sum_digits(number):
    number_string = str(number)
    sum = 0

    for i in number_string:
        sum += int(i)

    return sum
print(sum_digits(56))



# מה שמופיע מעליך זה דוגמא לכך שניתן גם לקבל בחזרה ערכים בפונקצה
# דגשים בפוקנציה 1. לכתוב רק פעולה אחת2. סדר בפונקציות 3ץשים לב להזחות 4. ליצור פונקצייה main ושם לקרוא לכך הפונקציות למשל  ואם אני עושה פעולה למשל ב
# def printer(n,k,i):
#     my_function2(n)
#     my_function2(k)
# for i in "abcdefghij":
#     my_function(i)
# זה הסדר הנכון במידה ורוצים לעשות שינוי בקריאה  במקרה הזה ללהכניס מחרוזת