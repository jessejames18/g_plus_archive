import os
import sys
import codecs
import webbrowser
from os.path import dirname, abspath

root_address = dirname(dirname(abspath(__file__))) + "/"
archive_address = root_address + "archive/"
result_address =  root_address + "search_result.html"


def read_file(file_name):
    file_list = []
    file = codecs.open(archive_address + file_name, "r", "utf-8")
    for line in file:
        file_list.append(line)
    post_url = file_list[0].split("url=")[1]
    if len(file_list) == 2:
        post_content = file_list[1]
    else:
        post_content = None
    return post_url, post_content


def term_comparison(term_one, term_two):
    if term_one == term_two:
        return True
    return False


def write_on_disk(post_url, post_content, file):
    link_string = '<a href="' + post_url + '">'
    file.write("<tr>")
    file.write("<th>")
    file.write(link_string)
    file.write(post_url)
    file.write("</a>")
    file.write("</th>")
    file.write("<th>")
    file.write(post_content)
    file.write("</th>")
    file.write("</tr>")


def create_html_table(file):
    file.write("<!DOCTYPE html>\n")
    file.write("<html>\n")
    file.write("<head>\n")
    file.write("<style>\n")
    file.write("table, th, td {\n")
    file.write("border: 1px solid black;\n")
    file.write("border-collapse: collapse;}\n")
    file.write("</style>\n")
    file.write("</head>\n")
    file.write("<body>\n")
    file.write('<table style="width:100%">\n')



def end_html_table(file):
    file.write("</table>\n")
    file.write("</body>\n")
    file.write("</html>\n")


def main():
    file = codecs.open(result_address, "w", "utf-8")
    create_html_table(file)
    query_list = sys.argv
    for file_name in os.listdir(archive_address):
        break_flag = False
        post_url, post_content = read_file(file_name)
        if post_content != None:
            post_content_list = post_content.split(" ")
            for term_two in post_content_list:
                if len(query_list) > 1:
                    for query in query_list:
                        term_one = query.decode('utf-8')
                        if term_comparison(term_one, term_two):
                            write_on_disk(post_url, post_content, file)
                            break_flag = True
                            break
                if break_flag == True:
                    break
                else:
                    term_one = query_list[0].decode('utf-8')
                    if term_comparison(term_one, term_two):
                        write_on_disk(post_url, post_content, file)
                        break
    end_html_table(file)
    file.close()

    webbrowser.open_new_tab(result_address)
main()
