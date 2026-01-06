import datetime
from django.db import models
from django.utils import timezone

class QRCode(models.Model):
    input_text = models.CharField(max_length=200)
    qr_code_img = models.ImageField(upload_to='qr_codes/')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.input_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <=self.pub_date <= now
