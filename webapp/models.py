from django.db import models


# This manager retrieves artifacts belonging to a particular session
class ArchiveManager(models.Manager):
    # returns artifacts belonging to a particular session
    @staticmethod
    def get_session(s_id):
        return Artifacts.objects.filter(session_id=s_id)

    # i.e. get_session
    # def get_queryset(self, s_id):
    #    return super().get_queryset().filter(session_id=s_id)


# This manager stores artifacts belonging to a particular session
class SessionManager(models.Manager):
    # creates an artifact (a tale record) belonging to a particular session
    @staticmethod
    def create_artifact(s_id, a_url):
        session = Artifacts(session_id=s_id, artifact_url=a_url)
        session.save()


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
    # particular_session_artifacts = ArchiveManager()
