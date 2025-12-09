# ביטוי רגולרי מה זה אויך עובדים איתו ?! רגולרי זה בעצם שפה לניהול טקסט אפשר
#  1. לחפש טקסט על פי מחרוס              2. לבדוק אם תקין או לא 🔍 איתור תבניות בטקסט
# ✅ בדיקת תקינות (מייל, טלפון, סיסמה) ✂ חילוץ חלקים מתוך מחרוזת
#  🔁 החלפת טקסט לפי חוק   📑 פיצול מתקדם של מחרוזות
# בכדי להתנהל עם שפה זו צריך לייבא את ריגקס שזה השפה
import re # יבוא השפה
# בוא נלמד על כמה ביטויים נתחיל  מהראשון re.search
# re.search(pattern, text) - pattern -זה הביטוי -TEXT -זה הטקסט שאני בודק בו
#  re.search זוהי צורת חיפוד ע"י כך שאני נותן לי ביטוי והוא בודק אם קיים או לא והאם נכון הוא לא כמובן חלמטה יש סטרינג פשוט אבל הוא שימושי במידה ויש משנה תראה את זה אחרי הדוגמא למטה
# import re
# if re.search("moshe","moshe are cool"): # תנאי אם ר חיפו ש יש את הביטוי משה אז תדפיס משה נמצא ואחרת תדפיס משה לא קיים
#     print("moshe are find ")
# else:
#     print("moshe are not find")
# המשך הסבר מתי באמנת הre.רלוונטי מתי שיש מתשנה ואני בודק בו למשל
# יצרתי משתנה בשם USER ואז עשיתי בדיקה דרך RE.SEARCH האם זמספר תווים תקין
# בכדי להמנע משגיאות במידה ומדובר באות גדולה \קטנה נוסיף [ובתוכו נכניס רגולטור ]
# לדוגמא:
# if re.search("f[FF]rema","frame is food"): #   שים לב כתבתי [] רגלטור ובתוכו הכנסץי אות גדולה \קטנה וכמובן לא שכחתי לכתוב R לפני שידע אקסא
# user=input("what is your number?: ")
# # if re.search(r"^\d{15}$", user):
# #     print(f"User {user} is absorbed" )
# # else:
# #     print(f"User {user} is not absorbed")
# #
# user_name = input("what is your name?: ")
# name_user = input("what is your name_user?: ")
# # if re.search(r"^[\w\.-]+@gmail\.com$", name_user):
# #     print( f" {name_user}  is found")
# # else:
# #     print(f"{name_user} is not found")
# #  זה חיבור של שלושתם לתנאי אחד אן  יש 6 ספרות ליוזר ו מייל תקין או תדפיס לי היוזר נמצא אחרת היזור לא נמצא
# if re.search(r"^\d{6}$", user) and re.search(r"^[\w\.-]+@gmail\.com$", name_user) and re.search(r"[mM]oshe", name_user):
#     print( f" {user_name} is found")
# else:
#     print(f"{name_user} is not found")
#  result in cmd -
# k is not found \k is found
# lest move on re.finall מחזיר את כל הערכים שדומים למשל
# re.findall() returns a list of all the matching names
sentence = "Hey there, my name is Shuli"
camel_case_list = re.findall(r"[A-Z][a-z]+", sentence)
print(camel_case_list) # כאן  קיבלתי הכל לעוד ערכיפ פשוט זה נותן בכל המשפט לא רק במילה אחת
