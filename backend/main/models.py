from django.db import models

# Create your models here.
class News(models.Model):
    id = models.AutoField(primary_key=True) 
    title = models.CharField(max_length=255)
    img_href = models.URLField()
    content = models.TextField()
    news_href = models.URLField(unique=True)
    display = models.BooleanField(default=False)
    published_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "news"
        ordering = ['-published_at'] 