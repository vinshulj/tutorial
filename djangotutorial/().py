# coding: utf-8
Quetion.object.all()
Question.object.all()
Question.objects.all()
Question.object.filter(question_text__startswith="What
")
Question.objects.filter(question_text__startswith="What")
from django.utils import timezone
current_year=timezone.now().year()
current_year=timezone.now().year
Question.objects.get(pub_date__year=current_year)
Question.objects.get(pub_date)
q=Question.objects.get(pk=1)
q
q.id
q.pub_date
q.was_published_recently()
q.was_published_recently()
q.choice_set
q.choice_set.all()
q.choice_set.create(choice_text="not much",votes=0)
q.choice_set.create(choice_text="hi",votes=3)
q.choice_set.create(choice_text="the sky",votes=3)
c.question
q.choice_set.create(choice_text="the sky",votes=3).question
c=q.choice_set.create(choice_text="night",votes=0)
c.question
q.choice_set.all()
q.choice_set.count()
c=q.choice_set.filter(choice_text__startswith="the")
c
c.delete()
get_ipython().run_line_magic('save', '')
