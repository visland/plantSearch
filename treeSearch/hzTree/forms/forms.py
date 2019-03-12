from django import forms
from django.forms import NumberInput, TextInput, Select, CheckboxSelectMultiple

BLOOM_COLOR_CONDITION_CHOICES = (
    ('白', '白色'),
    ('红', '红色'),
    ('黄', '黄色'),
    ('紫', '紫色'),
    ('绿', '绿色'),
)

FRUIT_COLOR_CONDITION_CHOICES = (
    ('白', '白色'),
    ('黄', '黄色'),
    ('红', '红色'),
    ('紫', '紫色'),
)

MONTHS_CHOICES = (
    ('任意', '任意'),
    ('Jan', '1月'),
    ('Feb', '2月'),
    ('Mar', '3月'),
    ('Apr', '4月'),
    ('May', '5月'),
    ('Jun', '6月'),
    ('Jul', '7月'),
    ('Aug', '8月'),
    ('Sep', '9月'),
    ('Oct', '10月'),
    ('Nov', '11月'),
    ('Dec', '12月'),
)

class QueryUserForm(forms.Form):
    queryContent = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control is-invalid',
            'placeholder': 'I Love you :)'}))

    bloom_color_condition = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=BLOOM_COLOR_CONDITION_CHOICES)

    fruit_color_condition = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FRUIT_COLOR_CONDITION_CHOICES)

    bloom_date_condition = forms.ChoiceField(
        widget=forms.Select,
        choices=MONTHS_CHOICES,)
    
    fruit_date_condition = forms.ChoiceField(
        widget=forms.Select,
        choices=MONTHS_CHOICES)

    