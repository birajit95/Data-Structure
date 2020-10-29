import smtplib
# import os
# # import smtplib
# import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = 'birajitdemo@gmail.com'
EMAIL_PASSWORD = '9595birajitB@'

# contacts = ['YourAddress@gmail.com', 'test@example.com']

msg = EmailMessage()
msg['Subject'] = 'Hello World'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'birumnna@gmail.com'

msg.set_content('This is a plain text email')

msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">This is an HTML Email!</h1>
    </body>
</html>
""", subtype='html')
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)