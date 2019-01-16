from django import forms  
from django.contrib.auth.models import User
from django.core.validators import validate_email

class userform(forms.ModelForm):
	username = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Enter UserName'}
    ),required=True,max_length=30)
	email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter email'}
    ),required=True, max_length=30)
	first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter first name'}
    ),required=True, max_length=30)
	last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter lastname'}
    ),required=True, max_length=30)
	password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter password'}
    ),required=True, max_length=30)
	confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter confirm password'}
    ),required=True, max_length=30)
	class Meta():
		model=User
		fields=['username','email','first_name','last_name','password','confirm_password']
	def clean_email(self):
		email=self.cleaned_data['email']
		try:
			ma=validate_email(email)
		except:
			raise forms.ValidationError("Email is not Valid")
		return email
	def clean_confirm_password(self):
		p=self.cleaned_data['password']
		cp=self.cleaned_data['confirm_password']
		if(p!=cp):
			raise forms.ValidationError("Confirm Password and Password Must be Same")
		else:
			if(len(p)<6):
				raise forms.ValidationError("Password must be atleast 6 Character")
			if(p.isdigit()):
				raise forms.ValidationError("Password must contains aleast a character")


class ChangePasswordForm(forms.ModelForm):
	old_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-group'}),label="Old Password",required=True)
	new_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-group'}),label="New Password",required=True)
	confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-group'}),label="Confirm New Password",required=True)
	def clean_confirm_password(self):
		np=self.cleaned_data['new_password']
		cp=self.cleaned_data['confirm_password']
		if(np!=cp):
			raise forms.ValidationError("Confirm Password and Password Must be Same")
		else:
			if(len(np)<6):
				raise forms.ValidationError("Password must be atleast 6 Character")
			if(np.isdigit()):
				raise forms.ValidationError("Password must contains aleast a character")

	class Meta:
		model = User
		fields = ['old_password','new_password','confirm_password']
