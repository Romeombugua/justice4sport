from django import forms


class WhoAreYouReportingForm(forms.Form):
    REPORT_CHOICES = [
        ('solicitor', 'Solicitor'),
        ('barrister', 'Barrister'),
        ('judge', 'Judge'),
        ('newspaper', 'Newspaper'),
        ('bank', 'Bank'),
    ]
    
    report_type = forms.ChoiceField(choices=REPORT_CHOICES, label="Who are you reporting?", widget=forms.RadioSelect)

class SolicitorForm(forms.Form):
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
    first_name = forms.CharField(label='First Name', max_length=10000000000)
    last_name = forms.CharField(label='Last Name', max_length=10000000000)
    firm = forms.CharField(label='Firm (if applicable)', max_length=10000000000, required=False)
    address = forms.CharField(label='Address and Postcode', widget=forms.Textarea)
    phone_number = forms.CharField(label='Phone Number', max_length=200000)
    email = forms.EmailField(label='Email Address')
    adjustments = forms.CharField(label='If you need any reasonable adjustments or assistance to report your concerns then please tell us here.', widget=forms.Textarea, required=False)

    # Fields for the person being reported
    individual_acted_for = forms.ChoiceField(choices=YES_NO_CHOICES, label="Has the individual you are reporting acted for you in the past?")
    reported_person_name = forms.CharField(label='Name of the person being reported', max_length=2000000)
    reported_firm_name = forms.CharField(label='Name of the firm being reported', max_length=2000000)
    reported_firm_address = forms.CharField(label='Firm’s address and postcode', widget=forms.Textarea)
    reported_firm_phone = forms.CharField(label='Firm’s phone number', max_length=200000)

    # Additional fields
    acted_for_you = forms.ChoiceField(choices=YES_NO_CHOICES, label="Has the individual's firm acted for you in the past?")
    act_for_another_person = forms.ChoiceField(choices=YES_NO_CHOICES, label="Does the individual you’re reporting act for another person?")
    individual_acting_for = forms.CharField(label="Who is the individual acting for (if applicable)?", max_length=2000000, required=False)
    
    # Details of the report (main complaint text)
    complaint = forms.CharField(label='Details of your report',max_length=1000000000, widget=forms.Textarea, help_text='Please tell us your concerns as clearly as possible. \n\tProvide as much relevant information as possible as this is what we will use to assess your report. \n\tInclude dates where appropriate.\n\t If you are reporting more than one individual/firm, please make clear what you think each has done wrong. If you have already contacted another organisation about this matter please tell us the outcome.')
    
    # Signature and Date
    signature = forms.CharField(label='Your Signature', max_length=100000000)
    date = forms.DateField(label='Date', widget=forms.DateInput(attrs={'type': 'date'}))
    
    
    
