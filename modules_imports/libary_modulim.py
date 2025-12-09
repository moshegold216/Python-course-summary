# # תיקיות = ומודלים זה בעצם אותו דבר אבל מה זה מכיוון שפיתון זה קוד פתוח אם אנחנו רוצים לבצע פעולה שכבר ביצע מישהו אחר אנחנו לא נצטרך להעתיק הכל נוכל פשוט להוריד את הקוד של אותו אדם ולהנות מחופש הבחירה
# # pip install "modelname" - זה הקוד להורדה מודל נמא זה השם של התיקייה שאתה רוצה להריד
# # import - זה הפקודה לייבוא הספרייה עצמה
#
# #                                                            סוגי מודלים נפוצים:
# #
# #           - OS זוהי ספרייה אשר מוקתנת בחבילת פייתון באופן אוטומטי ומה שהיא נותנת זה העלאת קבצים שינוי שם קבצים ויצירת תיקיות בקישור למטה ניתן  לראות פקודות נפוצות !
# #                                                 https://www.w3schools.com/python/module_os.asp   -link for more information
# #  example  for using the os-
# import os
# print(os.environ.get('HOMEPATH')) # to know the home -path
# print(os.getcwd()) # -to know which folder i am in
# for root, dirs, files in os.walk(r"C:\Users\משהגולדשטיין\OneDrive - click\Documents"): #חיבור לנתיב וחפש שם את הדברים האלה : ROOT - זה הנתיב הנוכחי DIRS- רשימת התיקיות בתוך רות וFILES רשימת הקבצים ואז תתחבר לנתיב הזה ושם חפש
#     for name in files: # יצירת מתשנה בשם NAME שהוא גורם לכך שהפכתי כת הקבצים לNA,E  את שם הקובץ
#         print(f"your file in {name}") # תדפיס לי את המשתנה FILES רק שאני כבר שיניתי אותו לNAME והוא יתןלי תתוצאה שריצתי
# #  os.rename - to know how to change the name !
# #  os.listdir  -replay names for folder u !
# #  endswith - how that end in path for exmpli (.text) \ (excel)!


import os

path = r"C:\Users\משהגולדשטיין\OneDrive - click\Documents\new_progect_for isral" # I created variable his name path and i give to hime a value (my file path )

for name in os.listdir(path): # i was crate variables and cal him name and  i pot that in listdir in on folder and i do print the name of the file
    print(name)
    if name.endswith("txt"): # i do a if the file ending with (text):
        filename = path + '/' + name # variable in name filenme = to path and to name
        newname = filename[:-3] + "old" # new name = to last name
        print(f"Renaming {filename} => {newname}")  #print that new and the last
        os.rename(filename, newname) # now change the name to new name !

