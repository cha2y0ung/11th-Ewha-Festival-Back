from django.db import models
from account.models import User


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Day(models.Model):
    DAY_CHOICES = (
        ('수요일', '수요일'),
        ('목요일', '목요일'),
        ('금요일', '금요일'),
    )
    DATE_CHOICES = (
        (10, 10),
        (11, 11),
        (12, 12),
    )

    day = models.CharField(choices=DAY_CHOICES, max_length=5)
    date = models.IntegerField(choices=DATE_CHOICES)

    def __str__(self):
        return f'{self.day}'

class Category(models.Model):
    CATEGORY_CHOICES = (
        ('음식', '음식'),
        ('굿즈', '굿즈'),
        ('체험', '체험'),
        ('기타', '기타'),
    )

    category = models.CharField(choices=CATEGORY_CHOICES, max_length=5)

    def __str__(self):
        return f'{self.category}'


class Booth(TimeStamp):
    COLLEGE_CHOICES = (
        ('교육관', '교육관'),
        ('대강당', '대강당'),
        ('신세계관', '신세계관'),
        ('생활관', '생활관'),
        ('정문', '정문'),
        ('포스코관', '포스코관'),
        ('학문관', '학문관'),
        ('휴웃길', '휴웃길')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.ManyToManyField(Day, related_name='booths')
    college = models.CharField(choices=COLLEGE_CHOICES, max_length=20)
    category = models.ManyToManyField(Category, related_name='booths')
    name = models.TextField()
    number = models.CharField(max_length=10, blank=True)
    thumnail = models.TextField(null=True, blank=True)
    opened = models.BooleanField(default=False)
    hashtag = models.TextField(null=True, blank=True)
    description = models.TextField(blank=True)
    like = models.ManyToManyField(User, related_name='booths', blank=True)

    def __str__(self):
        return self.name


class Image(TimeStamp):
    booth = models.ForeignKey(Booth, on_delete=models.CASCADE, related_name='images')
    image = models.TextField()


class Menu(TimeStamp):
    booth = models.ForeignKey(Booth, on_delete=models.CASCADE, related_name='menus')
    menu = models.TextField()
    price = models.PositiveIntegerField()
    is_soldout = models.BooleanField(default=False)


class Comment(TimeStamp):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    booth = models.ForeignKey(Booth, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()

class Notice(TimeStamp):
    booth = models.ForeignKey(Booth, on_delete=models.CASCADE, related_name='notices')
    content = models.TextField()

class Time(TimeStamp):
    booth = models.ForeignKey(Booth, on_delete=models.CASCADE, related_name='times')
    time = models.TextField()