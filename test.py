from urllib import request
import io,sys,re,time
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
import os
import time
import subprocess

class Spider():
    url_num = input('http://space.bilibili.com/*******:')
    url = ("http://space.bilibili.com/"+url_num)
    #url='http://space.bilibili.com/19523178'
    one_pattern = 'QAQ([\s\S]*?)QAQ'
    #main_one_pattern = ''

    def fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls,encoding='utf-8')
        #print (htmls)
        return htmls
    
    def analysis(self,htmls):
        one_html = re.findall(Spider.one_pattern,htmls)
        # print (one_html)
        one_html=one_html[0]
        return one_html

    def local_cmd(self,one_html):
        os.system(one_html)
        #os.system(r'taskkill /F /IM YoudaoNote.exe')
        print('ok!')
    def loop_cmd(self):
        while 1:
            time.sleep(1)
            htmls = self.fetch_content()
            self.local_cmd(self.analysis(htmls))
    def main(self):
        self.loop_cmd()

spider = Spider()
spider.main()