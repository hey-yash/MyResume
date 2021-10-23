from django import forms

class MyForm(forms.Form):
    firstname = forms.CharField(label="First Name",max_length=30)
    lastname = forms.CharField(label="Last Name",max_length=30)
    email = forms.EmailField(label="Email")
    comments = forms.CharField(widget=forms.Textarea(attrs={'rows':5,'cols':50,'style':'resize:none;'}),required=False)

    CHOICES = ((5,'Best'),(4,'Good'),(3,'Average'),(2,'Bad'),(1,'Worst'))
    rating = forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)
