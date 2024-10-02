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
