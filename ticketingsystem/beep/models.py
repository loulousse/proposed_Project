from django.db import models
# Create your models here.

class User(models.Model):
    userId = models.AutoField(primary_key = True)
    fname = models.CharField(max_length = 200, null = True)
    lname = models.CharField(max_length = 200, null = True)

    class meta:
        db_table = 'User'

class Route(models.Model):
    routeId = models.AutoField(primary_key = True)
    #userId = models.ForeignKey(User, on_delete = models.CASCADE)
    route_from = models.CharField(max_length = 200, null = True)
    route_to = models.CharField(max_length = 200, null = True)
    fare = models.IntegerField()

    class meta:
        db_table = 'Route'

class BeepJeep(models.Model):
    beepId = models.AutoField(primary_key = True)
    #routeId = models.ForeignKey(Route, on_delete = models.CASCADE)
    color = models.CharField(max_length = 200, null = True)
    capacity = models.CharField(max_length = 200, null = True)
    #beepStatus = models.CharField(max_length = 200, null = True)
    beepStatus = models.IntegerField()

    class meta:
        db_table = 'BeepJeep'

class Ticket(models.Model):
    ticketId = models.AutoField(primary_key = True)
    #userId = models.ForeignKey(User, on_delete = models.CASCADE)
    #beepId = models.ForeignKey(BeepJeep, on_delete = models.CASCADE)
    #routeId = models.ForeignKey(Route, on_delete = models.CASCADE)
    modeOfPayment = models.CharField(max_length = 200, null = True)
    validTime  = models.IntegerField()

    class meta:
        db_table = 'Ticket'
