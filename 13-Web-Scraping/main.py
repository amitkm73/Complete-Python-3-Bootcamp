"""
bootcamp web scraping stuff
"""
import requests
import bs4
import Image


def show_titles():
    """
    select all title tags and show the text
    :return: None
    """
    target_url = 'http://www.example.com'
    res = requests.get(target_url)
    soup = bs4.BeautifulSoup(res.text, "lxml")
    print('*' * 100)
    print(soup)
    print('*' * 100)
    title_tag = soup.select('title')
    for tag in title_tag:
        print(tag.getText())
    print('*' * 100)


def show_subtitles_by_css():
    """
    select subtitles by knowing their css class and show their text
    :return: None
    """
    target_url = 'https://en.wikipedia.org/wiki/Grace_Hopper'
    res = requests.get(target_url)
    soup = bs4.BeautifulSoup(res.text, "lxml")
    items = soup.select(".toctext")
    for item in items:
        print(item.text)
    print('*'*100)


def show_image():
    """
    select image thumb tag, go to the source image, print stuff about it
    then save it to a file and display it
    :return: None
    """
    target_url = 'https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)'
    res = requests.get(target_url)
    soup = bs4.BeautifulSoup(res.text, "lxml")
    image_info = soup.select('.thumbimage')
    print('*' * 100)
    print(image_info)
    print(len(image_info))
    computer = image_info[0]
    image_src_link = computer['src']
    print(image_src_link)
    image_link = requests.get('https:' + image_src_link)
    print(image_link.content)
    f = open('img_file.jpg', 'wb')
    f.write(image_link.content)
    f.close()
    print('*' * 100)
    img = Image.open('img_file.jpg')
    img.show()


def multi_pages_items():
    """
    work with multiple pages and items
    :return: None
    """
    two_star_titles = []
    base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
    for page_num in range(1, 51):
        scrape_url = base_url.format(page_num)
        res = requests.get(scrape_url)
        soup = bs4.BeautifulSoup(res.text, "lxml")
        books = soup.select(".product_pod")
        for book in books:
            if len(book.select('.star-rating.Two')) != 0:
                two_star_titles.append(book.select('a')[1]['title'])
        for book_title in two_star_titles:
            print(book_title)


def main_web():
    """
    web scraping tests
    :return: None
    """
#    show_titles()
#    show_subtitles_by_css()
#    show_image()
    multi_pages_items()


if __name__ == '__main__':
    main_web()
