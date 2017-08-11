#!/usr/bin/env python
#info for base url for CISOC and SKY JIRA

jiraBaseUrl_sky ='https://www.abc.com/jira/rest/api/'
jiraRestVersion = 'latest'
jiraUrl=jiraBaseUrl + jiraRestVersion
startAt=0
maxResults=1000
FirstJira='JRA-2'



#generate cert and key_file from user.p12 using SSL cmd described in READMEE.txt
cert = "certificate.pem"
key_file = "keys.pem"

#user credentials info
#convert username and password in base64 encoded value
username = "username"
password_sky = "password"


#Filter to query JIRA
#use the projectId and issuetype accordingly
projectId='ProjectId'
issuetype='Bug'
