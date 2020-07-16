from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name='Category Name')
    details = models.CharField(max_length=500, verbose_name='Category Details')

    parent_id = models.ForeignKey('self', null=True, related_name='category', on_delete=models.CASCADE)

    # def __str__(self):
    #     return "<Category: {} {}>".format(self.category_name)

    def __repr__(self):
        return self.id
        # return self.parent_id.category_name