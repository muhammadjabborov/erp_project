from django.db.models import PositiveIntegerField, DecimalField, CharField

from apps.common.models import BaseModel


class Inventory(BaseModel):
    title = CharField(max_length=255)
    quantity = PositiveIntegerField(default=0)
    price = DecimalField(max_digits=10, decimal_places=6)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Inventory"
        verbose_name_plural = "Inventory"
