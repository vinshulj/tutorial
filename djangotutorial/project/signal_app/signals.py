from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save,pre_init,post_init,pre_save,pre_delete,post_delete
from django.dispatch import receiver
from .models import AddressList, UserAddressList
from adminpage.models import Adduser
@receiver(pre_init, sender=Profile)
def modify_profile_init(sender, args, kwargs, **others):
    print("Pre-initialization")
    # print(User.objects.all())
    print(kwargs)
    if 'name' in kwargs:
        kwargs['name'] = kwargs['name'].lower()
        
@receiver(post_init, sender=Profile)
def modify_profile_post_init(sender, instance, **others):
    print("Post-initialization")
    # print(User.objects.filter(username="guys"))
    if instance.age is not None:
        instance.age += 2
        print(instance.name, instance.age)

@receiver(pre_save, sender=Profile)
def Save(sender, instance,raw, **kwargs):
    print(f"Pre-save : {instance.name}")
    print(kwargs.get('raw'))
    if instance.age:
        instance.age -=2
    print(instance.name,instance.age)
    print(kwargs.get('using'))
    print(kwargs.get('raw'))

@receiver(post_save, sender=Profile)
def Save(sender, instance, created, **kwargs):
    print(f"Post-save : {instance.name}")
    if created:
        print("Profile created")
        if instance.age:
            instance.age +=2
        print(instance.name,instance.age)
    else:
        print("Profile updated")


@receiver(pre_delete, sender=Profile)
def modify_profile_pre_delete(sender, instance, **others):
    print("Pre-delete")
    print(instance.name, instance.age)
        
@receiver(post_delete, sender=Profile)
def modify_profile_post_delete(sender, instance, **others):
    print("Post-delete")
    print(instance.name, instance.age)



# aswer of this question
@receiver(post_init, sender=Adduser)
def modify_user_post_init(sender, instance, **others):
    if not hasattr(instance, '_is_post_initialized'):
        instance._is_post_initialized = True
        print("Post-initialization of User")
        print(UserAddressList.objects.filter(user=instance.user))
        print(instance.user)



# from django.core.signals import request_started,request_finished
# import json

# @receiver(request_started)
# def request_started_receiver(sender,environ, **kwargs):
#     if environ['PATH_INFO'] == '/jwtapi/api/ctoken/a/' and environ['REQUEST_METHOD'] == 'POST':
#         # env=environ['wsgi.input']
#         # body_data = json.loads(env.read().decode('utf-8'))
#         # # environ['wsgi.input']=env
#         # # print(json.loads(environ['wsgi.input'].read().decode('utf-8')))
#         # if not body_data:
#         #     print("Empty body received")
#         # else:
#         #     print(body_data.get('username'))
#         #     print("Request started signal received.")
#         #     print(AddressList.objects.filter(adduser__user__username=body_data.get('username')))
            
#         @receiver(post_init, sender=Adduser)
#         def modify_user_post_init(sender, instance, **others):
#             if not hasattr(instance, '_is_post_initialized'):
#                 instance._is_post_initialized = True
#                 print("Post-initialization of User")
#                 print(AddressList.objects.filter(adduser=instance.id))
#     else:
#         print("Request started signal received for a different path.")



@receiver([post_save,post_delete], sender=UserAddressList)
def prmission(sender,instance, **kwargs):
    print("Permission check for user:", instance.user)
    # if instance.user.username and instance.user.password:
    #     print("Permission granted for user:")
    # else:
    #     print("Permission denied for user:", instance.user.username)
    
@receiver(post_save, sender=User)
def modify_user_ave(sender, instance, **others):
    address_list = UserAddressList.objects.filter(user__username=instance.username)
    if not address_list:                                    
        empty_address = UserAddressList(user=instance)
        empty_address.save()