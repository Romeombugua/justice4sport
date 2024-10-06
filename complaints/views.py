from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
from .models import PastCase
from .forms import ComplaintForm, WhoAreYouReportingForm, JCIOForm,  BarristerForm
from django.db.models import Q
import os
from django.http import HttpResponse
from docx import Document
from django.conf import settings
from weasyprint import HTML
from django.template.loader import render_to_string


def who_are_you_reporting(request):
    if request.method == 'POST':
        form = WhoAreYouReportingForm(request.POST)
        if form.is_valid():
            report_type = form.cleaned_data['report_type']
            
            # Redirect to the appropriate form based on user selection
            if report_type == 'solicitor':
                return redirect('solicitor_form')  # URL for solicitor (SRA) form
            elif report_type == 'barrister':
                return redirect('barrister_form')  # URL for barrister (BSB) form
            elif report_type == 'judge':
                return redirect('judge_form')  # URL for judge form
    else:
        form = WhoAreYouReportingForm()
    
    return render(request, 'complaints/who_are_you_reporting.html', {'form': form})

def classify_complaint(complaint_text):
    if "solicitor" in complaint_text.lower():
        return "solicitor"
    elif "barrister" in complaint_text.lower():
        return "barrister"
    elif "judge" in complaint_text.lower():
        return "judge"
    return "unknown"

def find_similar_cases(complaint_category, complaint_text):
    keywords = complaint_text.split()
    query = PastCase.objects.filter(category=complaint_category)
    
    q = Q()
    for keyword in keywords:
        q |= Q(keywords__icontains=keyword)
    
    query = query.filter(q)
    return query

def check_for_breaches(complaint_text):
    breaches = []
    if "CPR" in complaint_text:
        breaches.append("CPR Breach")
    if "human rights" in complaint_text:
        breaches.append("Human Rights Breach")
    if "rule of law" in complaint_text:
        breaches.append("Rule of Law Breach")
    return breaches

def populate_complaint_form(complaint_category, form_data, similar_cases):
    # Path to the form template based on the category
    template_path = os.path.join(settings.BASE_DIR, 'templates/forms/sra-form.docx')
    # if complaint_category == "solicitor":
    #     template_path = os.path.join(settings.BASE_DIR, 'templates/forms/sra-form.docx')
    # elif complaint_category == "barrister":
    #     template_path = os.path.join(settings.BASE_DIR, 'templates/forms/BSB_complaint_form.docx')
    # elif complaint_category == "judge":
    #     template_path = os.path.join(settings.BASE_DIR, 'templates/forms/GCIO_complaint_form.docx')
    # else:
    #     return None

    # Load the template
    doc = Document(template_path)

    # Function to replace placeholders in paragraphs
    def replace_text(paragraph, placeholder, value):
        if placeholder in paragraph.text:
            paragraph.text = paragraph.text.replace(placeholder, value)

    # Replace placeholders in paragraphs
    # for paragraph in doc.paragraphs:
    #     replace_text(paragraph, '<<TITLE>>', form_data['title'])
    #     replace_text(paragraph, '<<FIRST_NAME>>', form_data['first_name'])
    #     replace_text(paragraph, '<<LAST_NAME>>', form_data['last_name'])
    #     replace_text(paragraph, '<<FIRM>>', form_data['firm'] or 'N/A')
    #     replace_text(paragraph, '<<ADDRESS>>', form_data['address'])
    #     replace_text(paragraph, '<<PHONE_NUMBER>>', form_data['phone_number'])
    #     replace_text(paragraph, '<<EMAIL>>', form_data['email'])
    #     replace_text(paragraph, '<<REPORTED_PERSON_NAME>>', form_data['reported_person_name'])
    #     replace_text(paragraph, '<<REPORTED_FIRM_NAME>>', form_data['reported_firm_name'])
    #     replace_text(paragraph, '<<REPORTED_FIRM_ADDRESS>>', form_data['reported_firm_address'])
    #     replace_text(paragraph, '<<REPORTED_FIRM_PHONE>>', form_data['reported_firm_phone'])
    #     replace_text(paragraph, '<<ACTED_FOR_YOU>>', form_data['acted_for_you'])
    #     replace_text(paragraph, '<<ACT_FOR_ANOTHER_PERSON>>', form_data['act_for_another_person'])
    #     replace_text(paragraph, '<<SOLICITOR_ACTING_FOR>>', form_data['solicitor_acting_for'] or 'N/A')
    #     replace_text(paragraph, '<<COMPLAINT_TEXT>>', form_data['complaint'])
    #     replace_text(paragraph, '<<SIGNATURE>>', form_data['signature'])
    #     replace_text(paragraph, '<<DATE>>', form_data['date'].strftime("%d/%m/%Y"))

    # Replace placeholders inside tables
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for paragraph in cell.paragraphs:
                    replace_text(paragraph, '<<TITLE>>', form_data['title'])
                    replace_text(paragraph, '<<FIRST_NAME>>', form_data['first_name'])
                    replace_text(paragraph, '<<LAST_NAME>>', form_data['last_name'])
                    replace_text(paragraph, '<<FIRM>>', form_data['firm'] or 'N/A')
                    replace_text(paragraph, '<<ADDRESS>>', form_data['address'])
                    replace_text(paragraph, '<<PHONE_NUMBER>>', form_data['phone_number'])
                    replace_text(paragraph, '<<EMAIL>>', form_data['email'])
                    replace_text(paragraph, '<<ADJUSTMENTS>>', form_data['adjustments'] or 'N/A')
                    replace_text(paragraph, '<<INDIVIDUAL_ACTED_FOR>>', form_data['individual_acted_for'])
                    replace_text(paragraph, '<<REPORTED_PERSON_NAME>>', form_data['reported_person_name'])
                    replace_text(paragraph, '<<REPORTED_FIRM_NAME>>', form_data['reported_firm_name'])
                    replace_text(paragraph, '<<REPORTED_FIRM_ADDRESS>>', form_data['reported_firm_address'])
                    replace_text(paragraph, '<<REPORTED_FIRM_PHONE>>', form_data['reported_firm_phone'])
                    replace_text(paragraph, '<<ACTED_FOR_YOU>>', form_data['acted_for_you'])
                    replace_text(paragraph, '<<ACT_FOR_ANOTHER_PERSON>>', form_data['act_for_another_person'])
                    replace_text(paragraph, '<<INDIVIDUAL_ACTING_FOR>>', form_data['individual_acting_for'] or 'N/A')
                    replace_text(paragraph, '<<COMPLAINT_TEXT>>', form_data['complaint'])
                    replace_text(paragraph, '<<SIGNATURE>>', form_data['signature'])
                    replace_text(paragraph, '<<DATE>>', form_data['date'].strftime("%d/%m/%Y"))

    # Save the populated document
    populated_form_path = os.path.join(settings.MEDIA_ROOT, f'populated_{complaint_category}_complaint_form.docx')
    doc.save(populated_form_path)

    return populated_form_path


