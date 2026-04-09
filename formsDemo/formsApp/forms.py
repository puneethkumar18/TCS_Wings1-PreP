from django import forms

class UserRegistrationForm(forms.Form):
    GENDER = [('male','MALE'),('female','FEMALE')]
    firstName=forms.CharField(required=False)
    lastName = forms.CharField(max_length=30)
    email = forms.CharField(max_length=30, required=False)
    gender = forms.CharField(widget=forms.Select(choices=GENDER))



    def clean(self):
        data = super().clean()
        if str(data['email']).find('@') == -1:
            raise forms.ValidationError("Not Valid Email")
    
    # def clean_firstName(self):
    #     res = self.cleaned_data['firstName']
    #     if len(res) > 8:
    #         raise forms.ValidationError("Should be less than 8")
    #     return res