from django.contrib import admin

from data_classifier.projects import models

admin.site.register(models.Project)
admin.site.register(models.Dataset)
admin.site.register(models.Participant)
admin.site.register(models.WorkPackage)
admin.site.register(models.WorkPackageParticipant)
