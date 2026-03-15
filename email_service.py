import smtplib
from email.message import EmailMessage
import os

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
SECRETARY_EMAIL = os.getenv("SECRETARY_EMAIL")


def send_email(event_title, docx_bytes):

    msg = EmailMessage()

    msg["Subject"] = f"Event Report — {event_title}"
    msg["From"] = SENDER_EMAIL
    msg["To"] = SECRETARY_EMAIL

    msg.set_content(
        f"Please find attached the report for event: {event_title}"
    )

    msg.add_attachment(
        docx_bytes,
        maintype="application",
        subtype="vnd.openxmlformats-officedocument.wordprocessingml.document",
        filename=f"{event_title}.docx"
    )

    with smtplib.SMTP("smtp.gmail.com",587) as server:

        server.starttls()

        server.login(SENDER_EMAIL,SENDER_PASSWORD)

        server.send_message(msg)