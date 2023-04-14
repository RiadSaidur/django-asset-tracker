from django.db import models

from company.models import Company


class Employee(models.Model):
  name = models.CharField(max_length=100)
  company = models.ForeignKey(to=Company, on_delete=models.CASCADE)

  def __str__(self) -> str:
    return f'{self.company} - {self.name}'