from django.db import models
    

class Lead(models.Model):

    SOURCE_CHOICES = (
        ('YouTube', 'YouTube'),
        ('Facebook', 'Facebook'),
        ('Google', 'Google'),
        ('Newsletter', 'Newsletter'),
    )

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField(default=18)
    agent = models.ForeignKey("Agent", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Agent(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)