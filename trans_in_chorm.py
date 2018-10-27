
# -*- coding: utf-8 -*-  
#Python -V: Python 2.6.6  
#filename:GoogleTranslation1.2.py  

import re  
import urllib,urllib2  

#urllib:  
#urllib2: The urllib2 module defines functions and classes which help in opening  
#URLs (mostly HTTP) in a complex world — basic and digest authentication,  
#redirections, cookies and more.  



def translate(text):  
  
    '''模拟浏览器的行为，向Google Translate的主页发送数据，然后抓取翻译结果 '''  
      
    #text 输入要翻译的英文句子  
    text_1=text  
    #'langpair':'en'|'zh-CN'从英语到简体中文  
    values={'hl':'zh-CN','ie':'UTF-8','text':text_1,'langpair':"'en'|'zh-CN'"}  
    url='http://translate.google.cn/translate_t'  
    data = urllib.urlencode(values)  

    #GET / HTTP/1.1
    host = 'Host: translate.google.cn'
    #User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0
    accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    accept_Language = 'en-US,en;q=0.5'
    accept_Encoding = 'gzip, deflate, br'
    #Cookie: NID=144=l0QHL3V4l9c7Je2eZrAbS3y0DMERMUlqJYb0wEr3taitr3f1wFRGN7Gq3c8V9eWTlAhihO8vWzjYHrcG8u0ZMGh7YMRKx_Y1L8UodCEHlkKnr3rST5ShXFY754xRGMSoBzHRNr8s1JVHPEQqQEp3O5-7iSjr58c7oidg3kmVy2Y; _ga=GA1.3.659857013.1540624556; _gid=GA1.3.1413228545.1540624556; 1P_JAR=2018-10-27-11
    #Connection: keep-alive
    #Upgrade-Insecure-Requests: 1
    #Cache-Control: max-age=0

    #headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0'}
    req = urllib2.Request(url,data)  
    #模拟一个浏览器  
    browser= 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0'#'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)'  
    req.add_header('User-Agent',browser) 
    req.add_header('Cookie','NID=144=l0QHL3V4l9c7Je2eZrAbS3y0DMERMUlqJYb0wEr3taitr3f1wFRGN7Gq3c8V9eWTlAhihO8vWzjYHrcG8u0ZMGh7YMRKx_Y1L8UodCEHlkKnr3rST5ShXFY754xRGMSoBzHRNr8s1JVHPEQqQEp3O5-7iSjr58c7oidg3kmVy2Y; _ga=GA1.3.659857013.1540624556; _gid=GA1.3.1413228545.1540624556; 1P_JAR=2018-10-27-11') 
    req.add_header('Accept',accept)
    req.add_header('Accept-Language',accept_Language)
    req.add_header('Accept-Encoding',accept_Encoding)
    req.add_header('Upgrade-Insecure-Requests',1)
    req.add_header('Cache-Control','max-age=0')
    #向谷歌翻译发送请求  
    response = urllib2.urlopen(req)  
    #读取返回页面  
    html=response.read()  
    #从返回页面中过滤出翻译后的文本  
    #使用正则表达式匹配  
    #翻译后的文本是'TRANSLATED_TEXT='等号后面的内容  
    #.*? non-greedy or minimal fashion  
    #(?<=...)Matches if the current position in the string is preceded  
    #by a match for ... that ends at the current position  
    p=re.compile(r"(?<=TRANSLATED_TEXT=).*?;")  
    m=p.search(html)  
    text_2=m.group(0).strip(';')  
    return text_2  

if __name__ == "__main__":  
    #text_1 原文  
    #text_1=open('c:\\text.txt','r').read()  
    text_1='Hello, my name is Derek. Nice to meet you! '  
    print('The input text: %s' % text_1)  
    text_2=translate(text_1).strip("'")  
    print('The output text: %s' % text_2)  

    #保存结果  
    filename='c:\\Translation.txt'  
    fp=open(filename,'w')  
    fp.write(text_2)  
    fp.close()  
        
    report='Master, I have done the work and saved the translation at '+filename+'.'  
    print('Report: %s' % report)  
