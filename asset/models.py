from django.db import models

from employee.models import Employee


class Asset(models.Model):
  name = models.CharField(max_length=100)
  checked_out = models.DateTimeField()
  returned = models.DateTimeField(null=True, blank=True)
  hand_out_condition = models.TextField()
  returned_condition = models.TextField(null=True, blank=True)
  employee = models.ForeignKey(to=Employee, on_delete=models.CASCADE)

  def __str__(self) -> str:
    return f'{self.employee} - {self.name}'