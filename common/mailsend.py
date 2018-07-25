""" SendMail        类发送邮件和发送表格邮件用
    sendmail        发邮件
    senddataframe   发表格邮件
    20180725 by pengke
"""

import smtplib
from email.mime.text import MIMEText
from email.header import Header


class SendMail(object):
    def __init__(self, host, port, user, password, withssl=True):
        self._user = user
        self._smtp = smtplib.SMTP(host, port)
        if withssl:
            self._smtp.ehlo()
            self._smtp.starttls()
            self._smtp.login(user, password)

    def sendmail(self, sender, mailto, mailcc, subject, text, encoding='utf-8'):
        message = MIMEText(text, _subtype='html', _charset=encoding)
        message['From'] = self._user if not sender else str(Header(sender, encoding)) + '<' + self._user + '>'
        message['Subject'] = Header(subject, encoding)
        message['To'] = ';'.join(mailto)
        if mailcc:
            message['CC'] = ';'.join(mailcc)
        self._smtp.sendmail(self._user, mailto + mailcc, message.as_string())

    def senddataframe(self, sendername, mailto, mailcc, subject, data, width=500, encoding='utf-8'):
        texts = list()
        texts.append('<style>.table-a table{border-right:1px solid #777;border-bottom:1px solid #777} '
                     '.table-a table td,th{border-left:1px solid #777;border-top:1px solid #777}  '
                     '.table-a table th{background-color:#3F3F3F;color:#fff;text-align:left;vertical-align:baseline;}'
                     '.table-a table{font-size:10pt;}'
                     '</style>')
        texts.append('<div class="table-a"><table border="0" cellspacing="0" cellpadding="0" width="'+str(width)+'px">')
        texts.append('<tr>')
        for col in data.columns:
            texts.append('<th>' + col + '</th>')
        texts.append('</tr>')
        for i in range(data.shape[0]):
            texts.append('<tr>')
            for j in range(data.shape[1]):
                texts.append('<td>' + data.iloc[i][j] + '</td>')
            texts.append('</tr>')
        texts.append('</table></div>')
        text = ''.join(texts)
        self.sendmail(sendername, mailto, mailcc, subject, text, encoding)
        print(text)

    def __del__(self):
        try:
            self._smtp.close()
        finally:
            pass


if __name__ == '__main__':
    import pandas as pd
    mailhost = 'mail.googgggle.net'
    mailport = 465
    mailuser = 'yoyoxixi@googgggle.net'
    mailpasswd = 'yoxipasswd'
    receiveto = ['yoyoxixi@googgggle.net']
    reveicecc = ['xixiyoyo@googgggle.net']
    title = '测试邮件，不要回复,不要回复,不要回复'
    dataf = pd.read_csv('testmail.csv', encoding='gbk')
    mail = SendMail(mailhost, mailport, mailuser, mailpasswd)
    mail.senddataframe('哟西', receiveto, reveicecc, title, dataf, 800)
