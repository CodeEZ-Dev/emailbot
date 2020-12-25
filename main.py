import smtplib
import speech_recognition as sr
import pyttsx3

from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass

def sendEmail(receiver,subject,body):
    '''
    this function get email id and password validate these two and send auto email to 
    "To" email id
    funtion using SMTP server, validating gmail server to send email
    '''
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('muralidharan1307@gmail.com','murali@123')
    email = EmailMessage()
    email['From'] = 'muralidharan1307@gmail.com'
    email ['To'] = receiver
    email['Subject'] =subject
    email.set_content(body)
    server.send_message(email)
    

email_list ={
    'tara':'muralidharan1307@gmail.com',
    'dude':'muralidharan1307@gmail.com',
    'sai':'muralidharan1307@gmail.com',
    'sai ashwanth':'muralidharan1307@gmail.com',
    'saradha':'muralidharan1307@gmail.com'
}

def get_email_info():
    talk('To Whom you want to a send email')
    name=get_info()
    receiver = email_list[name]
    print(receiver)
    talk('what is the subject of your email?')
    subject =get_info()
    talk('Tell me body to write here')
    body = get_info()
    sendEmail(receiver,subject,body)
    talk('Your Email sent to '+name)
    talk("Do you want to send more email?")
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()

get_email_info()