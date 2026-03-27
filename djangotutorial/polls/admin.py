from django.contrib import admin
from .models import Question
from .models import Choice,Gender,Author,Book,User,sales

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Gender)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(User)  
admin.site.register(sales)