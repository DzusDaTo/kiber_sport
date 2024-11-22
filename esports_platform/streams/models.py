from django.db import models


class Stream(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    is_live = models.BooleanField(default=False)

    def __str__(self):
        return self.title
