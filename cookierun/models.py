from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models


class Character(models.Model):
    RATING = (
        ("S", "S-class"),
        ("A", "A-class"),
        ("B", "B-class"),
        ("C", "C-class"),
        ("L", "L-class"),
    )
    name = models.CharField(
        max_length=100,
        db_index=True,
        validators=[
            MinLengthValidator(3),
            RegexValidator(r"[ㄱ-힣]", message="한글을 입력해주세요."),
        ],
    )
    foreign_name = models.CharField(max_length=100, blank=True)
    rating = models.CharField(max_length=1, choices=RATING)
    pet = models.CharField(max_length=50, blank=True)
    price = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    photo = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
