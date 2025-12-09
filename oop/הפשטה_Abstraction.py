# הפשטה זה להסתיר מהמשתמש את המורכבים  וישנם שני דרכים ליצור הפשטה
# דרך א <
class Animal:
    def __init__(self,name,type,size):
        self.name = name
        self.type = type
        self.size = size
    def Getdatalist(self):
        return "the name {} the type is {} the size is {}".format(self.name, self.type, self.size)

dog = Animal("yory","fish","Small") # מידע הקבוע מראש הוא לא צריך לדעת איך זה עובד אלא הוא לוחץ START והוא מקבל את המידע על החייה
#print(dog.Getdatalist())
# ויש עוד סוג הפשטה
# יצירת ירושה בסיסית ופשוט שימוש רק במשהו ספציפי וכך המשתמנש לא צריך לדעת מה זה
class Animal: # קלאס אב
    def __init__(self, name, type, size): # יצירת תכונות
        self.Name = name # חיבור לקלאס
        self.Type = type
        self.Size = size

    def GetDetails(self): #יצירת פונקציה אשר צחזירה
        return f'{self.Name} is a {self.Type}, its size is {self.Size}'
class Dog(Animal): # יצירת קלאס בן
    def __init__(self, size): # יצירת תכונות
        Animal.__init__(self, "nok", 'Dog', size) # כמו SUPER רק סינון ישיר לדגומא במקרה הזה מסנן את TYPE  כתבתי מראש מהו וכך המשתמש לא צריך לדעת מה זה טיפ ואני הגדלתי לעשות ועשיתי שלא יצטרך לדעת מה זה השם
dog = Dog("Small") # יצירתמשתנה בשם דוג ואז שימוש בדוג הקיים ונתינת ערכים לתכונות
print(dog.GetDetails()) # הדפס את דוג ואת דאטאליסט

# אז לסיכום הפשטה זה פשוט להפוך את הקוד לברור למשתתמש הוא לא צריך לדעת לוגיקה אפשר ע"י פשוט זה שנותנים ערכים מראש והוא צריך פשוט ללחוץ התחל ואפשר כ"י חיצירת ירושה ולקיחה רלוונטית ספציפים ממחלקת האב ושינוי הערכים