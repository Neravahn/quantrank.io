import smtplib
from email.mime.text import MIMEText
import random
import os





SENDER_EMAIL = os.getenv("SENDER_EMAIL")
APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")


def generate_otp():
    return str(random.randint(100000, 999999))

def send_otp(receiver_email):
    otp = generate_otp()

    msg = MIMEText(f"""
    <html>
  <body style="margin:0; padding:0; background:#ffffff; font-family: Arial, Helvetica, sans-serif;">

    <div style="max-width:600px; margin:30px auto; padding:20px;">

      <div style="
        background:black;
        padding:30px;
        border-radius:10px;
        border:1px solid rgb(255, 183, 0);
        width:500px;
        margin:0 auto;
        text-align:center;
      ">

        <div style="
          margin-bottom:25px;
          border-radius:15px;
          background:rgb(255, 183, 0);
          color:black;
          width:350px;
          margin-left:auto;
          margin-right:auto;
          padding:10px 0;
        ">
          <h2 style="
            margin:0;
            color:black;
            font-weight:600;
            letter-spacing:0.5px;
          ">
            Email Verification
          </h2>
        </div>

        <div style="
          font-size:15px;
          color:white;
          line-height:1.6;
        ">
          <p>
            A request was made to create an account on <strong>QuantRank</strong>
            using this email address.
          </p>

          <p>
            Please use the One Time Password below to verify your email:
          </p>

          <h2 style="
            color:rgb(255, 183, 0);
            letter-spacing:3px;
            margin:20px 0;
          ">
            {otp}
          </h2>

          <p>
            This OTP is valid for a limited time. Do not share this code with anyone.
          </p>

          <p>
            If you did not initiate this request, you may safely ignore this email.
          </p>

          <p style="margin-top:25px;">
            Regards,<br>
            <strong>QuantRank</strong>
          </p>
        </div>

      </div>

      <div style="
        background:#ffffff;
        margin-top:15px;
        padding:15px;
        border-radius:8px;
        text-align:center;
        font-size:13px;
        color:#777777;
        border-top:1px solid rgb(255, 183, 0);
      ">
        <p style="margin:6px 0;">
          Built by <strong>Prashant</strong> for <strong>Axiom</strong>
        </p>
        <p style="margin:6px 0;">
          © QuantRank
        </p>
      </div>

    </div>

  </body>
</html>

    """, 'html')

    msg['Subject'] = "Email Verification"
    msg['From'] = SENDER_EMAIL
    msg['To'] = receiver_email


    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_email, msg.as_string())
        server.quit()
        return otp
    
    except Exception as e:
        return None
    


send_otp('prashantc48774.r@gmail.com')