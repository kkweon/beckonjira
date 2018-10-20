import json
from typing import Tuple

import boto3

s3 = boto3.client("s3")


def get_name() -> str:
    return "Hello, World"


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
