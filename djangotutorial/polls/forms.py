from django import forms

class UserloginForm(forms.Form):
    User_name = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    
    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
    
from django import forms
class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super().__init__(*args, **kwargs)

    username = forms.CharField(max_length=6)
    password = forms.CharField(widget=forms.PasswordInput)
    


from django import forms
from django.contrib.auth.models import User as AuthUser

class UserCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)  # hide password input

    class Meta:
        model = AuthUser
        fields = ["username", "password"]  # choose fields you want

    def save(self, commit=True):
        user = super().save(commit=False)
        # Hash the password before saving
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = AuthUser
        fields = ["username", "password"]  # choose fields you want
    def save(self, commit=True):
        user = super().save(commit=False)
        # Hash the password before saving
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

# forms.py
from django import forms
from .models import Author,Book
#, Book, sales as Sales, User as UserProfile

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) <3 and name.isalpha():
            raise forms.ValidationError("Author name must be at least 3 characters long and contain only letters.")
        return name

class AuthorUpdateForm(forms.ModelForm):
    previous_name = forms.CharField(
        label="Previous Name",
        required=False,
        disabled=True
    )

    class Meta:
        model = Author
        fields = ["previous_name", "name"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # populate previous_name from instance
        if self.instance.pk:
            self.fields["previous_name"].initial = self.instance.name
            
class AuthorDeleteForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = [] # No fields needed for delete confirmation 
    # def __init__(self, *args, **kwargs): # IT WILL NOT BE NEEDED FOR DELETE AS NOT USE MODEL FORM
    #     super().__init__(*args, **kwargs)

    #     # populate previous_name from instance
    #     if self.instance.pk:
    #         self.fields["name"].initial = self.instance.name
    
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']
        
