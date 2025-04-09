from django.db import models

from django.utils import timezone


class Contact(models.Model):
    """
    Model to store contact requests from users.
    """
    class Meta:
        verbose_name_plural = 'Contact Requests'

    SUBJECTS = (
        ('Games with Hard Complexity', 'Games with Hard Complexity'),
        ('Pricing Inquiry', 'Pricing Inquiry'),
        ('Trouble buying the game', "Trouble buying the game"),
        ('Account Issues', "Account Issues"),
        ('Other', "Other"),
    )

    name = models.CharField(max_length=254)
    email = models.EmailField()
    subject = models.CharField(choices=SUBJECTS, max_length=254,)
    message = models.TextField(max_length=1024)
    date_created = models.DateTimeField(default=timezone.now)
    responded = models.BooleanField(default=False)

    def __str__(self):
        return self.email


class Faq(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question
