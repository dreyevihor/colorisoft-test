from django.db import models
from collections import Counter
# Create your models here.

class Note(models.Model):
    class Meta:
        ordering = ['-count_unique_words']

    text = models.TextField()
    count_unique_words = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        def clear_from_token(string):
            syn_tokens = '.,/?!@#$%^&*()_-=+~`<>\'"|'
            str_res = string
            for token in syn_tokens:
                    str_res = str_res.replace(token, '') 
            return(str_res)
        copy_text = clear_from_token(self.text)
        self.count_unique_words = len(Counter(copy_text.split(' ')))
        super().save(*args, **kwargs)
