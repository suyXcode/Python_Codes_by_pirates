import smtplib

# email and password
myemail = "suyxcode@gmail.com"
password = "lgcs iyms oheb mlck"



# create connection

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(myemail, password)

# send email
connection.sendmail(
    from_addr=myemail,
    to_addrs="heysuyash891@gmail.com",
    msg="Subject: Hello from Python\n\nThis is a test email sent from Python."
    
)

connection.close()