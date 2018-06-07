import sendgrid
from sendgrid.helpers.mail import Email, Mail, Content

API_KEY = '520121'
SUBJECT = 'Welcome'
BODY = 'Hi {}'

sg = sendgrid.SendGridAPIClient(apikey=API_KEY)


def send_email(email, name):
    from_email = Email("15751005410@q139.com")
    to_email = (email)
    subject = "Welcome"
    content = Content("text/plain", BODY.format(name))
    mail = Mail(from_email, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    send_email('somebody@gmail.com', 'Some Body')
    print('Done')
