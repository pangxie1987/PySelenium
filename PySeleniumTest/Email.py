#-*- coding:utf-8 -*-
'''
调用邮箱服务器，发送邮件
'''
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

smtpserver='smtp-mail.outlook.com' #发送服务器
port='587'
#user='m18516292278@163.com'
user='lpb.waln@outlook.com'  #发送邮箱用户
passwd='Lpb201212'

sender='lpb.waln@outlook.com' #发送邮箱地址

reverser='m18516292278@163.com'  #接收邮箱
subject='Python Mail Test with attach-邮件主题!'  #主题中带中文的，则发件人名称正常

#邮件内容
msg=MIMEText('<html><h1>你好!</h1></html>','html','utf-8')
msg['Subject']=Header(subject,'utf-8')

#添加附件
filename='geckodriver.log'
sendfile=open('geckodriver.log','rb').read()
att=MIMEText(sendfile,'base64','utf-8')
att["Content-Type"]='application/octet-stream'
att['Content-Disposition']='attchment;filename=%s'%filename.encode('gb2312')
msgRoot=MIMEMultipart('related','utf-8')
msgRoot['Subject']=subject
msgRoot.attach(att)

smtp=smtplib.SMTP()

smtp.connect(smtpserver,port)  #使用port
smtp.starttls() #SMTP 加密方法 STARTTLS  解决加密问题
smtp.ehlo()
smtp.login(user,passwd)
smtp.sendmail(sender,reverser,msgRoot.as_string())
smtp.quit()
print('Email send Sucess!')