def submit_complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            complaint_text = form.cleaned_data['complaint']
            complaint_category = classify_complaint(complaint_text)

            if complaint_category == "unknown":
                return render(request, 'complaints/error.html', {
                    "error_message": "Complaint category could not be identified."
                })

            similar_cases = find_similar_cases(complaint_category, complaint_text)
            breaches = check_for_breaches(complaint_text)

            # Populate the appropriate complaint form
            populated_form_path = populate_complaint_form(complaint_category, form_data, similar_cases)

            # Render the results page, include path to the populated form
            return render(request, 'complaints/complaint_results.html', {
                "complaint_category": complaint_category,
                "similar_cases": similar_cases,
                "breaches": breaches,
                "complaint_text": complaint_text,
                "populated_form_path": populated_form_path,  # Pass the path for the download
            })
    else:
        form = ComplaintForm()

    return render(request, 'complaints/submit_complaint.html', {'form': form})

def download_form(request, file_path):
    """Serve the populated form as a downloadable file."""
    # Get the absolute path to the file in the media directory
    file_path = os.path.join(settings.MEDIA_ROOT, file_path)

    # Serve the document as a downloadable file
    return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=os.path.basename(file_path))


def jcio_form(request):
    if request.method == 'POST':
        form = JCIOForm(request.POST, request.FILES)
        if form.is_valid():
            # Create PDF from form data
            form_data = form.cleaned_data
            complaint_text = form.cleaned_data['complaint_details']
            complaint_category = classify_complaint(complaint_text)

            if complaint_category == "unknown":
                return render(request, 'complaints/error.html', {
                    "error_message": "Complaint category could not be identified."
                })

            similar_cases = find_similar_cases(complaint_category, complaint_text)
            breaches = check_for_breaches(complaint_text)
            html_string = render_to_string('complaints/jcio_pdf_template.html', {'form_data': form_data})
            pdf_file = HTML(string=html_string).write_pdf()

            # Save the PDF to the media directory
            pdf_filename = os.path.join(settings.MEDIA_ROOT, f'jcio_complaint_{form_data["your_name"]}.pdf')
            with open(pdf_filename, 'wb') as f:
                f.write(pdf_file)

            # Redirect to a success page or provide a download link
            return render(request, 'complaints/complaint_results.html', {
                "complaint_category": complaint_category,
                "similar_cases": similar_cases,
                "breaches": breaches,
                "complaint_text": complaint_text,
                "populated_form_path": pdf_filename,  # Pass the path for the download
            })  # Change to the correct URL
    else:
        form = JCIOForm()

    return render(request, 'complaints/jcio_form.html', {'form': form})

def barrister_form(request):
    if request.method == 'POST':
        form = BarristerForm(request.POST, request.FILES)
        if form.is_valid():
            # Create PDF from form data
            form_data = form.cleaned_data
            complaint_text = form.cleaned_data['event_information']
            complaint_category = classify_complaint(complaint_text)

            if complaint_category == "unknown":
                return render(request, 'complaints/error.html', {
                    "error_message": "Complaint category could not be identified."
                })

            similar_cases = find_similar_cases(complaint_category, complaint_text)
            breaches = check_for_breaches(complaint_text)
            html_string = render_to_string('complaints/barrister_pdf_template.html', {'form_data': form_data})
            pdf_file = HTML(string=html_string).write_pdf()

            # Save the PDF to the media directory
            pdf_filename = os.path.join(settings.MEDIA_ROOT, f'barrister_complaint_{form_data["barrister_name"]}.pdf')
            with open(pdf_filename, 'wb') as f:
                f.write(pdf_file)

            # Redirect to a success page or provide a download link
            return render(request, 'complaints/complaint_results.html', {
                "complaint_category": complaint_category,
                "similar_cases": similar_cases,
                "breaches": breaches,
                "complaint_text": complaint_text,
                "populated_form_path": pdf_filename,  # Pass the path for the download
            })  # Change to the correct URL
    else:
        form = BarristerForm()

    return render(request, 'complaints/barrister_form.html', {'form': form})


def success_page(request):
    return render(request, 'complaints/success.html')  #