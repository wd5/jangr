from django.db import models

class UploadModel(models.Model):
    title = models.CharField(max_length=64, blank=True)
    file = models.FileField(upload_to='')

    @property
    def filename(self):
        return self.file.name.rsplit('/', 1)
