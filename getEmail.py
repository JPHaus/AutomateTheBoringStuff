#! python3

import imapclient, pyzmail

imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)

#Login
email = input("Email: ")
password = input("Password: ")
imapObj.login(email, password)

# Get list of folders
#imapObj.list_folders()

# Select a folder to search through
imapObj.select_folder('INBOX', readonly=True)

imapObj.search(['ALL'])