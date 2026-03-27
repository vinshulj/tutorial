import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField("enter",help_text="Enter question",max_length=200,blank=True)
    pub_date = models.DateTimeField("my")
    # id=models.AutoField(primary_key=True)
    # gender=models.CharField(max_length=1,choices=[('M','Male'),('F','Female')])
    # class Meta:
    #     db_table = 'student20'
    class Meta:
        ordering = ['question_text'] 

    # def __str__(self):
    #     return "que"
    # def __repr__(self):
    #     return "hi"
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def __str__(self):
        return self.question_text
    


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
    class Meta:
        unique_together = ('choice_text', 'votes')


    def __str__(self):
        return self.choice_text

class Gender(models.Model) :
    gender=models.CharField(max_length=1,choices=[('M','Male'),('F','Female')])
    def __str__(self):
        return self.gender

class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
#i have four model Auther (main)(field:-name) then book (field:-title,forignkey to auther) then sales(field:-sale_date,book(forignkey to book),quantity,price) then user(field:-name,age,oneToOne to sales,about)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    
class sales(models.Model):
    sale_date=models.DateField()
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    price=models.FloatField()
    def __str__(self):
        return self.sale_date.strftime("%Y-%m-%d")

class User(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    sales=models.OneToOneField(sales,on_delete=models.CASCADE)
    about=models.TextField("about book",default="this is good book")
    def __str__(self):
        return self.name
    
#charfield,intergerfield,floatfield,decimalfield,datafield,timefield,DateTimefield,Autofield,forignkey,oneToOnefield,
#manytomanyfield,Imagefield,urlfield,filefield,emailfiend                                                   
#model.CASCADE,model.PROtect,model.NONE,model.SET_Default,model.Set_NULL,model.set()
