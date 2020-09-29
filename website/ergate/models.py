from django.db import models

# Create your models here.
class Autoset(models.Model):
    auto_num = models.IntegerField(primary_key=True)
    uname = models.CharField(max_length=45)
    s_num = models.ForeignKey('Stockitem', models.DO_NOTHING, db_column='s_num')
    sname = models.CharField(max_length=45)
    set_money = models.FloatField()
    today = models.FloatField()
    input = models.FloatField()
    output = models.FloatField()
    profit = models.FloatField()
    flag = models.IntegerField()
    strat_date = models.CharField(max_length=45)
    end_date = models.CharField(max_length=45)
    autosetcol = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'autoset'
class PredictRate(models.Model):
    stock_num = models.OneToOneField('Stockitem', models.DO_NOTHING, db_column='stock_num', primary_key=True)
    name = models.CharField(max_length=45)
    numofstock = models.FloatField(db_column='numOfstock')  # Field name made lowercase.
    persent = models.FloatField()

    class Meta:
        managed = False
        db_table = 'predict_rate'


class Simulation(models.Model):
    simul_num = models.IntegerField(primary_key=True)
    uname = models.CharField(max_length=45)
    st_num = models.ForeignKey('Stockitem', models.DO_NOTHING, db_column='st_num')
    sname = models.CharField(max_length=45)
    set_money = models.FloatField()
    today = models.FloatField()
    input = models.FloatField()
    output = models.FloatField()
    profit = models.FloatField()
    start_date = models.CharField(max_length=45)
    end_date = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'simulation'


class Stockitem(models.Model):
    stock_num = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45)
    representative = models.CharField(max_length=45)
    price = models.FloatField()
    numofstock = models.FloatField(db_column='numOfstock')  # Field name made lowercase.
    probabilitytowin = models.FloatField(db_column='probabilitytoWin')  # Field name made lowercase.
    probabilitytolose = models.FloatField(db_column='probabilitytoLose')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stockitem'