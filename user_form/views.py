from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserForm
from .serializers import UserFormSerializer
from django.core.mail import send_mail
from django.conf import settings
class UserFormAPIView(APIView):
    def post(self, request):
        serializer = UserFormSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            
            # Send email to form submitter
            subject = 'Thank you for submitting the form'
            message = 'Dear {},\nThank you for submitting the form.'.format(instance.name)
            from_email = settings.EMAIL_HOST_USER  # Replace with your email address
            to_email = [instance.email]
            send_mail(subject, message, from_email, to_email)

            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def get(self, request):
        queryset = UserForm.objects.all()
        serializer = UserFormSerializer(queryset, many=True)
        return Response(serializer.data)
