from django.db import models

class Tuite(models.Model):
    content = models.CharField('Tuite', max_length=280)
    author = models.ForeignKey('users.User', verbose_name='Autor', on_delete=models.CASCADE, related_name='tuites')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.username}: {self.content}'

    class Meta:
        ordering = ('-date_created', )