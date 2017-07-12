#!/usr/bin/env python
import requests
import json
from Jira_Connection import *
import base64
import sys
import logging

logger = logging.getLogger('sky_jira')

#To authenticate the abc server and get the data in JSON format from the server
def authenticateGetData_sky(key):
    url = jiraUrl + '/search?startAt=' + str(startAt) + '&maxResults=' + str(maxResults) + '&jql=project=' + str(projectId) + ' and issuetype=' + str(issuetype) + ' and Key>' + str(key) + ' ORDER BY key ASC'
    logger.debug(url)
    with requests.session() as session:
        session.cert=(cert,key_file)
        session.auth=(username,base64.urlsafe_b64decode(password_sky))
        response=session.get(url)
        logger.info("server responded with status :" + str(response.status_code))

    if response.status_code == 200:
        json_data = response.json()
        return json_data['issues'],json_data['total']
    else:
        logger.error("The JIRA server failed to reply correctly (HTTP status): " + str(response.status_code))
        exit(1)


