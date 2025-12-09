# כימוס זה יצירת משתנה פרטי כימוס בפייתון זה בעצם הסדרת מידע וכמה שיותר הסימן __ אחרי הסלף יגרום לכך  שיהיה שגיאה שתגיד לא ניתן לגשת למשתמש
class MyStudent:
    def __init__(self,name,privet):
        self.name = name
        # self.__privet = privet # כ הנה כאן זה דוגמא ליצירת משתנה וכימוס התוכן של התוכן שלו עי __  שים לב כימוס זה קיים אך רק במחלקה בלבד

         


def main():
    mnos = MyStudent("MOSD",9525457)
    print(mnos.name)
    # print(mnos.privet) # שאעשה כאן הדפס אקבל שגיאה נ
main()




