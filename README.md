# JXL
Django implementation of JXL to get filtered data from Jira and write values to an excel file.

## Instructions
* Make sure postgres is installed, else an error will occur for pg_config when installing psycopg2.
  * https://help.ubuntu.com/lts/serverguide/postgresql.html
    * use nautilus to open file directory to enable editing
  * Make sure .ebextensions has a .config file with the following:
    * ```yaml
    packages:
      yum:
        git: []
          postgresql93-devel: []
          libjpeg-turbo-devel: []```
      * More info: https://realpython.com/deploying-a-django-app-and-postgresql-to-aws-elastic-beanstalk/#configure-eb-initialize-your-app
* Start postgresql
  * ```systemctl start postgresql```
  * ```systemctl enable postgresql```
* Install requirements.txt
  * ```pip install .```
* Install geckodriver for selenium
  * download
    * ```wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz```
  * Extract
    * ```tar -xvzf geckodriver*```
  * Make it executable
    * ```chmod +x geckodriver```
  * Add driver to PATH
    * ```sudo mv geckodriver /usr/local/bin```
