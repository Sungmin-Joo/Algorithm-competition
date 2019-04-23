mail = input()
st = "CAMBRIDGE"
for i in st:
    mail = mail.replace(i.upper(),'')
    mail = mail.replace(i.lower(),'')
print(mail)