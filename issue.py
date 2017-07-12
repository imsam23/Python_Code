#!/usr/bin/env python
import requests
import re
import sys
import json
from Jira_Connection import *
from authentication import *
import pprint
import logging

logger = logging.getLogger('issue')

#For parsing the JSON data retrived from authenticateGetData_sky
class Issue:

    _issue = None

    def __init__(self, issue):
        self._issue = issue

    def key(self):
        return self._issue['key']

    def project(self):
        return self._issue['fields']['project']['key']

    def type(self):
        return self._issue['fields']['issuetype']['name']

    def defect_version(self):
        if self._issue['fields']['customfield_10013']==None:
            return None
        else:
            return self._issue['fields']['customfield_10013']['value']

    def components(self):
        if len(self._issue['fields']['components'])==0:
            return None
        else:
            return self._issue['fields']['components'][0]['name']

    def fixVersions(self):
        if len(self._issue['fields']['fixVersions'])==0:
            return None
        else:
            return self._issue['fields']['fixVersions'][0]['name']

    def title(self):
        title = self._issue['fields']['summary'].encode('ascii', 'ignore').replace('"', "'")
        return title

    def description(self):
        description = self._issue['fields']['description'].encode('ascii', 'ignore').replace('"', "'")
        return description

    def priority(self):
        priority = self._issue['fields']['priority']['name']
        if priority=='Very High':
            priority='Blocker'
        elif priority=='High':
            priority='Critical'
        elif priority=='Medium':
            priority='Major'
        elif priority=='Low':
            priority='Minor'
        else:
            pass
        return priority

    def assignee(self):
        if self._issue['fields']['assignee'] is not None:
            return self._issue['fields']['assignee']['displayName']
        return "No assignee"

    def dueDate(self):
        return str(self._issue['fields']['duedate'])

    def createdDate(self):
        return self._issue['fields']['created'].split('T')[0]

    def lastUpdated(self):
        return self._issue['fields']['updated']

    def labels(self):
        return self._issue['fields']['labels']

    def hasLabel(self, label):
        return label in self._issue['fields']['labels']


def search_project_issues(key):

    allIssues = [];
    total = -1
    issues, total = authenticateGetData_sky(key)
    logger.info("Resp - issues: "+str(len(issues))+", total:"+str(total))

    issueObjects = []
    for issue in issues:
        issueObjects.append(Issue(issue))
    return issueObjects,total