class BarristerForm(forms.Form):
    # Section 9: Personal details (optional for anonymous reporting)
    your_title = forms.ChoiceField(choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Ms', 'Ms'), ('Miss', 'Miss'), ('Other', 'Other')], label="Your Title", required=False)
    your_name = forms.CharField(label="Your Name", max_length=2000000, required=False)
    your_email = forms.EmailField(label="Your Email", required=False)
    your_phone_number = forms.CharField(label="Your Phone Number", max_length=200000, required=False)
    your_address1 = forms.CharField(label="Your Address Line", max_length=2000000, required=False)
    # your_address2 = forms.CharField(label="Your Address Line 2", max_length=2000000, required=False)
    # your_address3 = forms.CharField(label="Your Address Line 3", max_length=2000000, required=False)
    your_postcode = forms.CharField(label="Your Postcode", max_length=200000, required=False)
    # Section 1: Who you're reporting
    barrister_name = forms.CharField(label="Name of barrister/chambers/entity", max_length=2000000)
    address1 = forms.CharField(label="Address of barrister/body", max_length=2000000)
    # address2 = forms.CharField(label="Address 2 of barrister/body", max_length=2000000, required=False)
    # address3 = forms.CharField(label="Address 3 of barrister/body", max_length=2000000, required=False)
    postcode = forms.CharField(label="Postcode of barrister/body", max_length=200000)
    email = forms.EmailField(label="Email of barrister/body")
    phone_number = forms.CharField(label="Phone number of barrister/body", max_length=200000)

    # Section 2: Reporting more than one barrister
    more_than_one = forms.ChoiceField(choices=[('Yes', 'Yes'), ('No', 'No')], label="Is it about more than one barrister/chambers/entity/AETO?", widget=forms.RadioSelect)
    
    # Additional details for more barristers (conditionally required)
    second_barrister_name = forms.CharField(label="Name of second barrister/chambers/entity", max_length=2000000, required=False)
    second_address1 = forms.CharField(label="Address of second barrister/body", max_length=2000000, required=False)
    # second_address2 = forms.CharField(label="Address 2 of second barrister/body", max_length=2000000, required=False)
    # second_address3 = forms.CharField(label="Address 3 of second barrister/body", max_length=2000000, required=False)
    second_postcode = forms.CharField(label="Postcode of second barrister/body", max_length=200000, required=False)
    second_email = forms.EmailField(label="Email of second barrister/body", required=False)
    second_phone_number = forms.CharField(label="Phone number of second barrister/body", max_length=200000, required=False)

    # Section 3: Case-related information
    acting_for = forms.ChoiceField(choices=[('Me', 'Me'), ('Someone Else', 'Someone Else'), ('Not Applicable', 'Not Applicable')], label="Who was/is the barrister or entity acting for?", widget=forms.RadioSelect)
    related_to_previous_report = forms.ChoiceField(choices=[('Yes', 'Yes'), ('No', 'No')], label="Does this relate to any other report that has previously been made to the BSB?", widget=forms.RadioSelect)
    reference_number = forms.CharField(label="Please give a reference number or details (if applicable)", max_length=2000000, required=False)
    
    # Section 4: Court case details
    related_to_court_case = forms.ChoiceField(choices=[('Yes', 'Yes'), ('No', 'No')], label="Does this matter relate to a court case?", widget=forms.RadioSelect)
    case_name = forms.CharField(label="Name of case", max_length=2000000, required=False)
    court_name = forms.CharField(label="Name of court", max_length=2000000, required=False)
    court_reference_number = forms.CharField(label="Reference number", max_length=2000000, required=False)

    # Section 5: Your relationship to the case
    relationship_to_case = forms.ChoiceField(choices=[
        ('Involved', 'I was involved in the case (on either side)'),
        ('Witness', 'Witness'),
        ('Member of the public', 'Member of the public'),
        ('Judge/Magistrate', 'Judge/Magistrate'),
        ('Legal professional', 'Legal professional'),
        ('Other', 'Other'),
    ], label="What is your relationship to the case?", widget=forms.RadioSelect)

    litigant_in_person = forms.ChoiceField(choices=[('Yes', 'Yes'), ('No', 'No')], label="Were you a Litigant in person (acting for yourself without a lawyer)?", widget=forms.RadioSelect)
    case_ongoing = forms.ChoiceField(choices=[('Yes', 'Yes'), ('No', 'No')], label="Is the case ongoing?", widget=forms.RadioSelect)

    # Section 6: Event details
    last_occurrence = forms.DateField(label="Date of last occurrence", widget=forms.DateInput(attrs={'type': 'date'}))
    event_information = forms.CharField(label="Please set out as clearly as possible the information you want to tell us", widget=forms.Textarea, max_length=1000000000)

    # Section 7: Additional witnesses
    witness_name = forms.CharField(label="Name of witness (if applicable)", max_length=2000000, required=False)
    witness_email = forms.EmailField(label="Email of witness (if applicable)", required=False)
    witness_phone_number = forms.CharField(label="Phone number of witness (if applicable)", max_length=200000, required=False)
    witness_consent = forms.ChoiceField(choices=[('Yes', 'Yes'), ('No', 'No')], label="Have they given consent to be contacted by BSB?", widget=forms.RadioSelect, required=False)

    # Section 8: Documentation and additional information
    # supporting_documents = forms.FileField(label="Please give us any supporting documentation", required=False)
    other_information = forms.CharField(label="Is there any other information you wish to add?", widget=forms.Textarea, required=False)



    # Section 10: Communication preferences
    communication_needs = forms.ChoiceField(choices=[('Yes', 'Yes'), ('No', 'No')], label="Do you have any specific communication needs?", widget=forms.RadioSelect, required=False)
    preferred_contact_method = forms.CharField(label="Preferred method of contact", max_length=2000000, required=False)

    # Section 11: Declaration
    declaration = forms.BooleanField(label="I confirm that the information given in this form is true, complete and accurate.")


class JCIOForm(forms.Form):
    
        # Personal information fields
    your_title = forms.ChoiceField(choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Ms', 'Ms'), ('Miss', 'Miss'), ('Other', 'Other')], label="Your Title", required=False)
    your_name = forms.CharField(label="Your Name", max_length=2000000, required=False)
    your_email = forms.EmailField(label="Your Email", required=False)
    your_phone_number = forms.CharField(label="Your Phone Number", max_length=200000, required=False)
    your_address1 = forms.CharField(label="Your Address Line", max_length=2000000, required=False)
    # your_address2 = forms.CharField(label="Your Address Line 2", max_length=2000000, required=False)
    # your_address3 = forms.CharField(label="Your Address Line 3", max_length=2000000, required=False)
    your_postcode = forms.CharField(label="Your Postcode", max_length=200000, required=False)
    
    hearing_date = forms.DateField(
        label="Hearing Date",
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False
    )
    hearing_venue = forms.CharField(label="Hearing Venue", max_length=2000000, required=True)
    judicial_officer = forms.CharField(label="Judicial Office Holder", max_length=2000000, required=True)
    hearing_number = forms.CharField(label="Hearing Number", max_length=1000000, required=False)
    misconduct_date = forms.DateField(
        label="Date of Alleged Misconduct",
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True
    )
    complaint_details = forms.CharField(
        label="Details of Complaint",
        widget=forms.Textarea,
        help_text="Please give specific examples of the conduct that you are complaining about.",
        required=True,
        max_length=1000000000
    )
    
    # Optional field for multiple dates of misconduct
    additional_dates = forms.CharField(
        label="Additional Dates (if applicable)",
        widget=forms.Textarea,
        required=False,
        help_text="If your complaint relates to more than one date, please include the further dates here."
    )
    
    # File attachment
    # supporting_document = forms.FileField(label="Attach a file", required=False)

    # Mandatory confirmation
    guidance_read = forms.BooleanField(
        label="I have read your guidance about the JCIO's remit",
        required=True
    )
    
    understanding_remit = forms.BooleanField(
        label="I understand that my complaint will be rejected if it falls outside your remit.",
        required=True
    )

class NewspaperForm(forms.Form):
    your_title = forms.ChoiceField(choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Ms', 'Ms'), ('Miss', 'Miss'), ('Other', 'Other')], label="Your Title", required=False)
    full_name = forms.CharField(max_length=255, label="Full Name")
    full_address = forms.CharField(widget=forms.Textarea, label="Full Address")
    email_address = forms.EmailField(label="Email Address")
    mobile_phone = forms.CharField(max_length=15, label="Mobile Phone")
    complain_on_behalf = forms.CharField(widget=forms.Textarea, label="Are you making a complaint on behalf of someone else? (If so enter their full name, postal address & telephone number)", required=False)
    relationship_to_person = forms.CharField(max_length=255, label="Your relationship to the person you want to complain about", required=False)
    consent_to_complain = forms.BooleanField(label="Have they agreed to you making this complaint on their behalf?", required=False)
    
    person_or_firm_complained_about = forms.CharField(max_length=255, label="Who are you complaining about? (Full name and position of the person, or the firm name)")
    firm_postal_address = forms.CharField(widget=forms.Textarea, label="Full postal address of the firm")
    type_of_work = forms.CharField(max_length=255, label="What kind of work was involved in the complaint?")
    complaint_details = forms.CharField(widget=forms.Textarea, label="What are you complaining about? (Briefly describe the issue)", max_length=1000000000)
    
    problem_awareness_date = forms.DateField(label="Date you first became aware of the problem", widget=forms.DateInput(attrs={'type': 'date'}))
    impact_on_you = forms.CharField(widget=forms.Textarea, label="What effect has this had on you?")
    
    complained_to_firm = forms.BooleanField(label="Have you complained to the person or firm involved?", required=False)
    date_of_complaint = forms.DateField(label="When did you complain to the person or firm?", widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    firm_response = forms.CharField(widget=forms.Textarea, label="What response have you had to your complaint from the person or firm?", required=False)
    firm_actions = forms.CharField(widget=forms.Textarea, label="Please describe what the person or firm involved has said or done about your complaint since you made it to them.", required=False)
    
    desired_resolution = forms.CharField(widget=forms.Textarea, label="What do you think the person or firm involved should have done to get you Justice?")


class BankForm(forms.Form):
    your_title = forms.ChoiceField(choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Ms', 'Ms'), ('Miss', 'Miss'), ('Other', 'Other')], label="Your Title", required=False)
    full_name = forms.CharField(max_length=255, label="Full Name")
    full_address = forms.CharField(widget=forms.Textarea, label="Full Address")
    email_address = forms.EmailField(label="Email Address")
    mobile_phone = forms.CharField(max_length=15, label="Mobile Phone")
    complain_on_behalf = forms.CharField(widget=forms.Textarea, label="Are you making a complaint on behalf of someone else? (If so enter their full name, postal address & telephone number)", required=False)
    relationship_to_person = forms.CharField(max_length=255, label="Your relationship to the person you want to complain about", required=False)
    consent_to_complain = forms.BooleanField(label="Have they agreed to you making this complaint on their behalf?", required=False)
    
    person_or_firm_complained_about = forms.CharField(max_length=255, label="Who are you complaining about? (Full name and position of the person, or the firm name)")
    firm_postal_address = forms.CharField(widget=forms.Textarea, label="Full postal address of the firm")
    type_of_work = forms.CharField(max_length=255, label="What kind of work was involved in the complaint?")
    complaint_details = forms.CharField(widget=forms.Textarea, label="What are you complaining about? (Briefly describe the issue)", max_length=1000000000)
    
    problem_awareness_date = forms.DateField(label="Date you first became aware of the problem", widget=forms.DateInput(attrs={'type': 'date'}))
    impact_on_you = forms.CharField(widget=forms.Textarea, label="What effect has this had on you?")
    
    complained_to_firm = forms.BooleanField(label="Have you complained to the person or firm involved?", required=False)
    date_of_complaint = forms.DateField(label="When did you complain to the person or firm?", widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    firm_response = forms.CharField(widget=forms.Textarea, label="What response have you had to your complaint from the person or firm?", required=False)
    firm_actions = forms.CharField(widget=forms.Textarea, label="Please describe what the person or firm involved has said or done about your complaint since you made it to them.", required=False)
    
    desired_resolution = forms.CharField(widget=forms.Textarea, label="What do you think the person or firm involved should have done to get you Justice?")
