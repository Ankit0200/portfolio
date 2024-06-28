from django.db import models

class Project(models.Model):
    Name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='project_img')
    git_url = models.CharField(max_length=100, default="none")

    live_demo_url = models.CharField(max_length=100, null=True)



class TECH_KNOWLEDGE(models.Model):
    Name = models.CharField(max_length=200)
    level=models.CharField(max_length=100)

