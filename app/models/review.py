from app.models.spot import Spot
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.deletion import CASCADE


class Review(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=CASCADE,
        verbose_name='ユーザ',
    )

    spot = models.ForeignKey(
        Spot,
        on_delete=CASCADE,
        verbose_name='スポット',
    )

    star = models.IntegerField(
        choices=(
            (1, '星1'),
            (2, '星2'),
            (3, '星3'),
            (4, '星4'),
            (5, '星5'),
        ),
        default=5,
        verbose_name='評価',
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
        return f'{self.user.pk}-{self.spot.pk}-{self.star}'

    class Meta:
        verbose_name_plural = 'レビュー'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'spot'],
                name='unique_review',
            ),
        ]
