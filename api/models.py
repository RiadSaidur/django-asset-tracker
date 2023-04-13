from django.db import models

class Company(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self) -> str:
    return self.name


class Employee(models.Model):
  name = models.CharField(max_length=100)
  company = models.ForeignKey(to=Company, on_delete=models.CASCADE)

  def __str__(self) -> str:
    return f'{self.company} - {self.name}'


class Asset(models.Model):
  name = models.CharField(max_length=100)
  checked_out = models.DateTimeField()
  returned = models.DateTimeField(null=True, blank=True)
  hand_out_condition = models.TextField()
  returned_condition = models.TextField(null=True, blank=True)
  employee = models.ForeignKey(to=Employee, on_delete=models.CASCADE)

  def __str__(self) -> str:
    return f'{self.employee} - {self.name}'