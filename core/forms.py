from django import forms
from .models import Paste

PASTE_EXPIRY = (
    
    ("never", "Never"),
    ("burnafterread", "Burn after read" ),
    ("tenmins", "10 Minutes"),
    ("onehour", "1 Hour"),
    ("oneday", "1 Day"),
    ("oneweek", "1 Week"),
    ("twoweeks", "2 Weeks"),
    ("onemonth", "1 Month"),
    ("sixmonths", "6 Months"),
    ("oneyear", "1 Year")

)
class PasteForm(forms.ModelForm):
    paste_expiry = forms.ChoiceField(choices=PASTE_EXPIRY, widget=forms.Select(attrs= {'id': 'pasteExpiry'})) 
    tag_list = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'type': 'text', 'id': 'tagsInput'}))
   
    def __init__(self, *args, **kwargs):
        super(PasteForm, self).__init__(*args, **kwargs)
        # Set initial values
       
        
    class Meta:
        model = Paste
        fields = ['content', 'paste_exposure', 'title', 'burn_after_reading', 'password', 'password_text', 'paste_expiry', 'tag_list']
        widgets = {
            
            'content': forms.Textarea(attrs={'class': 'paste-form__textarea'}),
            
            

        }
