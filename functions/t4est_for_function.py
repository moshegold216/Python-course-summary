def kefel(a, b):
    result = a * b

    if result < 0:
        return 0
    return result


print(kefel(5, 3))
print(kefel(-5, 3))
print(kefel(-2, -4))
#
# תבו פונקציה שתבדוק אם שני תווים נתונים הם לאותה קטגוריית ...
#
# אם אחת מהתווים אינה אות, החזר-1
# אם שני התווים הם אותו רישיות/קטנות, החזרה1
# אם שני התווים הם אותיות, אך לא בעלי רישיות גדולה וקטנה, החזרה0

def same_case(a, b):
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"

    if a in lower and b in lower:
        return 1
    elif a in upper and b in upper:
        return 1
    elif a in upper and b in lower:
        return 0
    elif a in lower and b in upper:
        return 0
    else:
        return -1
#
# צור פונקציה finalGrade, אשר מחשבת את הציון הסופי של סטודנט בהתאם לשני פרמטרים: ציון בבחינה ומספר פרויקטים שהושלמו.
#
# פונקציה זו צריכה לקבל שני ארגומנטים: exam - ציון למבחן (מ-0 עד 100); projects - מספר הפרויקטים שהושלמו (מ-0 ומעלה);
#
# פונקציה זו צריכה להחזיר מספר (ציון סופי). ישנם ארבעה סוגים של ציונים סופיים:
#
# 100, אם הציון בבחינה גבוה מ-90 או אם מספר הפרויקטים שהושלמו עולה על 10.
# 90, אם הציון בבחינה גבוה מ-75 ואם מספר הפרויקטים שהושלמו הוא לפחות 5.
# 75, אם הציון בבחינה גבוה מ-50 ואם מספר הפרויקטים שהושלמו הוא לפחות 2.
def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    elif exam > 75 and projects >= 5:
        return 90
    elif exam > 50 and projects >= 2:
        return 75
    else:
        return 0
#
#
# תם יוצרים גרסת מסוף מבוססת טקסט של משחק הלוח האהוב עליכם. במשחק הלוח, בכל תור יש שישה שלבים שחייבים להתרחש בסדר הזה: לגלגל את הקוביות, לזוז, להילחם, להשיג מטבעות, לקנות בריאות ולהדפיס סטטוס.
#
#
from preloaded import *

health = 100
position = 0
coins = 0

def main():
    roll_dice()
    move()
    combat()
    get_coins()
    buy_health()
    print_status()
# שוט, בהינתן מחרוזת של מילים, מחזירה את אורך המילה/ות הקצרות ביותר.
#
# המחרוזת לעולם לא תהיה ריקה ואין צורך להתחשב בסוגי נתונים שונים.
#

def find_shorts(s):
    min = len(s)
    counter = 0
    i = 0

    while i < len(s):

        if s[i] != ' ':
            counter += 1

        if s[i] == " " or i == len(s) - 1:
            if counter < min:
                min = counter
            counter = 0

        i += 1

    return min

