from django.db import models


class tb_user(models.Model):
    UserSeq = models.IntegerField(primary_key=True)
    UserId = models.CharField(max_length=255, null=True)
    Pw = models.CharField(max_length=255, null=True)
    Email = models.CharField(max_length=255, null=True)
    regDate = models.CharField(max_length=10, null=True)
    regTime = models.CharField(max_length=6, null=True)
    InsertDateTime = models.DateTimeField(null=True)
    UpdateDateTime = models.DateTimeField(null=True)

    class Meta:
        managed = True
        db_table = 'tb_user'


class tb_reward(models.Model):
    RewardSeq = models.IntegerField(primary_key=True)
    UserSeq = models.IntegerField()
    isEarn = models.CharField(max_length=2, null=True)
    Reward = models.DecimalField(max_digits=19, decimal_places=5, null=True)
    rewardDate = models.CharField(max_length=10, null=True)
    rewardTime = models.CharField(max_length=6, null=True)
    InsertDateTime = models.DateTimeField(null=True)
    UpdateDateTime = models.DateTimeField(null=True)

    class Meta:
        managed = True
        db_table = 'tb_reward'


class tb_order(models.Model):
    OrderSeq = models.IntegerField(primary_key=True)
    UserSeq = models.IntegerField()
    ItemSeq = models.IntegerField()
    IsReward = models.CharField(max_length=2, null=True)
    UseReward = models.DecimalField(max_digits=19, decimal_places=5, null=True)
    RestReward = models.DecimalField(max_digits=19, decimal_places=5, null=True)
    OrderDate = models.CharField(max_length=10, null=True)
    OrderTime = models.CharField(max_length=6, null=True)
    InsertDateTime = models.DateTimeField(null=True)
    UpdateDateTime = models.DateTimeField(null=True)

    class Meta:
        managed = True
        db_table = 'tb_order'


class tb_item(models.Model):
    ItemSeq = models.IntegerField(primary_key=True)
    ItemName = models.CharField(max_length=255, null=True)
    ItemPrice = models.DecimalField(max_digits=19, decimal_places=5, null=True)
    Category = models.CharField(max_length=255, null=True)
    memo = models.TextField(max_length=1000, null=True)
    InsertDateTime = models.DateTimeField(null=True)
    UpdateDateTime = models.DateTimeField(null=True)

    class Meta:
        managed = True
        db_table = 'tb_item'