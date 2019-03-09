# -*- coding: utf-8 -*-
# QQ音乐快速下载
import requests
import os
import time
import re
import urllib
from fake_useragent import UserAgent

proxies = {
	'http':'http://115.29.214.175:8118'
}


class Downloader():
	def __init__(self):
		self.headers = {
					'User-Agent': UserAgent().random,
					}
		self.search_url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.top&searchid=34725291680541638&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w={}&g_tk=5381&jsonpCallback=MusicJsonCallback703296236531272&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0'
		self.fcg_url = 'https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg?g_tk=5381&jsonpCallback=MusicJsonCallback9239412173137234&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&cid=205361747&callback=MusicJsonCallback9239412173137234&uin=0&songmid={}&filename={}.m4a&guid=8208467632'
		self.downloader_url = 'http://dl.stream.qqmusic.qq.com/{}.m4a?vkey={}&guid=8208467632&uin=0&fromtag=66'
	def run(self, keyword, num=1):
		# Step1
		# 根据歌名搜索，获取所需的信息
		print('[INFO]:Searching...')
		res = requests.get(self.search_url.format(keyword), headers=self.headers).text
		# media_mid
		media_mid_temp = re.findall('"media_mid":"(.*?)"', res)
		media_mid = []
		for i in range(len(media_mid_temp)):
			media_mid.append('C400'+media_mid_temp[i])
		# songmid
		songmid = re.findall('"lyric_hilight":".*?","mid":"(.*?)","mv"', res)
		# singer
		singer_temp = re.findall('"singer":\[.*?\]', res)
		singer = []
		for s in singer_temp:
			singer.append(re.findall('"name":"(.*?)"', s)[0])
		# songname
		songname = re.findall('},"name":"(.*?)","newStatus"', res)
		# Step2
		# 获取下载地址
		print('[INFO]:Parsing download url...')
		urls = []
		del_idex = []
		songname_keep = []
		singer_keep = []
		for m in range(len(media_mid)):
			try:
				fcg_res = requests.get(self.fcg_url.format(songmid[m], media_mid[m]), headers=self.headers)
				vkey = re.findall('"vkey":"(.*?)"', fcg_res.text)[0]
				urls.append(self.downloader_url.format(media_mid[m], vkey))
				songname_keep.append(songname[m])
				singer_keep.append(singer[m])
			except:
				print('[Warning]:One song lost...')
			time.sleep(0.5)
		# Step3
		# 下载歌曲
		print('[INFO]:Start downloading...')
		if num > len(urls):
			print('[Warning]:Only find %d songs...' % len(urls))
			num = len(urls)
		if not os.path.exists('./results'):
			os.mkdir('./results')
		for n in range(num):
			print('[INFO]:Downloading %dth song...' % (n+1))
			filepath = './results/{}'.format(songname_keep[n].replace("\\", "").replace("/", "").replace(" ", "")+'_'+singer_keep[n].replace("\\", "").replace("/", "").replace(" ", "")+'.m4a')
			urllib.request.urlretrieve(urls[n], filepath)
		print('[INFO]:All done...')

# if __name__ == '__main__':
# 	while True:
# 		print('[INFO]:QQ music Downloader...')
# 		print('[Author]:Charles')
# 		keyword = input('Enter the SongName:')
# 		songnum = input('Enter the num you want to download:')
# 		try:
# 			songnum = int(songnum)
# 		except:
# 			continue
# 		dl = Downloader()
# 		dl.run(keyword, songnum)
# 回忆里的那个人，亲爱的你在哪里，天之大，想着你亲爱的，我的快乐就是想你，你是否也在我心中，看透爱情看透你，做你的爱人，这一生回忆有你就足够，驿动的心，等你等了那么久，我爱你胜过你爱我，放不下的牵挂，朋友别哭，把悲伤留给自己，放不下的牵挂，天在下雨我在想你，亲爱的你在哪里，天之大，想着你亲爱的，我的快乐就是想你，你是否也在我心中，看透爱情看透你，做你的爱人，这一生回忆有你就足够，驿动的心，
# musicName = '天在下雨我在想你，我的好兄弟，迟来的爱，常回家看看，父亲，母亲，你不来我不老，吻别，中国人，天亮了，看海，我的楼兰，送战友'
# musicName = '妈妈我想你，我和草原有个约定，你会爱我到什么时候，没有你的陪伴我真的好孤单，披着羊皮的狼，冲动的惩罚，再回西藏，两只蝴蝶，西海情歌，情人'
musicName = '刘和刚，阎维文'
musicName1 = '下定决心忘记你，自由,从头再来，拥抱你离去,为爱流下伤的泪'
musicList = musicName.split('，')
# musicList = musicList[12:]
print(musicList)
dl = Downloader()
if __name__ == '__main__':
	for music in musicList:
		dl.run(music,1)
		print(music)


