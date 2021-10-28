from django import forms

class MyForm(forms.Form):
    firstname = forms.CharField(label="First Name",max_length=30)
    lastname = forms.CharField(label="Last Name",max_length=30)
    email = forms.EmailField(label="Email")
    CHOICES = ((5,'Best'),(4,'Good'),(3,'Average'),(2,'Bad'),(1,'Worst'))
    rating = forms.ChoiceField(label="Rate My Site!",choices=CHOICES,widget=forms.RadioSelect)
    comments = forms.CharField(label="Suggestions are welcome!",widget=forms.Textarea,required=False)
