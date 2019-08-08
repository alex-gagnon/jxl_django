import os

from dotenv import load_dotenv

load_dotenv()

auth = {'url': os.environ.get('JIRA_URL'),
        'user': os.environ.get('JIRA_USER'),
        'pwd': os.environ.get('JIRA_PASSWORD')}
