from django.db import models

class Message(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    email = models.EmailField()
    message = models.TextField()
    issued = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return self.name