from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from .models import Artifacts, ArchiveManager, SearchCriteria, CriteriaManager
from django.views.decorators.http import require_http_methods
from urllib.request import urlopen
import os, shutil
from .crawler.crawler import *


# i.e. test home page
# def start_session(request, search_criterion_id):
def start_session(request):
    execute_session()
    return HttpResponse("Session created!")


def delete_session(request, session_id):
    ArchiveManager.delete_session(session_id)
    return HttpResponse("deleted session: " + str(session_id))


def check_last_session_index(request):
    unique_session_indexes = ArchiveManager.get_unique_sessions()
    return JsonResponse(unique_session_indexes)

# Redirected page of artifact
@require_http_methods(["GET", "POST"])
def view_artifact(request, artifact_id):
    try:
        artifact = ArchiveManager.get_artifact(artifact_id)
        webpage = artifact.artifact_url

        # remove "https://" when real urls are stored
        return HttpResponseRedirect("https://" + webpage)

    except Artifacts.DoesNotExist:
        raise Http404("Website does not exist")


# Page that returns artifacts of a particular session
@require_http_methods(["GET", "POST"])
def get_session(request, session_id):
    try:
        artifact_list = ArchiveManager.get_session(session_id)
        # output = ',\n'.join([a.artifact_url for a in artifact_list])
        output = {}
        i = 0

        for a in artifact_list:
            output[i] = a.artifact_url
            i += 1

        return JsonResponse(output)

    except Artifacts.DoesNotExist:
        raise Http404("Session does not exit")


# Page that returns search criteria list
@require_http_methods(["GET", "POST"])
def get_search_criteria(request):
    try:
        criteria_list = CriteriaManager.get_criteria()
        # output = ',\n'.join([c.criterion for c in criteria_list])
        output = {}
        i = 0

        for c in criteria_list:
            output[i] = c.criterion
            i += 1

        return JsonResponse(output)

    except SearchCriteria.DoesNotExist:
        raise Http404("Search Criteria does not exit")

# Page that allows user to add search criteria list & returns updated search criteria list
@require_http_methods(["GET", "POST"])
def add_search_criteria(request, new_criterion):
    try:
        criterion = new_criterion
        CriteriaManager.create_criterion(criterion)

        return get_search_criteria(request)

    except SearchCriteria.DoesNotExist:
        raise Http404("Search Criteria does not exit")


# Page that allows user to remove search criteria list & returns updated search criteria list
@require_http_methods(["GET", "POST"])
def remove_search_criteria(request, criterion_to_remove):
    try:
        CriteriaManager.delete_criterion(criterion_to_remove)

        return get_search_criteria(request)

    except SearchCriteria.DoesNotExist:
        raise Http404("Search Criteria does not exit")


# Function to start a session, receive artifact url list from scrapy, and store the url's in the DB
# def execute_session(search_criteria_id):
def execute_session():
    try:
        # CriteriaManager.reset_criterion_to_use()
        # CriteriaManager.set_criterion_to_use(search_criteria_id)
        run_crawler()

    except OSError:
        # display error message
        return False
    else:
        return True


# Function to save artifact HTML file to local file reserve directory
def save_artifact_to_file(filename, artifact_url):

    # prompt tagging options

    try:
        # extract HTML file via url
        url = artifact_url
        response = urlopen(url)  # change to urllib2
        web_content = response.read()

        # write webpage content to file & save
        f = open(filename + ".html", "w")
        f.write(web_content)
        f.close()

    except IOError:
        # display error message
        return False
    else:
        return True


