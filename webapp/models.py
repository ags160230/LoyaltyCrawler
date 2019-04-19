from django.db import models
from django.utils import timezone


# This manager retrieves artifacts belonging to a particular session
class ArchiveManager(models.Manager):
    # creates an artifact (a tale record) belonging to a particular session
    @staticmethod
    def create_artifact(s_id, a_url):
        artifact = Artifacts(session_id=s_id, artifact_url=a_url, retrieval_date=timezone.now())
        artifact.save()

    # returns particular artifact via id
    @staticmethod
    def get_artifact(a_id):
        return Artifacts.objects.get(artifact_id=a_id)

    # returns artifacts belonging to a particular session
    # use session[i] to refer to artifact i
    @staticmethod
    def get_session(s_id):
        return Artifacts.objects.filter(session_id=s_id)


# This manager deletes a session
class UpdateManager(models.Manager):
    # deletes all artifacts of a session
    @staticmethod
    def delete_session(s_id):
        Artifacts.objects.filter(session_id=s_id).delete()


class Artifacts(models.Model):
    session_id = models.IntegerField()
    artifact_id = models.AutoField(primary_key=True)
    artifact_url = models.CharField(max_length=255)
    retrieval_date = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return self.artifact_url


# This manager deletes criteria from the search criteria list
class CriteriaManager(models.Manager):
    # deletes a criterion for search criteria list
    @staticmethod
    def create_criterion(c):
        criterion = SearchCriteria(criterion=c)
        criterion.save()

    # returns search criteria list
    @staticmethod
    def get_criteria():
        return SearchCriteria.objects.all()

    # deletes a criterion from search criteria list
    @staticmethod
    def delete_criterion(c_id):
        SearchCriteria.objects.filter(criterion_id=c_id).delete()


class SearchCriteria(models.Model):
    criterion_id = models.AutoField(primary_key=True)
    criterion = models.CharField(max_length=255)

    def __str__(self):
        return self.criterion
