from django.db import models


# Create your models here.
class UniversityCampus(models.Model):
    #   Set up the various fields we need for this object. Ties it to our db as well.
    campus_name = models.CharField(max_length=60, default="", blank=True, null=False)
    campus_state = models.CharField(max_length=2, default="", blank=True, null=False)
    #   Here, I actually use the primary key field to indicate the Campus ID will be that field.
    #   This is normally made default for us, but we're specifying, so let's do that.
    campus_id = models.IntegerField(default="", blank=True, null=False, primary_key=True)

    #   It shows up pretty ugly on the admin panel if I don't set the string up...
    def __str__(self):
        display_campus = '{0.campus_name}'
        return display_campus.format(self)

    #   This just tells the system to restrict the plurilisation or display it how I want
    class Meta:
        verbose_name_plural = "University Campus"
