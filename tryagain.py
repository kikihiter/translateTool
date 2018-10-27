# -*- coding: UTF-8 -*-
# kiki 2018/10/27

"""
try my best for a long time.Finally,i got it.This code can translate word in Engling to Chinese.
some code from https://www.v2ex.com/t/353781
now it is time to do my work
"""

"""
@author:yunkchen
@file:translate.py
@time:2017/4/10 0010 下午 1:52
"""
import requests
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
en2zh_url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=zh&dt=t&q="
zh2en_url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=zh&tl=en&dt=t&q="
headers = { "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"Accept-Encoding":"gzip, deflate, sdch, br",
"Accept-Language":"zh-CN,zh;q=0.8",
"User-Agent":"Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1",
"Referer": "http://wap.baidu.com"
}


def translate(word):
	word = word.decode("utf-8")
	#print word
	if word >= u'\u4e00' and word<=u'\u9fa5':
		response = requests.get(zh2en_url+word, timeout=60, headers=headers)
		ch = response.content.split("\"")[1]
		print(ch)
	else:
		response = requests.get(en2zh_url+word, timeout=60, headers=headers)
		print
		print response.content
		#print
		#print response.content.split("\"")
		ch = response.content.split("\"")
		MAX_index = len(ch)
		for i in range(MAX_index-1):
			if i%4 == 1:
				print ch[i]
		#ch = response.content.split("\"")[i]
		#print 
		#print(ch)

#while True:
word = raw_input("Please input word:")
translate(word)