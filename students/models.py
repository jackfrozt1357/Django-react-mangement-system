from django.db import models

# stu_email=student email
#signed_in_at = time student sgned into the hostel
#room_number = room of student i.e A202
#hall = Building where student room is located i.e  Paul hall,Massachusetts Hall
class models(models.Model):
    first_name=models.CharField("First name",max_length=20)
    last_name=models.CharField("Last name ",max_length=20)
    stu_email=models.EmailField()
    phone=models.CharField(max_length=11)
    room_number=models.TextField(blank=True,null=True)
    hall=models.TextField(blank=True,null=True)
    signed_in_at=models.DateTimeField("Signed in at",auto_now_add=True)


    def _str_(self):
        return self.first_name


