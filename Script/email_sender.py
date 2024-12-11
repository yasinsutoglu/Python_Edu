# SMTP (Simple Mail Transfer Protocol) - Similar to HTTP/s case
# Simple Mail Transfer mechanism (SMTP) is a mechanism for exchanging email messages between
# servers. It is an essential component of the email communication process and operates at the
# application layer of the TCP/IP protocol stack. SMTP is a protocol for transmitting and
# receiving email messages. In this article, we are going to discuss every point about SMTP.

#  What is Simple Mail Transfer Protocol?
# SMTP is an application layer protocol. The client who wants to send the mail opens a
# TCP connection to the SMTP server and then sends the mail across the connection.
# The SMTP server is an always-on listening mode. As soon as it listens for a
# TCP connection from any client, the SMTP process initiates a connection through port 25.
# After successfully establishing a TCP connection the client process sends the mail instantly.
# Details: https://www.geeksforgeeks.org/simple-mail-transfer-protocol-smtp/
# ----------------------------------------------
# import smtplib # it provides all things us to create smtp server.
# from email.message import EmailMessage
# from string import Template
# from pathlib import Path    # or os.path
#
# html_temp = Template(Path('./index.html').read_text())
#
# email = EmailMessage()
# email['from'] = 'Universe'
# email['to'] = 'ysutoglu@gmail.com'
# email['subject'] = 'You are good person'
# email.set_content(html_temp.substitute({'name': 'Jess'}), 'html')
# OR
# email.set_content(html_temp.substitute(name='Jess'), 'html')
'''
<!DOCTYPE html>
<html>
<head>
</head>
<body>
    Hello $name, You are awesome, and you know it!
</body>
</html>
'''

# creates SMTP session
# with smtplib.SMTP(host='smtp.gmail.com', port=465) as smtp:
	#   smtp.ehlo() # ehlo --> standard protocol
	#   smtp.starttls() # tls--> encryption mechanism
	#   smtp.login('<sender email address>', '<sender password>')
	# # message to be sent
	# message = "Message_you_need_to_send"
	# # sending the mail
	# smtp.sendmail('<sender email address>', '<receiver email address>', message)
	# # terminating the session
	# smtp.close()
	#-----------------

# https://stackoverflow.com/questions/10147455/how-to-send-an-email-with-gmail-as-provider-using-python?answertab=modifieddesc#tab-top
# https://stackoverflow.com/questions/72480454/sending-email-with-python-google-disables-less-secure-apps