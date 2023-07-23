from django.db import models
from django.urls import reverse


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name


class Quiz(models.Model):
    name = models.CharField(max_length=255)
    # db_index означает, что поле индексируемое и поиск будет чуть быстрее
    # То, по какому полю будет автозаполняться слаг, необходимо указать в admin.py
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    description = models.TextField(blank=True)
    # Для того чтобы фото норм работало, см. settings
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=False)
    # auto now add означает, что значение time create для каждой
    # записи будет определенно один раз - в момент создания
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    cat = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    def get_absolute_url(self, ):
        return reverse('quiz', kwargs={'test_slug': self.slug})


class Questions(models.Model):
    question = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.PROTECT)

    def __str__(self):
        return self.question


class Answers(models.Model):
    answer = models.CharField(max_length=255)
    is_right = models.BooleanField()
    question = models.ForeignKey(Questions, on_delete=models.PROTECT)

    def __str__(self):
        return self.answer
