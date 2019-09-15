from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import RadioSelect


class QuestionForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        # print(question.get_answers_list())
        choice_list = [x for x in question.get_answers_list()]
        print(choice_list)
        self.fields["answers"] = forms.ChoiceField(choices=choice_list, widget=RadioSelect)



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
    
    def __init__(self, *args, **kwargs):
	    super(SignUpForm, self).__init__(*args, **kwargs)

	    for fieldname in ['username', 'password1', 'password2','first_name','last_name','email']:
	       	self.fields[fieldname].help_text = None


class RegistrationForm(forms.Form):
	username=forms.CharField(max_length=100)
	name=forms.CharField(max_length=100)
	password=forms.CharField(max_length=100)
	email=forms.CharField(max_length=60)
	contact_number=forms.CharField(max_length=100)
	whatsapp_number=forms.CharField(max_length=100)
	dob = forms.CharField(max_length=10)
	gender = forms.CharField(max_length=1)
	address=forms.CharField(max_length=100)
	state=forms.CharField(max_length=100)
	city=forms.CharField(max_length=100)
	pin=forms.CharField(max_length=100)
		   
	fathers_name=forms.CharField(max_length=100)
	fcontact_number=forms.CharField(max_length=100)
	fwhatsapp_number=forms.CharField(max_length=100)

		   
	mothers_name=forms.CharField(max_length=100)
	mcontact_number=forms.CharField(max_length=100)
	mwhatsapp_number=forms.CharField(max_length=100)

	paddress=forms.CharField(max_length=100)
	pstate=forms.CharField(max_length=100)
	pcity=forms.CharField(max_length=100)
	ppin=forms.CharField(max_length=100)

	school_name=forms.CharField(max_length=100)
	class_upto=forms.CharField(max_length=100)
	percentage=forms.CharField(max_length=100)
	saddress=forms.CharField(max_length=100)
	sstate=forms.CharField(max_length=100)
	scity=forms.CharField(max_length=100)
	spin=forms.CharField(max_length=100)
	