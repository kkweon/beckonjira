import json
from typing import Tuple

import boto3
import requests

from .models import JiraIssueTypeFactory, JiraTicket
from .text import build_browse_url, build_url

s3 = boto3.client("s3")


def get_jira_auth() -> Tuple[str, str]:
    """
    >>> get_jira_auth()
    ('beckonbot', '...')
    """
    jira_auth = json.loads(
        s3.get_object(
            Bucket="beckon-devops", Key="credentials/beckon_credentials.json"
        )["Body"].read()
    ).get("jira", {})

    return jira_auth.get("user", ""), jira_auth.get("password", "")


def get_ticket_info(name: str) -> JiraTicket:
    """
    >>> ticket_info = get_ticket_info("BASE-12345")
    >>> ticket_info
    JiraTicket(name='BASE-12345',
               issue_type=JiraIssueType(...),
               summary='CB3: Spider and polar charts has label that is obstructed and punch to edit showing',
               url='https://beckon.atlassian.net/browse/BASE-12345')
    """
    ticket_url = build_url(name)
    res = requests.get(ticket_url, auth=get_jira_auth()).json()
    issue_type = JiraIssueTypeFactory(**res["fields"]["issuetype"])
    summary = res["fields"]["summary"]
    browse_url = build_browse_url(name)

    return JiraTicket(name=name, issue_type=issue_type, summary=summary, url=browse_url)
