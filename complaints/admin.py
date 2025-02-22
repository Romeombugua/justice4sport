from django.contrib import admin
from .models import PastCase
from .models import Submission, Document, DocumentChunk

admin.site.register(PastCase)
admin.site.register(Submission)
admin.site.register(Document)
admin.site.register(DocumentChunk)
