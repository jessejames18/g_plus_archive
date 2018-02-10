# g_plus_archive
Google plus offline search

## Description
This script queries Google Plus API to download activies in your account and let you search through your posts.

## Requirements
- Python 2.7.13
- pycurl

## Installation Guide
Step1: Installing the requirement

```
sudo pip install pycurl
```
Note that depending on your machine, your requirement packages might be different.


Step2: adding your user ID to the script
- move to the script direcoty

```
cd scripts/
```
- edit the file `gplus-api.py`
```
vim gplus-api.py 
```
- find the following line
```
user_id = "YOUR_USER_ID"
```
- replace "YOUR_USER_ID" with your user ID.


