#'''
import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host = 'smtp.xxx.com'
mail_user = 'xxxx'
mail_pass = 'xxxxxx'


sender = 'from@runoob.com'
receivers = ['284953505@qq.com']

message = MIMEText('失智测试...', 'plain', 'utf-8')
message['From'] = Header('只怕是失了智', 'utf-8')
message['To'] = Header("失智测试", 'utf-8')

subject = '失智邮件测试'
message['subject'] = Header(subject, 'utf-8')

try:
	smtpObj = smtplib.SMTP()
	smtpObj.connect(mail_host,25)
	smtpObj.login(mail_user, mail_pass)
	smtpObj.sendmail(sender, receivers, message.as_string())
	print("嗨，你失了智么")
except smtplib.SMTPException:
	print("果然失了智，这都收不到")
#'''
'''
import sys,smtplib

fromaddr = raw_input("From:傻子")
toaddrs = raw_input("To:憨子").split(',')
print("Enter message, end with ^D:")
msg='傻逼吧'
while 1:
	line = sys.stdin.readline()
	if not line:
		break
msg = msg + line
server = smtplib.SMTP('localhost')
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
'''

from email import encoders
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr,formataddr
import smtplib


def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr((Header(name,'utf-8').encode(),addr))

from_addr = input('From:')
password = input('Password:')
to_addr = input('To:')
smtp_server = input('SMTP server')


message = MIMEText('失智测试...', 'plain', 'utf-8')
message['From'] = _format_addr('只怕是失了智:{}'.format(from_addr))
message['To'] = _format_addr("失智测试:{}".format(to_addr))
message['Subject'] = Header('来自傻子的问候...','utf-8').encode()



try:
	smtpObj = smtplib.SMTP(smtp_server,25)
	smtpObj.set_debuglevel(1)
	smtpObj.login(from_addr, password)
	smtpObj.sendmail(from_addr, [to_addr], message.as_string())
	print("嗨，你失了智么")
	server.quit()
except smtplib.SMTPException:
	print("果然失了智，这都收不到")
'''