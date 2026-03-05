
# Email sender stub (fill credentials to use)
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path

def send_email(subject: str, html_path: Path, to_email: str, from_email: str, smtp_host: str, smtp_port: int, username: str, password: str):
    html = Path(html_path).read_text(encoding="utf-8")
    msg = MIMEMultipart("alternative"); msg["Subject"]=subject; msg["From"]=from_email; msg["To"]=to_email
    msg.attach(MIMEText(html, "html"))
    with smtplib.SMTP_SSL(smtp_host, smtp_port, context=ssl.create_default_context()) as server:
        server.login(username, password); server.sendmail(from_email, [to_email], msg.as_string())
