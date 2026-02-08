class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

emails = []
input_line = input()

while not input_line == "Stop":
    sender, receiver, content = input_line.split()
    email = Email(sender, receiver, content)
    emails.append(email)
    input_line = input()

indexes = [int(i) for i in input().split(", ")]

for index in indexes:
    emails[index].send()

for email in emails:
    print(email.get_info())