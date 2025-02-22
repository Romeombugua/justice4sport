from django.db import models

class PastCase(models.Model):
    CATEGORY_CHOICES = [
        ('solicitor', 'Solicitor'),
        ('barrister', 'Barrister'),
        ('judge', 'Judge')
    ]

    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    case_summary = models.TextField()
    keywords = models.TextField()

    def __str__(self):
        return f"{self.category} case: {self.case_summary[:50]}"


class Submission(models.Model):
    site = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=200, blank=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.site} - {self.name}"
    
class Document(models.Model):
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)

class DocumentChunk(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    content = models.TextField()
    embedding = models.BinaryField()
    chunk_index = models.IntegerField()