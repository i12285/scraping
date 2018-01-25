import requests
from bs4 import BeautifulSoup
import pdb

res = requests.get("https://official.ameba.jp/")
content = res.content
soup = BeautifulSoup(content, "html.parser")
pdb.set_trace()

