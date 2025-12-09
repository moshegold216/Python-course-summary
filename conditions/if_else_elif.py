number = 10
if number %2 == 10:
    # IF זה תנאי אם זה ככה אז תעדשה ככה
    print("THIS NUMBER IS EVEN")
else:
    #ELSE זה במידה ולא אז תדפיס ככה מאוד קיצוני

    print("THIS NUMBER IS ODD")
grade = 75
if grade >= 90:
    print("מצטיין")
elif grade >= 70:
    print("טוב")
# אינו קיצוני זה כמו עוד IF נותן עוד אופציות
elif grade >= 60:
    print("מספיק")
else:
    print("נכשל")


movie = 'Batman'
role = 'viin'
hair_color = 'green'

if movie == 'Batman' and role == 'villain' or hair_color == 'green':
    print("It's the Joker!")
# ניתן להוסיף תנאים אם אנד על יף אנד זה חייב להיות גם וגם הכל חייב להתקיים אבל בOR זה או או
else:
    print('Some other character')
# ניש דבר כזה תנאי בתוך תנאי מכניבים את היף בתוך התנאי
