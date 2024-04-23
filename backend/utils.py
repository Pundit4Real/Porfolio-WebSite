from django.core.mail import EmailMessage


class EmailSender:
    
    def send_mail(self, data):
        email = EmailMessage(
            subject=data['email_subject'],
            body=data['email_body'],
            to=[data['to_email']],
        )
        email.send()
    
    def send_client_email(self, client):

        email = 'mohammedaalli088@gmail.com'
        message = f"Message from: {client.first_name} {client.last_name}\nEmail: {client.email}\nPhone: {client.phone}\n\n{client.message}"
        data = {
            'email_subject': client.service,
            'email_body': message,
            'to_email': email
        }
        self.send_mail(data)
        return True
