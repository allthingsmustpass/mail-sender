import smtplib

def validate_credentials(smpt_username, smpt_password):
    try:
        smpt_server = 'smtp.gmail.com'
        smpt_port = 587
        with smtplib.SMTP(smpt_server, smpt_port) as server:
            server.starttls()
            server.login(smpt_username, smpt_password)
        return True
    except smtplib.SMTPAuthenticationError:
        return False
