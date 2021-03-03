from django.db import models


class Level(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return "%s" % (self.name)

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return "%s" % (self.name)

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    def __str__(self):
        return "%s" % (self.name)


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100,default="asd")
    level = models.ForeignKey(Level,on_delete = models.CASCADE)
    real_price = models.FloatField(default=1)
    price = models.FloatField(default=1)
    discount = models.FloatField(default=1)
    course_score = models.FloatField(default=1)
    users = models.IntegerField(default=1)
    category = models.ForeignKey(Category,related_name='category',on_delete = models.CASCADE)
    sub_category = models.ForeignKey(Category,related_name='sub_category',on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher,on_delete = models.CASCADE)

    def __str__(self):
        return "%s" % (self.name)
