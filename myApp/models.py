from django.db import models

# Create your models here.
# 1.Model for experienceData
class Experience(models.Model):
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    title = models.CharField(max_length=200)
    tools = models.JSONField(default=list) #เก็บข้อมูลเป็นแบบ Array แต่ถ้า default = dict จะเป็น Obj แทน
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True) #null= True เมื่อถ้างานนนี้ยังทำไม่เสร็จกำลังทำ

    class Meta:
        ordering = ['-start_date'] # เรียงจากปัจจุบันไปอดีต ถ้าลบ - ออกจะเป็นอดีตไปปัจจุบัน

    def __str__(self):
        return f"{self.title}"
# 2.Model for skillData
class Skill(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    level = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"    
    
# 3.Model for projectData
class Project(models.Model):
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    name = models.CharField(max_length=200)
    tools = models.JSONField(default= list)
    description = models.TextField()
    github_link = models.URLField(null=True, blank=True)
    demo_link = models.URLField(null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True) #null= True เมื่อถ้างานนนี้ยังทำไม่เสร็จกำลังทำ

    def __str__(self):
        return f"{self.name}"  
    