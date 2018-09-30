# django_xlspopulator
Easy to use .xls Django model populator. 


How to:
1. First you need to install latest version of <b>xlrd: pip install xlrd==1.1.0</b>
1. In order for this to work, you need exactly match your model's field names and xls's first row values(column names), like this:
    ```python
    class Test(models.Model):
      one = models.CharField(max_length=150)
      two = models.CharField(max_length=150)
      three = models.CharField(max_length=150)
      four = models.CharField(max_length=150)
    ```
    <img src="https://github.com/bloodwithmilk25/django-xlspopulator/blob/master/col_names.jpg">
1. Then you need to create `populate.py` file at the one level with your `manage.py`
1. Put following code there:
    ```python
    # populate.py
    import os
    import django
    from django_xlspopulator.populator import Populator
    os.environ.setdefault('DJANGO_SETTINGS_MODULE','YOURPOJECT.settings')
    django.setup()
    from YOURAPP.models import Test

    pop = Populator('C:/Users/Guido/Desktop/testfile.xls', Test)
    pop.populate()
    ```
    * Populator object takes three arguments:
      * path to the .xls file in form of a string
      * Django model object
      * Sheet number, int(0 by defaulft, specify it if you want to use other sheet)
1. Run `populate.py` from the terminal and wait. For my old machine with SQLite it took 5 mins to populate model from file that had 4 columns and 10000 rows.
