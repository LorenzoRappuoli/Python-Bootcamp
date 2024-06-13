##################### Extra Hard Starting Project ######################
import smtplib as sm
import datetime as dt
import random as rd
import os


my_email = "lorenzo.rappuoli.bip.2@gmail.com"

# 1. Update the birthdays.csv

with open('birthdays.csv', 'r') as file:
    content = file.readlines()


# 2. Check if today matches a birthday in the birthdays.csv

date_today = dt.datetime.now().date()

year = date_today.year
month = date_today.month
day = date_today.day

for l in content:

    elements = [x.replace(' ','') for x in l.split(',')]

    try:
        if year == int(elements[2]) and month == int(elements[3]) and day == int(elements[4]):

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

            path_document = "./letter_templates/"
            document = rd.choice(os.listdir(path_document))

            print('document: ', document)

            with open(path_document+document, 'r') as letter:
                content_letter = letter.read()


            content_letter = content_letter.replace('[NAME]',elements[0])


# 4. Send the letter generated in step 3 to that person's email address.

            with sm.SMTP("smtp.gmail.com") as connection:  # così si chiu
                connection.starttls()
                connection.login(
                    user=my_email,
                    password='mxds ydep xnoj rkmr'
                )
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs='ilaria.faleschini@gmail.com',
                    msg=
                    f"""
                    Subject: messaggio auguri per topina
                    {content_letter}
                    """

                )
    except:
        print("Issue with this element: ", l)








