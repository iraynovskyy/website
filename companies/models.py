from django.db import models


class Stock(models.Model):
    ticker = models.CharField(max_length=10)                               # facebook is fb , yahoo is yhoo
    open = models.FloatField()
    close = models.FloatField()
    volume = models.IntegerField()

    def __str__(self):      # we want to have a string representation of this
        return self.ticker