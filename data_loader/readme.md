# Data Loader - Assignment 5

## Introduction

A automated Python script to load the data from different sources such as EXCEL, SQLite DB, XML, SAS, and JSON files as well. 

## How to run the script

1. Fristly, you have to create a venv, make sure you have python installed 

```shell
python -m venv .venv
```

2. Activate the virtual environment 

```shell
./venv/Script/activate
```

3. Install the dependencies 

```shell
pip install -r requirements.txt
```

4. Run the scripts
4.1 The data_load.py: this script will load all the database from the data sources from ./data folder and print the results in your terminal output. 

```shell
python data_loader.py
```

4.2 The moview_reviewer.py: this script will only load ./data/IMDB_Movies_2021.db based on the assigments's requirements, there are: 
- TOP 3 HIGH MOVIES RATING
- ALL MOVIE TITLE EXISTS STORY WORD WITHIN 
- ALL MOVIES WHICH HAS THE SAME REVIEWERS 

```shell
python movie_reviwer.py
```