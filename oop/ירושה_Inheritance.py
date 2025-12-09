# ירושה זה בעצם העברת תכונות +מתודות למחלקה אחרת והצורה שעושים את זה שבשפוט מוסיפים את שם מחלקת האב בסוגריים
class MyStudent:
    pass

class Student(MyStudent): # ככה בעצם יורשים  מתודות ותכנות
    pass





class Cars: # מקרה הזה יצרנו קלאס  אב ונתנו לו תכונה בשם מודל
    def __init__(self,model,fast):
        self.model = model # קישרנו לקלאס הזה
        self.fast = fast
    def say_hello(self): # יצרנ מתודה בשם תגיד שלום ואז עשינו שהמתודה תחזיר את שלום זה המדל של הרכב
        return(r"Hello Cars the model {} and you on ".format(self.model))
# class Supercar(Cars):#  יצרנו קלאס בן ונתנו לו את הירושה מהאב  ע"י שכתבנו בסוגריים אבל לא נתנו שום ערך נוסף 
#     def over_drive(self):
#         return "Over speed " if self.fast >150 else "Drive "


def main (): # מאיין
    cars = Supercar("ausy 55",230,"der") # יצרנו משתנה בשם רכבים ונתנו לו שימוש בקלאס ואז נתצנו לו ערך
    cars3 = Supercar("mercedes R8 ",130,"der")
    print(cars.say_hello(),cars.over_drive())
    print(cars3.say_hello(),cars.over_drive())






# אפשר גם לעשות מתודה יניט בתוך הקלאס עי שימוש בדופר
class Supercar(Cars):#  יצרנו קלאס בן ונתנו לו את הירושה מהאב  ע"י שכתבנו בסוגריים
    def __init__(self,model,fast,fastchange):
        super().__init__(model,fast) # המתודה הזו גורמת לכך שאפשר לקשר בין הבן לאב כי אם היינו עושים את זה בלי אז באב היה לנו תכונה וגם בבן ואז  הוא לא מכיר בתכונה כי אנחנו עשינו הוספת תכונה ולכן אנחנו שולחים את זה לאב גם שהכליהיה מסונכרן
        self.fastchange = fastchange

    def over_drive(self):
        return "Over speed " if self.fast > 150 else "Drive "

main() # קריאה לפונקציה המנהל
