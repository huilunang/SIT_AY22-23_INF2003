# INF2003 - Smart Bloobin
## Improve Singapore's recycling bins.

## Install Dependencies
### 1. MariaDB Connector/C
#### MacOS
> brew install mariadb-connector-c
#### WindowsOS
> [MariaDB Connector/C](https://mariadb.com/docs/skysql-previous-release/connect/programming-languages/c/install/#Install_via_MSI_(Windows))
### 2. Python Package
> pip install -r requirements.txt

## Setup
- Rename `env` file to `.env` file

## Running Application
### MacOS
> flask --app src/app run
### WindowsOS
> python -m flask --app src/app run