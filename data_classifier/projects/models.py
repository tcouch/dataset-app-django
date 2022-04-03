from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField()


class Dataset(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()


class Participant(models.Model):
    PROJECT_MANAGER = "PM"
    RESEARCHER = "RE"
    ADMINISTRATOR = "AD"
    ROLE_CHOICES = [
        (PROJECT_MANAGER, "Project Manager"),
        (RESEARCHER, "Researcher"),
        (ADMINISTRATOR, "Administrator"),
    ]
    role = models.CharField(
        max_length=50,
        choices=ROLE_CHOICES,
        default=RESEARCHER,
    )

    user = models.ForeignKey(
        User, related_name="participants", on_delete=models.CASCADE
    )

    project = models.ForeignKey(
        Project, related_name="participants", on_delete=models.CASCADE
    )

    class Meta():
        unique_together = ("user", "project")


class WorkPackage(models.Model):
    NEW = "N"
    UNDERWAY = "U"
    COMPLETED = "C"
    STATUS_CHOICES = [
        (NEW, "New"),
        (UNDERWAY, "Underway"),
        (COMPLETED, "Completed"),
    ]
    status = models.CharField(
        max_length=32,
        choices=STATUS_CHOICES,
        default=NEW,
    )
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="work_packages"
    )
    name = models.CharField(max_length=256)
    description = models.TextField()
    participants = models.ManyToManyField(
        Participant,
        related_name="work_packages",
        through="WorkPackageParticipant",
        blank=True,
    )
    datasets = models.ManyToManyField(
        Dataset, related_name="work_packages", blank=True
    )


class WorkPackageParticipant(models.Model):
    work_package = models.ForeignKey(
        WorkPackage, related_name="work_package_participants", on_delete=models.CASCADE
    )
    participant = models.ForeignKey(
        Participant, related_name="+", on_delete=models.CASCADE
    )

    class Meta():
        unique_together = ("participant", "work_package")