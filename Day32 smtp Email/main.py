'''import smtplib

email = ""
password = ""
with smtplib.SMTP("smtp-mail.outlook.com", 587) as connetion:
    connetion.starttls()
    connetion.login(user=email,password=password)
    connetion.sendmail(
        from_addr=email,
        to_addrs="stephensusanto33@gmail.com",
        msg="Subject: Hello\n\n This is the body email"
    )'''
'''
import datetime

now = datetime.datetime.now()
print(now.weekday())'''


import smtplib
import datetime
import random

email = ""
password = ""
#motivation
now = datetime.datetime.now()
weekday  = now.weekday()
if weekday == 1:
    with open("quote.txt") as quote_file:
        all_quote = quote_file.readlines()
        quote = random.choice(all_quote)
    with smtplib.SMTP("smtp-mail.outlook.com", 587) as connetion:
        connetion.starttls()
        connetion.login(user=email, password=password)
        connetion.sendmail(
            from_addr=email,
            to_addrs=email,
            msg=f"Subject: Motivation\n\n{quote}")
