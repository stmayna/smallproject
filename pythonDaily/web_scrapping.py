from urllib.request import urlopen, Request
import re
from bs4 import BeautifulSoup

'''
source: https://realpython.com/python-web-scraping-practical-introduction/
'''

'''
Extract Text From HTML With String Methods
'''

# url = "http://olympus.realpython.org/profiles/aphrodite"
url = "http://olympus.realpython.org/profiles/poseidon"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
title_index = html.find("<title>")
len_title = len("<title>")
start_index = title_index + len("<title>")
end_index = html.find("</title>")
title = html[start_index:end_index]

'''
With User Agent
'''

# url = "https://www.wattpad.com/stories/bts%2cfanfiction%2cromance/new"
# user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"

# req = Request(url, headers={'User-Agent': user_agent})
# page = urlopen(req)

# html_bytes = page.read()
# html = html_bytes.decode("utf-8")

'''
Get to Know Regular Expressions
'''

re.findall("ab*c", "abcd")
#['abc']

re.findall("ab*c", "acc")
#['ac']

re.findall("ab*c", "abcac")
#['abc', 'ac']

re.findall("ab*c", "abdc")
#[]

re.findall("ab*c", "ABC")
#[]

re.findall("ab*c", "ABC", re.IGNORECASE)
#['ABC']

re.findall("a.c", "abc")
#['abc']

re.findall("a.c", "abbc")
#[]

re.findall("a.c", "ac")
#[]

re.findall("a.c", "acc")
#['acc']

re.findall("a.*c", "abc")
#['abc']

re.findall("a.*c", "abbc")
#['abbc']

re.findall("a.*c", "ac")
#['ac']

re.findall("a.*c", "acc")
#['acc']

re.findall("mb*a", "mbbna")
#[]

match_results = re.search("ab*c", "ABC", re.IGNORECASE)
match_results.group()
# 'ABC'

string = "Everything is <replaced> if it's in <tags>."
str_greedy = re.sub("<.*>", "ELEPHANTS", string) # Greedy
str_non_greedy = re.sub("<.*?>", "ELEPHANTS", string) # Non-greedy

'''
Extract Text From HTML With Regular Expressions

For now, just know that calling .group() on MatchObject
will return the first and most inclusive result,
which in most cases is just what you want.
'''

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")

pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title) # Remove HTML tags

'''
Exercise
Display the text following Name: and Favorite Color:
(not including any leading spaces or trailing HTML tags
that might appear on the same line).
'''

name_pattern =  "<h2.*?>.*?</h2.*?>"
color_pattern = "color:.*"
name_find = re.search(name_pattern, html, re.IGNORECASE)
color_find = re.search(color_pattern, html, re.IGNORECASE)
name_results = re.sub("<.*?>", "", name_find.group())
color_results = color_find.group()

# Exercixe Solution
html_page = urlopen(url)
html_text = html_page.read().decode("utf-8")

for string in ["Name: ", "Favorite Color:"]:
    string_start_idx = html_text.find(string)
    text_start_idx = string_start_idx + len(string)

    next_html_tag_offset = html_text[text_start_idx:].find("<")
    text_end_idx = text_start_idx + next_html_tag_offset

    raw_text = html_text[text_start_idx:text_end_idx]
    clean_text = raw_text.strip(" \r\n\t")
    # print(f"result: \n{clean_text}")

'''
Use an HTML Parser for Web Scraping in Python.
Requirement: pip install beautifulsoup4
'''

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
print(f"result: \n{soup}")

