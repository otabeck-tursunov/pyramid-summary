from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    pay = models.FloatField()

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=255)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    connection = models.JSONField(null=True, blank=True)
    stage = models.IntegerField(default=1)
    person = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='followers')

    def __str__(self):
        return f'{self.name} - {self.status}'

