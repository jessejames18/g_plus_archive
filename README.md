# g_plus_archive
Google plus offline search

## Description
This script queries Google Plus API to download activies in your account and let you search through your posts.

## Requirements
- Python 2.7.13
- pycurl

## Installation Guide
Step1: Install the requirement

```
sudo pip install pycurl
```
Note that depending on your machine, your requirement packages might be different.

#
Step2: add your user ID to the script
- move to the script direcoty

```
cd scripts/
```
- edit the file `gplus-api.py`
```
vim gplus-api.py 
```
- find the following line
`user_id = "YOUR_USER_ID"`
- replace "YOUR_USER_ID" with your user ID.

Note that you can find your user ID from your profile link.
#
Step3: create your API key
Follow this instruction to generate your API key:
  https://developers.google.com/+/web/api/rest/oauth#apikey

#
Step4: add your secret key (generated in step 3) to the file `gplus-api.py`
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
secret_key = "YOUR_SECRET_KEY"
```
- replace "YOUR_SECRET_KEY" with your secret key


## Running the script
There are two scripts.
- You can use `gplus-api.py` to download your posts in your local machine. In order to do that, simply run the script:
```
python gplus-api.py
```
- For searching through your posts, you can use `google-plus-search.py`. Keep in mind that the searching algorithm is boolean search. So, nothing fancy.
```
python google-plus-search.py Trump
```
It creates a temporary html file showing your search result and then automatically brings up your browser.

## Enjoy!
