from utils.config import email_password, email_address
import smtplib, ssl #security auth
from email.mime.multipart import MIMEMultipart #email structure
from email.mime.text import MIMEText #email body
from fastapi import HTTPException, status

class Email_repo:

    def _init_(self):
        self.website_url = "speakap.com"
        self.my_linkedin = "https://www.linkedin.com/in/noelia-rodr%C3%ADguez-morales-/"
        self.from_addr = email_address
        self.password = email_password
        self.location = "Pedro de Medinalaan 5, 1086 XK Amsterdam"
        self.powered_by = "Noe :)"
    
    # Entry point for sending emails
    def send_email_to_user(self, to: str, subject: str, greeting: str, body_1: str, body_2: str):
        # create email data
        body = self.email_body(greeting, body_1, body_2)

        # send email to user
        self.send_email(body, subject, to)
        return body
    
    # Methode that send email
    def send_email(self, body: str, subject: str, to: str):

        # Create email
        msg = MIMEMultipart("alternative")
        msg.add_header('from', self.from_addr)
        msg.add_header('to', to)
        msg.add_header('subject', subject)

        part = MIMEText(body, "html")
        msg.attach(part)

        context = ssl.create_default_context()

        # send email
        server = smtplib.SMTP(host='smtp.gmail.com', port=465)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(self.from_addr, self.password)
        server.send_message(msg, from_addr=self.from_addr, to_addrs=[to])

    # Methode thta createds body
    def email_body(self, greeting: str, body_1: str, body_2: str):
        return f"""
            <!doctype html>
            <html>
              <body style="background-color: #f6f6f6; font-family: sans-serif; -webkit-font-smoothing: antialiased; font-size: 14px; line-height: 1.4; margin: 0; padding: 0; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;">
                <table role="presentation" border="0" cellpadding="0" cellspacing="0" class="body" style="border-collapse: separate; mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #f6f6f6; width: 100%;" width="100%" bgcolor="#f6f6f6">
                  <tr>
                    <td style="font-family: sans-serif; font-size: 14px; vertical-align: top;" valign="top">&nbsp;</td>
                    <td class="container" style="font-family: sans-serif; font-size: 14px; vertical-align: top; display: block; max-width: 580px; padding: 10px; width: 580px; margin: 0 auto;" width="580" valign="top">
                      <div class="content" style="box-sizing: border-box; display: block; margin: 0 auto; max-width: 580px; padding: 10px;">
                        <table role="presentation" class="main" style="border-collapse: separate; mso-table-lspace: 0pt; mso-table-rspace: 0pt; background: #ffffff; border-radius: 3px; width: 100%;" width="100%">
                          <tr>
                            <td class="wrapper" style="font-family: sans-serif; font-size: 14px; vertical-align: top; box-sizing: border-box; padding: 20px;" valign="top">
                              <table role="presentation" border="0" cellpadding="0" cellspacing="0" style="border-collapse: separate; mso-table-lspace: 0pt; mso-table-rspace: 0pt; width: 100%;" width="100%">
                                <tr>
                                  <td style="font-family: sans-serif; font-size: 14px; vertical-align: top;" valign="top">
                                    <p style="font-family: sans-serif; font-size: 14px; font-weight: normal; margin: 0; margin-bottom: 15px;">{greeting}</p>
                                    <p style="font-family: sans-serif; font-size: 14px; font-weight: normal; margin: 0; margin-bottom: 15px;">{body_1}</p>
                                    <p style="font-family: sans-serif; font-size: 14px; font-weight: normal; margin: 0; margin-bottom: 15px;">{body_2}</p>
                                    <p style="font-family: sans-serif; font-size: 14px; font-weight: normal; margin: 0; margin-bottom: 15px;">Kind regards, </p>
                                    <p style="font-family: sans-serif; font-size: 14px; font-weight: normal; margin: 0; margin-bottom: 15px;"> Speakap</p>
                                  </td>
                                </tr>
                              </table>
                            </td>
                          </tr>
                        </table>
                        <div class="footer" style="clear: both; margin-top: 10px; text-align: center; width: 100%;">
                          <table role="presentation" border="0" cellpadding="0" cellspacing="0" style="border-collapse: separate; mso-table-lspace: 0pt; mso-table-rspace: 0pt; width: 100%;" width="100%">
                            <tr>
                              <td class="content-block" style="font-family: sans-serif; vertical-align: top; padding-bottom: 10px; padding-top: 10px; color: #999999; font-size: 12px; text-align: center;" valign="top" align="center">
                                <span class="apple-link" style="color: #999999; font-size: 12px; text-align: center;">{self.location}</span>
                              </td>
                            </tr>
                            <tr>
                              <td class="content-block powered-by" style="font-family: sans-serif; vertical-align: top; padding-bottom: 10px; padding-top: 10px; color: #999999; font-size: 12px; text-align: center;" valign="top" align="center">
                                Powered by <a href="{self.my_linkedin}" style="color: #999999; font-size: 12px; text-align: center; text-decoration: none;">{self.powered_by}</a>.
                              </td>
                            </tr>
                          </table>
                        </div>
                      </div>
                    </td>
                  </tr>
                </table>
              </body>
            </html>
                """