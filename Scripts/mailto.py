import config
import sendgrid
import os
from sendgrid.helpers.mail import *
import base64
import pandas
def email(sender,to,message,subject,attach=False):
   

    sg = sendgrid.SendGridAPIClient(apikey=config.api_key)
    from_email = Email(sender)
    to_email = Email(to)
    content = Content("text/html",message)
    if(bool(attach)):
        with open(attach,'rb') as f:
            data = f.read()
            f.close()
        encoded = base64.b64encode(data).decode()
        attachment = Attachment()
        attachment.content = encoded
        attachment.type = 'image/png'
        attachment.filename = 'file'
        attachment.disposition = 'inline'
        attachment.content_id = 'attach'
        
        try:
            mail = Mail(from_email, subject, to_email, content)
            mail.add_attachment(attachment)
            response = sg.client.mail.send.post(request_body=mail.get())
            print("mail sent to",to)
            print(attach)
            print(response.status_code)
        except:
            print("mail not sent to ", to)
            pass

    else:
        try:
            mail = Mail(from_email, subject, to_email, content)
            response = sg.client.mail.send.post(request_body=mail.get())
            print("mail sent to",to)
            print(response.status_code)
        except:
            print("mail not sent to ", to)
            pass
        
def gen_message(name,reg,text,fro):
    message = """<html>
<head></head>
 <body><p>Hey {name} {reg}!</p><br>
 <p>{text}</p>
 <br>Regards<br>Rudranshu

</body>
</html>""".format(text = text,name = name,reg =reg,fro = fro)
    return message
    
if __name__ == "__main__":
    # print((gen_message("ubaid","17BCE0983","hello","ubaid")))
    email("abcd@gmail.com","rudranshuganjoo@gmail.com","hello","t")
