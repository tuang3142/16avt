import requests
from bs4 import BeautifulSoup


def get_traits(doc):
    res = {'traits': []}
    cards = doc.find(class_='cards').find_all("app-pct-card")
    for card in cards:
        res['traits'].append({
            'title': card.attrs['title'],
            'label': card.attrs['label'],
            'score': card.attrs[':score']
        })
    return res


def get_hero_info(doc):
    def no_question_mark_td(tag):
        return tag.name == 'td' and not tag.text == '?'

    def trim(text):
        t = text.strip()
        if t[-1] == ':':
            return t[:len(t)-1]
        return t

    info, pair = {}, []
    table_datas = doc.find(class_='info-table').find_all(no_question_mark_td)
    for td in table_datas:
        text = trim(td.text)
        pair.append(text)
        if len(pair) == 2:
            key, val = pair
            info[pair[0]] = pair[1]
            pair = []
    return info


def extract_data(url):
    page = requests.get(url)
    doc = BeautifulSoup(page.content, 'html.parser')
    return {**get_traits(doc), **get_hero_info(doc)}
