import re
from datetime import datetime

from .config import PREFIX_BROWSE_URL, PREFIX_REST_URL

# pylint: disable=unused-import
from .models import JiraIssueType, JiraTicket


def normalize_ticket(name: str) -> str:
    """
    >>> normalize_ticket('base-12345')
    'BASE-12345'

    >>> normalize_ticket('12345')
    'BASE-12345'
    """
    name = name.split("/")[-1]

    if len(name) == 5:
        name = "BASE-" + name
    return name.upper()


def build_url(name: str) -> str:
    """
    >>> build_url('BASE-12345')
    'https://beckon.atlassian.net/rest/api/2/issue/BASE-12345'
    """
    return f"{PREFIX_REST_URL}/issue/{name}"


def build_browse_url(name: str) -> str:
    """
    >>> build_browse_url('BASE-12345')
    'https://beckon.atlassian.net/browse/BASE-12345'
    """
    return f"{PREFIX_BROWSE_URL}/{name}"


def clean_text(name: str) -> str:
    """
    >>> clean_text("Large Text")
    'large-text'

    >>> clean_text("cb3: spider and polar")
    'cb3-spider-and-polar'
    """
    name = name.lower()
    name = re.sub("[^A-Za-z0-9 ]+", "", name)
    name = re.sub(r"\s+", "-", name)
    return name


def build_branch_name(ticket_info: JiraTicket) -> str:
    """
    >>> issue_type = JiraIssueType(name="Bug",     \
                                   avatarId='',    \
                                   description='', \
                                   iconUrl='',     \
                                   id='',          \
                                   self_='',       \
                                   subtask='')
    >>> ticket_info = JiraTicket(name="BASE-12345",                \
                                 summary="cb3: chartbuilder test", \
                                 issue_type=issue_type,            \
                                 url='')
    >>> build_branch_name(ticket_info)
    'bug/.../BASE-12345-cb3-chartbuilder-test'
    """
    issue_type = clean_text(ticket_info.issue_type.name)
    date = datetime.now().strftime("%Y%m%d")
    summary = clean_text(ticket_info.summary)
    ticket_name = ticket_info.name

    return f"{issue_type}/{date}/{ticket_name}-{summary}"
