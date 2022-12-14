import pandas
import datetime
import random
import smtplib

EMAIL = "enter_email"
PASSWORD = "enter_pass"

now = datetime.datetime.now()
today = (now.month, now.day)

data = pandas.read_csv("birthdays.csv")
b_dict = {(data_row["month"], data_row["day"]) : data_row for (index, data_row) in data.iterrows()}

if today in b_dict:
    bd_person = b_dict[today]
    file_path = f"bday template/letter_{random.randint(1,3)}.txt"
    with open(file_path) as file:
        content = file.read()
        content = content.replace("[NAME]", bd_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=bd_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{content}")








