from django.utils.translation import ugettext_lazy as _
from django import forms
from models import ExcelImportTask
from django.forms import ModelForm


class ExcelFormatTranslateForm(forms.Form):
    # title = forms.CharField(max_length=50)
    import_file = forms.FileField(
        label=_('File to import')
    )
    header_row_numbered_from_1 = forms.IntegerField()
    spreadsheet_numbered_from_1 = forms.IntegerField()
    class_name = forms.CharField()


class ExcelImportTaskForm(ModelForm):
    class Meta:
        model = ExcelImportTask
        fields = ['excel_file', 'content', "header_row_numbered_from_1", "spreadsheet_numbered_from_1"]
    is_import_now = forms.BooleanField()

