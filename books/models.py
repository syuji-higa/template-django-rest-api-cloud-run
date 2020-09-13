from adminsortable.models import SortableMixin
from django.db import models


class Publisher(models.TextChoices):
    SHOEISHA = "翔泳社", "翔泳社"
    GIJYUTSU_HYORONSHA = "技術評論社", "技術評論社"
    SHUWA_SYSTEM = "秀和システム", "秀和システム"
    SB_CREATIVE = "SBクリエイティブ", "SBクリエイティブ"
    NIKKE_BP = "日経BP", "日経BP"


class Book(SortableMixin):
    isbn = models.CharField(verbose_name="ISBNコード", max_length=20)
    title = models.CharField(verbose_name="署名", max_length=100)
    price = models.IntegerField(verbose_name="価格", default=0)
    publisher = models.CharField(
        verbose_name="出版社", max_length=50, choices=Publisher.choices
    )
    published = models.DateField(verbose_name="刊行日")

    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    class Meta:
        ordering = ["the_order"]

    def __str__(self):
        return self.title
