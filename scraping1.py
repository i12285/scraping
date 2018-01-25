import requests
from bs4 import BeautifulSoup
import pdb
import re

def show_mygirl_rank(url):
    """
    練習
    """

    # html構造を取得
    res = requests.get(url)
    content = res.content
    soup = BeautifulSoup(content, 'html.parser')

    # webページからランキングのタイトルを取得
    title = soup.find("a",href="#_2017").text
    print("~~~" + title + "~~~")

    # 俺の女収集
    dev = soup.find(class_="toc_list").find_all("a")

    for cont in dev:
        mygirl = re.search(r"\d\位　\S+",cont.text)
        if mygirl is None:
            continue
        print(mygirl.group())

def main():
    url = 'https://newsmatomedia.com/gravure-idol'
    show_mygirl_rank(url)

if __name__ == '__main__':
    main()





    
