from typing import NamedTuple


class JiraIssueType(NamedTuple):
    avatarId: str
    description: str
    iconUrl: str
    id: str
    name: str
    self_: str
    subtask: bool


def JiraIssueTypeFactory(**kwargs) -> JiraIssueType:
    return JiraIssueType(
        avatarId=kwargs.get("avatarId", ""),
        description=kwargs.get("description", ""),
        iconUrl=kwargs.get("iconUrl", ""),
        id=kwargs.get("id", ""),
        name=kwargs.get("name", ""),
        self_=kwargs.get("self", ""),
        subtask=kwargs.get("subtask", False),
    )


class JiraTicket(NamedTuple):
    name: str
    issue_type: JiraIssueType
    summary: str
    url: str
