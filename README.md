# django-xlspopulator
Easy to use .xls Django model populator. 

( ͡° ͜ʖ ͡°)

How to:
* First you need to install latest version of xlrd: <b>pip install xlrd==1.1.0</b>
* In order for this to work, you need exactly match your model's field names and xls's first row values(column names), like this:
    ```python
    class Test(models.Model):
      one = models.CharField(max_length=150)
      two = models.CharField(max_length=150)
      three = models.CharField(max_length=150)
      four = models.CharField(max_length=150)
    ```
<img src="https://github.com/bloodwithmilk25/django-xlspopulator/blob/master/col_names.jpg">
   
