from django.db import models

# Create your models here.


# Create your models here.
 
class GoodsTest(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
