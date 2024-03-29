from django import forms
from django.forms.widgets import Select, DateInput
from django.shortcuts import reverse
from .models import Invoice, Part, Labour, Customer, Vehicle
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Reset, Field, ButtonHolder, HTML
from crispy_forms.bootstrap import Modal, PrependedText
from crispy_bootstrap5.bootstrap5 import FloatingField

def add_or_edit_button(slug):
    if slug:
        text = 'Edit'
    else:
        text = 'Create'
    return text

def add_or_edit_trash(slug):
    if slug:
        return HTML('<button type="button" data-bs-toggle="modal" data-bs-target='
                    f'"#delete-{slug}-modal" class="btn btn-light p-2 rounded-4">'
                    '<i class="bi-trash icon text-danger fs-3 align-middle"></i></button>')

def add_or_edit_path(slug, type):
    if slug:
        path = reverse('edit_'+type, args=[slug])
    else:
        path = reverse('create_'+type)
    return path

def add_or_edit_modal(slug, type, layout):
    if slug:
        layout
    else:
        layout = Modal(
            layout,
            css_id=type+"_modal",
            title="Add "+type.capitalize(),
            css_class="modal-lg h-100 overflow-y-auto"
        )
    return  layout
      

class CustomSelectWidget(Select):
    """ custom select widget to label each vehicle class with the corrsponding customer fk """
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(
            name, value, label, selected, index, subindex=subindex, attrs=attrs)
        try:
            instance = self.choices.queryset.get(pk=value.value)
            option_fk = instance.customer.id
            if option_fk:
                option['attrs']['class'] = option_fk
        except:
            option['attrs']['class'] = 'no_customer'
        return option


class InvoiceForm(forms.ModelForm):

    vehicle = forms.ModelChoiceField(
        queryset=Vehicle.objects.all(), widget=CustomSelectWidget)
    
    date_in = forms.DateField(
        label="From Date", widget=DateInput(attrs={'type': 'date'}))

    class Meta:
        model  = Invoice
        fields = ('customer', 'vehicle', 'date_in', 'mileage','status')
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.required = False
            
        self.helper = FormHelper()
        self.helper.form_action = add_or_edit_path(self.instance.slug, 'invoice')
        self.helper.form_class = 'mb-3'
        self.helper.layout = add_or_edit_modal(
            self.instance.slug,
            'invoice',
            Layout(
                Row(
                    Field('status', type="hidden"), css_class='mb-3'
                ),
                Row(
                    Column(
                        FloatingField(
                            'customer', 'date_in'
                        )
                    ),
                    Column(
                        FloatingField(
                            'vehicle', 'mileage'
                        ),
                    ),
                ),
                Row(
                    Column(
                        ButtonHolder(
                            Submit(
                                'submit',
                                add_or_edit_button(self.instance.slug),
                                css_class='ms-2'
                            ),css_class='float-end',
                        )
                    )
                )
            )
        )   


