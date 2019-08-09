# JXL
Django implementation of JXL to get filtered data from Jira and write values to an excel file.

## Instructions
### Automated
* Run ***installation/ubuntu_postgresql_setup.sh*** bash script to download postgresql, it's required files, start it, check to make
sure it's port is listening
* Run ***installation/ubuntu_geckodriver_install.sh*** bash script to download Firefox geckodriver and
add it's executable to PATH
* ```python myscript/manage.py makemigrations jxl```
* ```python myscript/manage.py migrate jxl```
* ```python myscript/manage.py test jxl```
* ```python myscript/manage.py runserver```
* ```python tests/functional_tests.py```

### Manual
* Follow these steps to install postgresql (on Ubuntu 18.04)
  * https://help.ubuntu.com/lts/serverguide/postgresql.html
    * Use nautilus to open file directory to enable editing of **postgresql.conf** and **pg_hba.conf**
      * If these files are edited while postgresql is running, postgresql will require a restart
        * ```sudo systemctl restart postgresql```
  * If deploying to AWS Elastic Beanstalk, make sure .ebextensions has a .config file with the following:
    * ```yaml
    packages:
      yum:
        git: []
          postgresql93-devel: []
          libjpeg-turbo-devel: []```
      * More info: https://realpython.com/deploying-a-django-app-and-postgresql-to-aws-elastic-beanstalk/#configure-eb-initialize-your-app
* Start postgresql
  * ```sudo systemctl start postgresql```
  * ```sudo systemctl enable postgresql```
* Ensure postgresql is running and has access to network
  * ```sudo service postgresql status``` - should return as active
  * ```sudo netstat -nl | grep postgresql``` - should return a stream
    * If nothing is returned make sure listen_addresses in **/etc/postgresql/10/mainpostgresql.conf** are
    not commented out (this is by default) and address is correct (or use * for all addresses).
      * Make sure **pg_hba.conf** has a line to set which computers can connect to server
        * host  all  all  127.0.0.1/24  all
    * https://stackoverflow.com/questions/38466190/cant-connect-to-postgresql-on-port-5432
* Install requirements.txt after postgresql has been installed
  * ```pip install -r requirements.txt```
* Install geckodriver for selenium to access Firefox
  * Download
    * ```wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz```
  * Extract
    * ```tar -xvzf geckodriver*```
  * Make it executable
    * ```chmod +x geckodriver```
  * Add driver to PATH
    * ```sudo mv geckodriver /usr/local/bin```
    
## Resources
* Serving static files on S3
  * https://www.caktusgroup.com/blog/2014/11/10/Using-Amazon-S3-to-store-your-Django-sites-static-and-media-files/
