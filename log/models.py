from django.db import models

class our_users(models.Model):
    
    user_name = models.TextField(max_length=50, primary_key=True)
    user_id = models.TextField(max_length=50)
    user_password = models.TextField(max_length=8)