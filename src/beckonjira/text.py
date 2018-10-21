import re
from datetime import datetime

from .config import PREFIX_BROWSE_URL, PREFIX_REST_URL

# pylint: disable=unused-import
from .models import JiraIssueType, JiraTicket

BASE_NUMBER_PATTERN = re.compile(r"BASE-\d+", flags=re.IGNORECASE)


def normalize_ticket(name: str) -> str:
    """Returns a norlized Jira Ticket Number
    NAME can be an url or base prefix or 5 digits

    >>> normalize_ticket('base-12345')
    'BASE-12345'

    >>> normalize_ticket('12345')
    'BASE-12345'

    # pylint: disable=line-too-long
    >>> normalize_ticket('https://beckon.atlassian.net/projects/BASE/issues/BASE-14883?filter=myopenissues&orderby=priority%20DESC')
    'BASE-14883'

    >>> normalize_ticket('whatever')
    Traceback (most recent call last):
        ...
    ValueError: whatever is not a valid Jira ticket
    """
    if len(name) == 5 and name.isdigit():
        return f"BASE-{name}"

    matched = BASE_NUMBER_PATTERN.search(name)

    if matched:
        return matched.group(0).upper()

    raise ValueError(f"{name} is not a valid Jira ticket")


def build_rest_url(name: str) -> str:
    """Given a NAME, normalized jira ticket,
    returns REST API ENDPOINT

    >>> build_rest_url('BASE-12345')
    'https://beckon.atlassian.net/rest/api/2/issue/BASE-12345'
    """
    return f"{PREFIX_REST_URL}/issue/{name}"


def build_browse_url(name: str) -> str:
    """Same as `build_rest_url` but returns an webpage
    >>> build_browse_url('BASE-12345')
    'https://beckon.atlassian.net/browse/BASE-12345'
    """
    return f"{PREFIX_BROWSE_URL}/{name}"


def clean_text(name: str) -> str:
    """Remove all special characters and replace any space by hypen.
    So, it should create a sort of URL friendly name

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
    """Given `ticket_info`, returns a full prospective branch name

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
