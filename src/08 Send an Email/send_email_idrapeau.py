import smtplib
import email

def send_email(email_address, subject_line, message_body):
  gmail_username = "ivanadrapeau"
  gmail_app_password = "" #placeholder

  recipient = [email_address]
  message = email.mime.MIMEtext(message_body)
  message["Subject"] = subject_line
  message["To"] = email_address
  message["From"] = f"{gmail_username}@gmail.com"

  smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
  smtp_server.login(gmail_username, gmail_app_password)
  smtp_server.sendmail(message["From"], recipient, message.as_string())
  smtp_server.quit()