import pandas
import datetime as dt
import random
import smtplib

now = dt.datetime.now()
month = now.month
day = now.day
my_email = "orisco.test@gmail.com"
my_password = "Os6852265"


user_input = input("enter a birthday (name,email,year,month,day) ")
with open("birthdays.csv", 'a') as file:
    file.write(user_input)


birthday_list = pandas.read_csv("birthdays.csv")
new_dict = birthday_list.set_index(['month', 'day']).T.to_dict()

if (month, day) in new_dict:
    name = new_dict[(month, day)]['name']
    email = new_dict[(month, day)]['email']
    random_number = random.randint(1,3)

    with open(f"letter_templates/letter_{random_number}.txt") as letter:
        birthday_letter = letter.read()
        new_letter = birthday_letter.replace("[NAME]", name.title())

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=email,
                            msg=f"Subject: Happy Birthday\n{new_letter}")
