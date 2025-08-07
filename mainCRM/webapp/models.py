from django.db import models

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# User Record Model
class UserRecord(models.Model):
    f_name = models.CharField(max_length=250)
    l_name = models.CharField(max_length=250)
    phone = models.IntegerField()
    tall = models.IntegerField()
    width = models.IntegerField()
    addres = models.CharField(max_length=500)
    created_at = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.f_name + " " + self.l_name
    
    class Meta:
        ordering = ['-created_at']
