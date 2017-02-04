#! python3
# sendEmail.py connects to gmail's smtp server and allows the user to send a message to one person at a time
import smtplib

#smtp.gmail.com

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
#print(type(smtpObj))
print(smtpObj.ehlo())
# Returns 250 if successful

# Send login info
email = input("Email: ")
password = input("Password: ")
smtpObj.login(email, password)
# Returns 235 if successful
# Look into setting up application specific pass for gmail

recipient = input("Send To: ")

msg = input("Message: ")

smtpObj.sendmail(email, recipient, 'Subject \n' + msg)

# Terminate the smtp session
smtpObj.quit()
# Returns 221 if termination is successful

