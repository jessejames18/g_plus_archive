import pycurl
from StringIO import StringIO
import json
import codecs
from os.path import dirname, abspath


root_address = dirname(dirname(abspath(__file__))) + "/"
user_id = "YOUR_USER_ID"
secret_key = "YOUR_SECRET_KEY"
archive_address = root_address + "archive/"
latest_id_address = root_address + "latest_id"
template_activity_list_query_link = "https://www.googleapis.com/plus/v1/people/" + user_id + "/activities/public?key=" \
                                    + secret_key + "&maxResults=100&pageToken="
template_get_activity_query_link = "https://www.googleapis.com/plus/v1/activities/activityId?key=" + secret_key


def send_request(api_link):
    buffer = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, api_link)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()

    body = buffer.getvalue()
    body_dict = json.loads(body)
    return body_dict


def write_on_disk(activity_id, activity_content_str, activity_url_str):
    dest_file = codecs.open(archive_address + activity_id, "w", "utf-8")
    dest_file.write("url=" + activity_url_str + "\n")
    dest_file.write(activity_content_str)
    dest_file.close()


def read_latest_id():
    find_latest_id = False
    latest_id_file = open(latest_id_address, "r")
    for line in latest_id_file:
        latest_id = line.replace("\n", "")
        find_latest_id = True
    latest_id_file.close()
    if find_latest_id == False:
        latest_id = "default_latest_id"
    return latest_id

def update_latest_id(new_latest_id):
    latest_id_file = open(latest_id_address, "w")
    latest_id_file.write(new_latest_id)
    latest_id_file.close()

def crawler(latest_id):
    query_activity_list = template_activity_list_query_link
    activity_list_dict = send_request(query_activity_list)
    latest_id_flag = False
    while_break_flag = False
    while True:
        for item in activity_list_dict['items']:
            activity_id = item['id']
            if activity_id == latest_id:
                while_break_flag = True
                break
            if latest_id_flag == False:
                latest_id = activity_id
                latest_id_flag = True
            activity_content_str =  item["object"]['content']
            activity_url_str = item['url']
            write_on_disk(activity_id, activity_content_str, activity_url_str)
        if while_break_flag == True:
            break
        if not "nextPageToken" in activity_list_dict:
            break
        next_page_token = activity_list_dict["nextPageToken"]
        query_activity_list = template_activity_list_query_link + next_page_token
        activity_list_dict = send_request(query_activity_list)
    update_latest_id(latest_id)

def main():
    latest_id = read_latest_id()
    crawler(latest_id)
main()
