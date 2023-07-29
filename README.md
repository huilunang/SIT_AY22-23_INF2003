# INF2003 - Smart Bloobin
Improve Singapore's recycling bins.

## Install Dependencies
### 1. MariaDB Connector/C
#### MacOS
> brew install mariadb-connector-c
#### WindowsOS
> [MariaDB Connector/C](https://mariadb.com/docs/skysql-previous-release/connect/programming-languages/c/install/#Install_via_MSI_(Windows))
### 2. Python Package
> pip install -r requirements.txt
### 3. [Docker Desktop](https://www.docker.com/products/docker-desktop/)
### 4. Make Utility
#### MacOS
> brew install make
#### WindowsOS
> [Reference](https://www.technewstoday.com/install-and-use-make-in-windows/)

## Setup
- Rename `env` file to `.env` file

## Running Application
-  App accessible at http://127.0.0.1:5000/
### MacOS
> flask --app src/app run
### WindowsOS
> python -m flask --app src/app run
### Docker
#### MacOS
> make run
#### WindowsOS
> Mingw32-make run

## Clean Up Docker Resources
### Remove compose build (stop application)
> make clean
### Remove unused resources dangling
> make deepclean

## Login Credentials
### Username: <your name> (e.g. sihui)
### Password: 123