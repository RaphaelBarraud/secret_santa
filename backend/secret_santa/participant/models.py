from django.db import models

class Participant(models.Model):
    """ Class to handle our Participant model and table """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    # Create the constraint to insure participants with different names
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['first_name', 'last_name'], name='unique_name'
            ),
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}" 


class Blacklist(models.Model):
    """ Class to handle our Blacklist model and table """
    owner = models.ForeignKey(
                    Participant, on_delete=models.CASCADE, related_name='blacklist')
    blacklisted = models.ForeignKey(
                    Participant, on_delete=models.CASCADE, related_name='blacklisted')

    def __str__(self):
        return f"{self.blacklisted.first_name} {self.blacklisted.last_name}"
