from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Artifacts, ArchiveManager, UpdateManager, SearchCriteria, CriteriaManager
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect
import urllib #check urllib2
import os

# Variable to record number of sessions created & value to increment for new session id
session_index = 0


# i.e. test home page
def home(request):
    return HttpResponse("You're at the Loyalty Crawler home page!")


# Redirected page of artifact
@require_http_methods(["GET", "POST"])
def view_artifact(request, artifact_id):
    try:
        artifact = ArchiveManager.get_artifact(artifact_id)
        webpage = artifact.artifact_url
        # remove "https://" when real urls are stored
        return redirect("https://" + webpage)
    except Artifacts.DoesNotExist:
        raise Http404("Session does not exit")


# Page that returns artifacts of a particular session
@require_http_methods(["GET", "POST"])
def get_session(request, session_id):
    try:
        artifact_list = ArchiveManager.get_session(session_id)
        output = ',\n'.join([a.artifact_url for a in artifact_list])
    except Artifacts.DoesNotExist:
        raise Http404("Session does not exit")

    return HttpResponse(output)


# Page that returns search criteria list
@require_http_methods(["GET", "POST"])
def get_search_criteria(request):
    try:
        criteria_list = CriteriaManager.get_criteria()
        output = ',\n'.join([c.criterion for c in criteria_list])
    except SearchCriteria.DoesNotExist:
        raise Http404("Search Criteria does not exit")

    return HttpResponse(output)


# Page that allows user to edit search criteria list & returns updated search criteria list
@require_http_methods(["GET", "POST"])
def edit_search_criteria(request):
    criteria_list = CriteriaManager.get_criteria()

    # GUI interaction to create criterion or delete criterion
    # user selects option to add or delete criterion | i.e True = add, False = delete

    edit_action = True

    try:
        if edit_action:
            # user enters criterion to be added
            criterion = "criterion here"
            CriteriaManager.create_criterion(criterion)
        else:
            # user selects criterion to delete | example criterion_id = 1 = criterion_list[0]
            criterion_id = 0
            CriteriaManager.delete_criterion(criterion_id)
    except SearchCriteria.DoesNotExist:
        raise Http404("Search Criteria does not exit")

    return get_search_criteria(request)


# Function to start a session, receive artifact url list from scrapy, and store the url's in the DB
def execute_session(search_criteria):
    session_id = session_index + 1

    # start session (i.e. use scrapy library to start web scraping/parsing utilizing search_criteria)

    artifact_list = ["url_1", "url_2", "url_3"]     # list of urls returned by scrapy

    # use manager to save artifacts in DB
    for a in artifact_list:
        ArchiveManager.create_artifact(session_id, a)

    # variable to return session execution status | True = success, False = failure
    # replace with try/except later
    execution_code = True

    if execution_code:
        return True
    else:
        return False


# Function to save artifact HTML file to local file reserve directory
def save_artifact_to_file(filename, artifact_url):

    # prompt tagging options

    try:
        # extract HTML file via url
        url = artifact_url
        response = urllib.urlopen(url)  # change to urllib2
        web_content = response.read()

        # write webpage content to file & save
        f = open(filename + ".html", "w")
        f.write(web_content)
        f.close()

        return True
    except IOError:
        # display error message
        return False


# Function to create a local file reserve directory
def create_directory(directory_name):
    try:
        os.mkdir(directory_name)
        return True
    except FileExistsError:
        # display error message
        return False


