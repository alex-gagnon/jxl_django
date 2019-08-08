import os

from .create_excel_file import CreateExcelFile, FILE_PATH
from .jira_project_issues import JiraProjectIssues


class JXL:
    issues = []

    def __init__(self, *args, **kwargs):
        self.__url = kwargs.get('url')
        self.__user = kwargs.get('user')
        self.__pwd = kwargs.get('pwd')
        self.__jira_vals = {
            'url': self.__url,
            'username': self.__user,
            'password': self.__pwd
        }

        self.project = kwargs.get('project')
        self.filter_by = kwargs.get('filter_by')
        self.version = kwargs.get('version')

        # Initialize JiraProjectIssues
        self.JPI = JiraProjectIssues(**self.__jira_vals, project=self.project)

    def __str__(self):
        return f"JXL(project={self.project}, filter_by={self.filter_by}, version={self.version})"

    def __call__(self, *args, **kwargs):
        self.project = kwargs.get('project')
        self.filter_by = kwargs.get('filter_by')
        self.version = kwargs.get('version')

    def get_filtered_jira_issues(self):
        """Returns filtered Jira issues"""
        filter_function = {'fix_version': self._by_detailed_fix_version,
                           'latest_version': self._by_latest_version}

        self.issues = filter_function[self.filter_by]()

        print(self.issues)

        return self.issues

    def _by_detailed_fix_version(self):
        """Filter issues by fix version with a more detailed return"""
        fix_version_issues = self.JPI.filter_by_fix_version(fix_version=self.version)
        detailed_issues = self.JPI.detailed_filter_by_fix_version(fix_version_issues)
        print(FILE_PATH)
        return detailed_issues

    def _by_latest_version(self):
        """Filter issues by latest version"""
        return self.JPI.filter_by_latest_version_delivered(latest_version=self.version)

    def write_data(self):
        """Write issues to an excel file and return latest file name"""
        filename = f'{self.project} {self.version}'
        excel = CreateExcelFile(filename=filename,
                                sheetname=self.version)
        excel.create_excel_book(data_list=self.issues)
        latest_file = excel.get_recent_file()

        return latest_file

    @staticmethod
    def download(latest_file):
        """Download the latest file"""
        return {"Successful": 200,
                "directory": FILE_PATH,
                "filename": latest_file,
                "filepath": os.path.join(FILE_PATH, latest_file)}
