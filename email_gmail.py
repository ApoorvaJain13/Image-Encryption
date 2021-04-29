import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
 
def messageEmailSend(toEmailAddress, messageBody):
	try:
		server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		#server.starttls()

		fromaddr = 'encrypto.app@gmail.com'

		server.login(fromaddr, "ACCOUNT_PASSWORD")

		msg = MIMEMultipart()
		msg['From'] = fromaddr
		msg['To'] = toEmailAddress
		msg['Subject'] = 'Encrypto - Secret Key'
		 
		body = messageBody
		msg.attach(MIMEText(body, 'plain'))

		text = msg.as_string()
		server.sendmail(fromaddr, toEmailAddress, text)
		os.system("notify-send Encrypto: 'Key Sent Successfully through E-Mail'")
		server.quit()

	except smtplib.SMTPException:
		print ("Unable to send mail.")
		os.system("notify-send Encrypto: 'Error Sending the Key Through E-Mail'")

if __name__ == '__main__':
	messageEmailSend("manpreetkaur3395@gmail.com", "8:hello:pika_pass")
