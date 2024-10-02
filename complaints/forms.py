from django import forms

class ComplaintForm(forms.Form):
    TITLE_CHOICES = [
        ('Mr', 'Mr'),
        ('Mrs', 'Mrs'),
        ('Ms', 'Ms'),
        ('Miss', 'Miss'),
        ('Other', 'Other')
    ]

    YES_NO_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No')
    ]

    title = forms.ChoiceField(choices=TITLE_CHOICES, label="Title")
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    firm = forms.CharField(label='Firm (if applicable)', max_length=100, required=False)
    address = forms.CharField(label='Address and Postcode', widget=forms.Textarea)
    phone_number = forms.CharField(label='Phone Number', max_length=20)
    email = forms.EmailField(label='Email Address')
    adjustments = forms.CharField(label='If you need any reasonable adjustments or assistance to report your concerns then please tell us here.', widget=forms.Textarea, required=False)

    # Fields for the person being reported
    individual_acted_for = forms.ChoiceField(choices=YES_NO_CHOICES, label="Has the individual you are reporting acted for you in the past?")
    reported_person_name = forms.CharField(label='Name of the person being reported', max_length=200)
    reported_firm_name = forms.CharField(label='Name of the firm being reported', max_length=200)
    reported_firm_address = forms.CharField(label='Firm’s address and postcode', widget=forms.Textarea)
    reported_firm_phone = forms.CharField(label='Firm’s phone number', max_length=20)

    # Additional fields
    acted_for_you = forms.ChoiceField(choices=YES_NO_CHOICES, label="Has the individual's firm acted for you in the past?")
    act_for_another_person = forms.ChoiceField(choices=YES_NO_CHOICES, label="Does the individual you’re reporting act for another person?")
    individual_acting_for = forms.CharField(label="Who is the individual acting for (if applicable)?", max_length=200, required=False)
    
    # Details of the report (main complaint text)
    complaint = forms.CharField(label='Details of your report', widget=forms.Textarea, help_text='Please tell us your concerns as clearly as possible. \n\tProvide as much relevant information as possible as this is what we will use to assess your report. \n\tInclude dates where appropriate.\n\t If you are reporting more than one individual/firm, please make clear what you think each has done wrong. If you have already contacted another organisation about this matter please tell us the outcome.')
    
    # Signature and Date
    signature = forms.CharField(label='Your Signature', max_length=100)
    date = forms.DateField(label='Date', widget=forms.DateInput(attrs={'type': 'date'}))
