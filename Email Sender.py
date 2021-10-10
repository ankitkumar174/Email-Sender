import win32com.client as win32
list = ["..................... Multiple Email Address ........................"]
for x in list:
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To=x
    mail.Subject= ".............................................."
    bd1='''.............

.............................. Mail Content ........................................
Mob- ..........'''
    mail.Body = bd1
    mail.Attachments.Add("... File Path ....")
    #mail.Display(True)
    mail.Send()