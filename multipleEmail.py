import smtplib as s

# Set up the SMTP server
ob = s.SMTP('smtp.gmail.com', 587)
ob.ehlo()
ob.starttls()
# Login to your Gmail account
ob.login('sumelbdx@gmail.com', 'password')
# Email details

subject='test python'
body=" i love python"
message='subject:{}\n\n{}'.format(subject,body)

# List of recipients
listadd=['sumelahmadbd@gmail.com', 'smmsumel@gmail.com''itsumel@gmail.com']

# Send the email
ob.sendmail('sumelbdx@gmail.com', listadd, message)
print('Send E-mail')
ob.quit()