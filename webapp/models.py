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
    @staticmethod
    def get_session(s_id):
        return Artifacts.objects.filter(session_id=s_id)

    # deletes all artifacts of a session
    @staticmethod
    def delete_session(s_id):
        Artifacts.objects.filter(session_id=s_id).delete()

    # returns the latest session number
    @staticmethod
    def get_last_session_id():
        return Artifacts.objects.all().last().session_id


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

    # returns a criterion from the search criteria list
    @staticmethod
    def get_criterion(c_id):
        return SearchCriteria.objects.get(criterion_id=c_id)

    # deletes a criterion from search criteria list
    @staticmethod
    def delete_criterion(c_id):
        SearchCriteria.objects.get(criterion_id=c_id).delete()

    # sets a criterion to use for the next search session
    @staticmethod
    def set_criterion_to_use(c_id):
        criterion = SearchCriteria.objects.get(criterion_id=c_id)
        criterion.in_use = True
        criterion.save()

    # returns a criterion to use for the next search session
    @staticmethod
    def get_criterion_to_use():
        return SearchCriteria.objects.get(in_use=True)

    # resets a criterion to out of use
    @staticmethod
    def reset_criterion_to_use():
        criterion = SearchCriteria.objects.get(in_use=True)
        criterion.in_use = False
        criterion.save()


class SearchCriteria(models.Model):
    criterion_id = models.AutoField(primary_key=True)
    criterion = models.CharField(max_length=255)
    in_use = models.BooleanField(default=False)

    def __str__(self):
        return self.criterion
