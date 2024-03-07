from django.db import models


class ClientRecord(models.Model):
    
    PROGRESS_CHOICES = [
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('finished', 'Finished'),
    ]
    
    creation_date = models.DateTimeField(auto_now_add=True)
    
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=255)
    country= models.CharField(max_length=125)
    company_name = models.CharField(max_length=300)
    work_info = models.TextField()
    start_date = models.DateTimeField()
    current_status = models.CharField(max_length=20, choices=PROGRESS_CHOICES, default='not_started')
    progress_percentage = models.CharField(max_length=100)
    delivery_date = models.DateTimeField()
    deal_amount = models.FloatField()
    
    def __str__(self):
        
        return self.first_name + '   ' + self.last_name
    
    
    
    
