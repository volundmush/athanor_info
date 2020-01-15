from django.db import models


class InfoFile(models.Model):
    object = models.ForeignKey('objects.ObjectDB', related_name='notes', on_delete=models.CASCADE)
    category = models.CharField(max_length=255, null=False, blank=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    iname = models.CharField(max_length=255, null=False, blank=False)
    contents = models.TextField(blank=False, null=False)
    date_created = models.DateTimeField(null=False)
    date_modified = models.DateTimeField(null=False)
    approved_by = models.ForeignKey('objects.ObjectDB', related_name='approved_notes', on_delete=models.PROTECT, null=True)

    class Meta:
        unique_together = (('object', 'category', 'iname'),)
        verbose_name = 'InfoFile'
        verbose_name_plural = 'InfoFiles'
