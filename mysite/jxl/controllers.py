import os

from dotenv import load_dotenv

from mysite.jxl.services import JXL

load_dotenv()


def download_xls(data):
    auth = {'url': os.environ.get('JIRA_URL'),
            'user': os.environ.get('JIRA_USER'),
            'pwd': os.environ.get('JIRA_PASSWORD')}
    project = {'project': data.get('project'),
               'filter_by': data.get('filter_by'),
               'version': data.get('version')}
    response = JXL(**auth, **project)
    response.get_filtered_jira_issues()

    return response.download(response.write_data())


if __name__ == '__main__':
    d = {'project': 'TM',
         'filter_by': 'fix_version',
         'version': '10.4'}
    print(download_xls(d))
