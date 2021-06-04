# <center>Dataproject SQLAlchemy</center>

Storing data in SQL DB and retrieved with SQLAlchemy.

Data project with the graphs generated on the browser using HighCharts.

## 1. Set up virtual environment
### Step 1 : Install virtual environment
NOTE : Should have pip installed
```bash
pip install virtualenv
```
### Step 2 : Create the virtual environment
```bash
virtualenv venv
```
### Step 3 : Activate the virtual environment
```bash
source venv/bin/activate
```
Once it is activated, it will show (venv) before the username as shown below : 
```bash
(venv) username project
$ 
```
### Step 4 : To deactivate virtual environment
```bash
deactivate
```

## 2. Clone repository
copy the link of ssh clone from the repository and run command as follows :
```bash
git clone git@gitlab.com:mountblue/cohort-16-python/arkadu_kumar/dataproject-sqlalchemy.git
```
After succesfully cloning the repository, change directory to dataproject-sqlalchemy by following command
```bash
cd dataproject-sqlalchemy
```

## 3. Install Dependencies
To install all the dependencies or requirements, run the command :

```bash
pip install -r requirements.txt
```
NOTE : Make sure to have virtual environment activated so it installs in the virtual environment.

## 4. Download required csv file
Download the csv file from the <a href="https://datahub.io/core/population-growth-estimates-and-projections/r/population-estimates.csv">link</a>  and paste it in the directory `datasets/csv` with the name **population_estimates_csv.csv**
```bash
datasets/csv/population_estimates_csv.csv
```

## 5. Run the Files
### Step 1 — Installing PostgreSQL
To install PostgreSQL, first refresh your server’s local package index:
```bash
sudo apt update
```

Then, install the Postgres package along with a -contrib package that adds some additional utilities and functionality:
```bash
sudo apt install postgresql postgresql-contrib
```
### Step 2 — Using PostgreSQL

One way is to switch over to the postgres account on your server by typing:
```bash
sudo -i -u postgres
```
 
Then you can access the Postgres prompt by typing:
```bash
postgres@server:~$ psql
```
 
This will log you into the PostgreSQL prompt, and from here you are free to interact with the database management system right away.

To exit out of the PostgreSQL prompt, run the following:
```bash
postgres=# \q
```
 
This will bring you back to the postgres Linux command prompt. To return to your regular system user, run the exit command:
```bash
postgres@server:~$ exit
```
 
Another way to connect to the Postgres prompt is to run the psql command as the postgres account directly with sudo:
```bash
sudo -u postgres psql
```
 
This will log you directly into Postgres without the intermediary bash shell in between.

Again, you can exit the interactive Postgres session by typing:
```bash
postgres=# \q
```
### Step 3 — Creating User and Database

Start postgres psql
```bash
sudo -u postgres psql
```
Type in the command:
```bash
postgres=# \i create_user.sql
```
This will create the user and database.
Then, exit postgres psql 
```bash
postgres=# \q
```
### Step 4 — To generate JSON files, run :
```bash
python3 generating_json.py
```
That will generate the JSON files.

NOTE: There should be `json` folder in `datasets` folder, like `datasets/json`, otherwise, it will throw a error that directory not exist.

Next run the command :
```bash
python3 -m http.server
```
It starts a localhost server. Head to that url and open `project.html` file to see the graphs.

To stop the server:
Click Ctrl^c

### Step 5 — Deleting User and Database

Start postgres psql
```bash
sudo -u postgres psql
```
Type in the command:
```bash
postgres=# \i delete_user.sql
```
This will create the user and database.
Then, exit postgres psql 
```bash
postgres=# \q
```

___
## Where are JSON files located ?
JSON files are located in `datasets/json` for each graph.

JSON files only contains data required for respective graph plots.

## How to plot graph on Browser ?
I have used <a href="https://www.highcharts.com/demo">HighCharts</a> JavaScript Lib for plotting graphs on Browser.
___
# <center>Thank You</center>