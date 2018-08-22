# coding=utf-8
import urllib.request, re, os, gzip, sys


def savefile(str):
    Path = os.getcwd()
    if not os.path.isdir(Path):
        os.mkdir(Path)
    pos = str.rindex('/')
    t = os.path.join(Path, str[pos + 1:])
    print("保存到:"+Path)
    return t


def unzip(dt):
    ret = None
    try:
        ret = gzip.decompress(dt)
    except:
        return dt
    return ret


def getImg(av):
    bili = 'https://www.bilibili.com/video/av'
    url = bili + av + '/'
    print("网址:"+url)
    try:
        req = urllib.request.urlopen(url)
    except:
        print("网页打开失败")
    data = unzip(req.read())
    img = re.findall(r'(http:[\S]*?/archive/[\S]*?(jpg|png|gif))', str(data))
    img = img[0][0]
    urllib.request.urlretrieve(img, savefile(img))

av = input('请输入视频的AV号：')
try:
    getImg(av)
except:
    print("下载封面失败")
