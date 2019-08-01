# JXL
Django implementation of JXL to get filtered data from Jira and write values to an excel file.

## Instructions
* Make sure postgres is installed, else an error will occur for pg_config when installing psycopg2.
  * ```brew install postgresql```
  * Troubleshoot: https://stackoverflow.com/questions/11618898/pg-config-executable-not-found
  * Make sure .ebextensions has a .config file with the following:
    * ```yaml
    packages:
      yum:
        git: []
          postgresql93-devel: []
          libjpeg-turbo-devel: []```
      * More info: https://realpython.com/deploying-a-django-app-and-postgresql-to-aws-elastic-beanstalk/#configure-eb-initialize-your-app 
