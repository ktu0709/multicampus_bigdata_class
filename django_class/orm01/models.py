from django.db import models

# Create your models here.
class dept(models.Model):
    deptno=models.AutoField(primary_key=True)
    dname=models.CharField(max_length=20,null=True,blank=True)
    loc=models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.deptno} {self.dname} {self.loc}"


    class Meta:
        managed = False
        db_table='dept' #실제 DB의 테이블의 이름과 동일

class emp(models.Model):
    empno=models.AutoField(primary_key=True)
    ename=models.CharField(max_length=20, null=True, blank=True)
    job=models.CharField(max_length=20,null=True,blank=True)
    mgr = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    hiredate = models.DateField(null=True, blank=True)
    sal = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
    comm = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
    deptno = models.ForeignKey(
        "dept",
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="employees"
    )

    def __str__(self):
        return f"{self.empno} {self.ename} {self.job} {self.mgr} {self.hiredate} {self.sal} {self.comm} {self.deptno}"

    class Meta:
        managed = False
        db_table='emp' #실제 DB의 테이블의 이름과 동일



class address(models.Model):
    _id=models.AutoField(primary_key=True)
    my_name = models.CharField(max_length=70,null=True)
    my_addr=models.CharField(max_length=70,null=True,blank=True)
    EMAIL=models.CharField(max_length=70, null=True, blank=True)

    def __str__(self):
        return f"{self.my_name} {self.my_addr} {self.EMAIL}"


    class Meta:
        managed = True
        db_table='m_address' #실제 DB의 테이블의 이름과 동일

class address02(models.Model):
    #_id=models.AutoField(primary_key=True)
    my_name = models.CharField(max_length=100,primary_key=True)
    my_addr=models.CharField(max_length=70,null=True,blank=True)
    EMAIL=models.CharField(max_length=70, null=True, blank=True)

    def __str__(self):
        return f"{self.my_name} {self.my_addr} {self.EMAIL}"


    class Meta:
        managed = True
        db_table='m_address02' #실제 DB의 테이블의 이름과 동일

class address03(models.Model):
    _id=models.AutoField(primary_key=True)
    my_name = models.CharField(max_length=70,null=True)
    my_addr=models.CharField(max_length=70,null=True,blank=True)
    EMAIL=models.CharField(max_length=70, null=True, blank=True)

    def __str__(self):
        return f"{self.my_name} {self.my_addr} {self.EMAIL}"


    class Meta:
        managed = True
        db_table='m_address03' #실제 DB의 테이블의 이름과 동일