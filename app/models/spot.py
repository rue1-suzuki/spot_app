from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.deletion import CASCADE


class Spot(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=CASCADE,
        verbose_name='作成ユーザ',
    )

    title = models.CharField(
        max_length=128,
        verbose_name='名前',
    )

    text = models.TextField(
        blank=True,
        null=True,
        max_length=128,
        verbose_name='内容',
    )

    prefecture = models.IntegerField(
        choices=(
            (1, '北海道'),
            (2, '青森県'),
            (3, '岩手県'),
            (4, '秋田県'),
            (5, '宮城県'),
            (6, '山形県'),
            (7, '福島県'),
            (48, '不明・その他・海外'),
        ),
        verbose_name='都道府県',
    )

    address = models.CharField(
        blank=True,
        null=True,
        max_length=128,
        verbose_name='住所',
    )

    image = models.ImageField(
        blank=True,
        null=True,
        verbose_name='イメージ画像',
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='作成日時',
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='更新日時',
    )

    def __str__(self):
        return self.title

    def count_review(self):
        from app.models import Review
        reviews = Review.objects.filter(spot=self)
        return len(reviews)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'prefecture'],
                name="unique_spot",
            ),
        ]
        verbose_name_plural = 'スポット'
