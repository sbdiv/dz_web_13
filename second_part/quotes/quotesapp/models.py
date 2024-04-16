from django.db import models

class Author(models.Model):
    fullname = models.CharField(max_length=100)
    born_date = models.CharField(max_length=20)
    born_location = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.fullname

class Quote(models.Model):
    tags = models.ManyToManyField('Tag', related_name='quotes')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    quote = models.TextField()

    def __str__(self):
        return f'"{self.quote}" - {self.author.fullname}'

class Tag(models.Model):
    name = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.name
