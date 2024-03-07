from django.db import models


class Draw(models.Model):
    """ Class to handle our Draw model and table """
    name = models.CharField(max_length=50)
    creation_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} runned on the {self.creation_time}"


class DrawResult(models.Model):
    """ Class to handle our DrawResult model and table """
    draw = models.ForeignKey(Draw, on_delete=models.CASCADE, related_name='draw_result')
    giver = models.CharField(max_length=100)
    receiver = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.giver} offers to {self.receiver}"