import prettytable, csv
from requests_html import HTMLSession

titleTL = {
    '辉夜大小姐想让我告白~天才们的恋爱头脑战~': 'kaguya', 
    '约定的梦幻岛': 'neverland', 
    '五等分的新娘': '5bun', 
    '路人超能100 II(灵能百分百 第二季)': 'mob2',
    '刀剑神域 Alicization': 'SAO:A', 
    '盾之勇者成名录':'shield hero', 
    '约会大作战 第三季': 'date a live',
    '关于我转生变成史莱姆这档事': 'slime', 
    'JOJO的奇妙冒险 黄金之风': 'jojo5', 
    '强风吹拂': 'run w/the wind', 
    'ULTRAMAN 机动奥特曼': 'ultraman', 
    'ULTRAMAN 机动奥特曼（中配）': 'ultraman dub', 
    '天使降临到我身边': 'tenshi', 
    '多罗罗': 'dororo', 
    '同居人是猫': 'roommate cat', 
    '魔法禁书目录 第三季': 'index3', 
    'pop子和pipi美的日常': 'pop team epic', 
    '不吉波普不笑': 'boogiepop', 
    '烟草': 'kemurikusa', 
    '精灵宝可梦 日月': 'pokemonSM'}

class Series:
    def __init__(self,source):
        self.rank = source.find('.num', first=True).text
        self.title = source.find('.title', first=True).text
        self.play = self.convertUnit(source.find('.data-box')[0].text)
        self.view = self.convertUnit(source.find('.data-box')[1].text)
        self.fav = self.convertUnit(source.find('.data-box')[2].text)
        self.pts = source.find('.pts div', first=True).text

    def convertUnit(self,text:str):
        if '万' in text:
            text = f'{str((int(float(text.replace("万", "")))*10000)/1000000)}m'
        elif '亿' in text:
            text = f'{(int(float(text.replace("亿", "")))*100000000)/1000000}m'
        return text

def singleRank(rank:int, page):
    s = Series(page.html.find('.rank-item')[rank-1])
    try:
        tempTitle = titleTL[s.title]
    except KeyError:
        tempTitle = s.title
    seriesInfo = (
        s.rank,
        tempTitle,
        s.play,
        s.view,
        s.fav,
        s.pts
    )
    
    return seriesInfo

def exportRankTable():
    with open("bilibiliRank.csv", "w") as f:
        w = csv.writer(f)
        w.writerow(['Rank', 'Title', 'Play', 'Danmaku', 'Favourites', 'Pts'])
        for i in range(1, 21):
            s = singleRank(i, page)
            w.writerow([s[i] for i in range(6)])
    print("Data saved in file bilibiliRank.csv.")


def bilibiliRank(rank:int = 0, export:bool = False):
    sess = HTMLSession()
    url = 'https://www.bilibili.com/ranking/bangumi/13/1/7/'

    pt = prettytable.PrettyTable()
    pt.field_names = ['Rank', 'Title', 'Play', 'Danmaku', 'Favourites', 'Pts']

    page = sess.get(url)

    if export==True:
        exportRankTable()

    if rank > 0:
        return singleRank(rank, page)
    else:
        for section in page.html.find('.rank-item')[:20]:
            s = Series(section)
            try:
                tempTitle = titleTL[s.title]
            except KeyError:
                tempTitle = s.title
                
            pt.add_row([s.rank, tempTitle, s.play, s.view, s.fav, s.pts])


        return pt

    