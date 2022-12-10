from django.db import models

# Create your models here.


class Category(models.Model):
    cat_title = models.CharField( max_length=50)

    def __str__(self) -> str:
        return self.cat_title


class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    content = models.TextField()
    createdAt = models.DateTimeField( auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True )

    def __str__(self) -> str:
        return self.title
    