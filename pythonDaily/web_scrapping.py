# source: https://realpython.com/python-web-scraping-practical-introduction/
# from urllib.request import urlopen

# # url = "http://olympus.realpython.org/profiles/aphrodite"
# url = "https://hit-wikis.pages.dev/"
# page = urlopen(url)
# html_bytes = page.read()
# html = html_bytes.decode("utf-8")
# # title_index = html.find("<title>")
# # start_index = title_index + len("<title>")
# # end_index = html.find("</title>")
# print(f"result: \n{html}")

# With User Agent

from urllib.request import urlopen, Request

url = "https://www.wattpad.com/stories/bts%2cfanfiction%2cromance/new"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"

req = Request(url, headers={'User-Agent': user_agent})
page = urlopen(req)

html_bytes = page.read()
html = html_bytes.decode("utf-8")

print(f"result: \n{html}")


