# coding: utf-8

class transCookie:
    def __init__(self, cookie):
        self.cookie = cookie
    def stringToDict(self):
        '''
        将从浏览器上Copy来的cookie字符串转化为Scrapy能使用的Dict
        :return:
        '''
        itemDict = {}
        items = self.cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')
            value = item.split('=')[1]
            itemDict[key] = value
        return itemDict

def trans_cookie(cookie):
    trans = transCookie(cookie)
    return trans.stringToDict()

if __name__ == '__main__':
    cookie = 'UM_distinctid=1637d13c8e4395-070a88b25da732-3a614f0b-144000-1637d13c8e5f2b; zg_did=%7B%22did%22%3A%20%221637d13c8f08d3-06b36e148912c-3a614f0b-144000-1637d13c8f1300%22%7D; _uab_collina=152681183925907640816444; PHPSESSID=vhsufin7q28m21tmid1sp1t4a3; _umdata=55F3A8BFC9C50DDA504BD840F2E94712DE130B5540D866C4A133B8A93B61CC33BE4EED9E27F05178CD43AD3E795C914C0FDC3A0F9CEF26EBECB6263678978FBF; hasShow=1; CNZZDATA1254842228=1030422692-1526806590-%7C1530953836; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1530932272,1530944157,1530954047,1530954886; acw_tc=AQAAAIIXUQrt4gIA/VirPRLOX5qN0K1L; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201530952817558%2C%22updated%22%3A%201530954916661%2C%22info%22%3A%201530802193683%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%227e7fb9829550386c0bceb96ffb891092%22%7D; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1530954917'
    print(trans_cookie(cookie))