from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    project_image = models.CharField(max_length=200)
    story = models.TextField()
    team = models.TextField()
    goal = models.TextField()
    results = models.TextField()
    documents = models.TextField()
    contact = models.TextField()
    media = models.TextField()
    earned = models.IntegerField()
    count_donors = models.IntegerField()
    funding_needed = models.IntegerField()

    def __unicode__(self):
        return self.name

class News(models.Model):
    news_date = models.DateField()
    text = models.TextField()
    project = models.ForeignKey(Project)

    def __unicode__(self):
        return self.text

class Post(models.Model):
    author = models.CharField(max_length=100)
    message = models.TextField()
    mail = models.EmailField()
    project = models.ForeignKey(Project)

    def __unicode__(self):
        return self.author

class Donor(models.Model):
    name = models.CharField(max_length=100)
    money = models.IntegerField()
    project = models.ForeignKey(Project)
    email = models.EmailField()

    def __unicode__(self):
        return self.name