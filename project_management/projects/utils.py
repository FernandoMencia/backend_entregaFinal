from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User

def send_notification(subject, message, recipient_list):
    print(f"Subject: {subject}")
    print(f"Message: {message}")
    print(f"To: {', '.join(recipient_list)}")

def get_all_user_emails():
    return list(User.objects.values_list('email', flat=True))


"""
En esta aplicación la función send_notification simplemente imprime los emails para 
mostrarlos por consola como está configurado en settings.

Para mandarlos realmente usando la función send_email, se podría usar:

def send_notification(subject, message, recipient_list):
    try:
        # Envia el correo utilizando send_mail
        
        send_mail(subject, message, from_email=None, recipient_list=recipient_list, fail_silently=False)
        
        # Imprime un mensaje de éxito en la consola si el correo se envió correctamente
        
        print(f"Notification email sent to: {', '.join(recipient_list)}")
    except Exception as e:
    
        # Captura cualquier excepción que pueda ocurrir durante el envío del correo
        print(f"Failed to send notification email: {str(e)}")

"""