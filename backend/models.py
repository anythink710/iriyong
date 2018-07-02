from django.db import models

# from backend.models import SecretKey
class SecretKey(models.Model):
    id = models.IntegerField(primary_key=True)
    secret_key = models.TextField()
    class Meta:
        managed = False
        db_table = 'iriyong_secretkey'
