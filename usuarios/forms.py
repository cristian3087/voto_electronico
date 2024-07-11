# forms.py

from django import forms

class UploadExcelForm(forms.Form):
    excel_file = forms.FileField(label='Archivo Excel', widget= forms.FileInput(attrs={'style': 'border:none;background:#e9e9ed;color:#000000;'}))
