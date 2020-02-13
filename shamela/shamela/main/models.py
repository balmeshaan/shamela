from django.db import models
from datetime import datetime
# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class AurthorsPro(models.Model):
    name = models.CharField(max_length=300)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)
    detail_about_aurthor = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Aurthors'


class Publishers(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Publishers'
        

class Books(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True)
    aurthor = models.ForeignKey(AurthorsPro, on_delete=models.SET_NULL, null=True)
    publisher = models.ForeignKey(Publishers, on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True, blank=True)
    book_file = models.FileField(upload_to='books/%Y/%m/%d', null=True, blank=True)
    phone_book_file = models.FileField(upload_to='phone_books/%Y/%m/%d', null=True, blank=True)
    edition = models.CharField(max_length=200, null=True, blank=True)
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Books'


class UserBooks(models.Model):
    APPROVED = '1'
    PENDING = '0'
    BOOK_CHOICES = [
        (APPROVED, 'Approved'),
        (PENDING, 'Pending'),
    ]
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True, blank=True)
    aurthor = models.ForeignKey(AurthorsPro, on_delete=models.SET_NULL, null=True, blank=True)
    publisher = models.ForeignKey(Publishers, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    book_file = models.FileField(upload_to='Uploaded_by_users/%Y/%m/%d', null=True)
    edition = models.CharField(max_length=200, null=True, blank=True)
    views = models.IntegerField(default=0)
    status = models.CharField(
        max_length=1,
        choices=BOOK_CHOICES,
        default=PENDING,
    )
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'User Books'