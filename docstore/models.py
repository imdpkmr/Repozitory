from django.db import models
from django.core.urlresolvers import reverse


class Artifact(models.Model):
    docname = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    remark = models.CharField(max_length=250)
    artifact_file = models.FileField()

    def get_absolute_url(self):
        return reverse('docstore:detail',kwargs = {'pk':self.pk})

    def __str__(self):
        return self.docname
