# Sending a Email 
import smtplib
from email.message import EmailMessage
sender = "shravanpitla180@gmail.com"
password = "xuwz kfsl wtxa vsqv"
receiver = "shravankumarpitla18@gmail.com"

msg = EmailMessage()
msg["subject"] = "Preparation Email"
msg["from"]=sender
msg["To"]=receiver
msg.set_content("Hello.This is a preparation email using Python")
with smtplib.SMTP_SSL("smtp.gmail.com",465)as server:
# SMPT_SSL --> connects to Gmail's SMPT server using port 465
    server.login(sender, password)
    # login()-->Log in using your Email and app password
    server.send_message(msg)
    #send_message()-->sends the email
print("Email sent Successfully")

# Attached a File or Word Document
import smtplib
from email.message import EmailMessage
sender = "shravanpitla180@gmail.com"
password = "xuwz kfsl wtxa vsqv"
receiver = "shravankumarpitla18@gmail.com"

msg = EmailMessage()
msg["subject"] = "Preparation Email"
msg["from"]=sender
msg["To"]=receiver
msg.set_content("Hello.This is a preparation email using Python")
# Attach a PDF or Word Document
file_path = r"C:\Users\Shravan Kumar\Downloads\Shravan Resume-2026.pdf"
with open(file_path, "rb")as file:
    file_data = file.read()

msg.add_attachment(
    file_data,
    maintype="application",
    subtype="pdf",
    filename="Shravan Resume-2026.pdf"
)
with smtplib.SMTP_SSL("smtp.gmail.com",465)as server:
# SMPT_SSL --> connects to Gmail's SMPT server using port 465
    server.login(sender, password)
    # login()-->Log in using your Email and app password
    server.send_message(msg)
    #send_message()-->sends the email
print("Email sent Successfully")

# Virtual Assessment 
import datetime
import webbrowser

print("Hello! I'm your Virtual Assistant.")

while True:
  command = input("\nHow may I help you ").lower()

  if "hello" in command or "hi" in command:
    print("Hello Vikas! How are you?")
  elif "time" in command:
    time = datetime.datetime.now().strftime("%I:%M %p")
    print("Current time is: ", time)
  elif "date" in command:
    date = datetime.datetime.now().strftime("%d-%m-%Y")
    print("Today's date is: ", date)
  elif "open google" in command:
    webbrowser.open("https://www.google.com")
    print("Opening Google....")
  elif "your name" in command:
    print("I am your Python Virtual Assistant")
  elif "exit" in command or "bye" in command:
    print("Goodbye! Have a nice day")
    break
  else:
    print("Sorry, I don't understand that command.")