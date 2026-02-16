import streamlit as st
import re
import zipfile
import smtplib
import os
from email.message import EmailMessage
from pathlib import Path
import importlib.util

# IMPORT YOUR PROGRAM 1 FUNCTION
# module name starts with a digit so import from file location
module_path = Path(__file__).parent / "102303112.py"
spec = importlib.util.spec_from_file_location("mashup_module", str(module_path))
mashup_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mashup_module)
create_mashup = mashup_module.create_mashup

EMAIL_REGEX = r"[^@]+@[^@]+\.[^@]+"
EMAIL_SENDER = "adishfab@gmail.com"

st.title("Mashup Generator")

singer = st.text_input("Singer Name")
videos = st.number_input("# of videos", min_value=11, value=20)
duration = st.number_input("Duration of each video (sec)", min_value=21, value=30)
email = st.text_input("Email ID")

if st.button("Submit"):

    if not singer or not email:
        st.error("All fields are required")
        st.stop()

    if not re.match(EMAIL_REGEX, email):
        st.error("Invalid Email ID")
        st.stop()

    PASSWORD = os.environ.get("Password of mail")

    if not PASSWORD:
        st.error("Environment variable 'Password' not found")
        st.stop()

    try:
        output = "output.mp3"

        st.info("Creating mashup...")
        create_mashup(singer, int(videos), int(duration), output)

        zipname = "result.zip"
        with zipfile.ZipFile(zipname, "w") as z:
            z.write(output)

        msg = EmailMessage()
        msg["Subject"] = "Your Mashup File"
        msg["From"] = EMAIL_SENDER
        msg["To"] = email
        msg.set_content("Attached is your mashup zip file.")

        with open(zipname, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype="application",
                subtype="zip",
                filename=zipname
            )

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_SENDER, PASSWORD)
            server.send_message(msg)

        st.success("Mashup created and emailed successfully!")

    except Exception as e:
        st.error(f"Error: {e}")
