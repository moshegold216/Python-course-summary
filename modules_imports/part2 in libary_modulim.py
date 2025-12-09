# the continue  of the libary moudel !
#  today we are gooing to talk abut sys model
#  for first what is sys model ?
# sys is model for play the sistem we have more information there - https://www.w3schools.com/python/ref_module_sys.asp
# המשתנה הראשון שאציג מתוך המודול הוא המשתנה argv(קיצור לargument variables) הכולל את רשימת הפרמטרים שהועברו לסקריפט שלנו משורת הפקודה.
#  ניתן להריץ דרך שורת פקודה
#  המודול sys מאפשר לנו לגשת למידע על תהליך פייתון שרץ כרגע כמו:
#
# פרמטרים משורת הפקודה
#
# מערכת ההפעלה
#
# גרסת פייתון
#
# קלט / פלט ועוד
#  מערך זה שאוכל לחלק את הקוד למשל אם אתוב בשורת CMD - python '.\part2 in libary_modulim.py' 11,32 לא יקרה כלום כל עוד ךלא הגדרתי שאני נותן לי אישור לפרמטר SYS
import sys # -code for the import
x = str("hi world")
print(f"this is what found - {x}")
print(sys.argv) # - זה התדפיס של התוכן הפרמטרים +