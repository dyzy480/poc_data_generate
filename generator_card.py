#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
import time
import random
import math,string


def getCards(userNum):

	print('generator card begin:' + str(userNum))
	#user_id 产生连续的客户号
	userId = ( x for x in range(1000000000,1000000000+userNum ))
	#卡bin对应地区
	cardRegion = {'603367':'01','603364':'01','603361':'01','603369':'01','603368':'01'
	,'613367':'02','613364':'02','613361':'02','613369':'02','613368':'02'
	,'623367':'03','623364':'03','623361':'03','623369':'03','623368':'03'
	,'633367':'04','633364':'04','633361':'04','633369':'04','633368':'04'
	,'643367':'05','643364':'05','643361':'05','643369':'05','643368':'05'
	}
	regionCode = {'01':'杭州','02':'北京','03':'深圳','04':'上海','05':'宁波'}
	#createTime 创建时间 
	now = int(time.time())
	
	
	#write file 
	with open('data/card.csv', 'w') as data1:
		for tmpId in userId:
			#每个客户的卡数量随机产生(0-6张)
			cardNum = random.randint(1,6)
			cards = (x for x in range(1,cardNum) )
			for n in cards:
				ckeys = list(cardRegion.keys())
				regionNum = len(cardRegion.keys())-1
				cardbinId = random.randint(1,regionNum)
				cardbin = ckeys[cardbinId]				#卡bin
				cardbinRegion = cardRegion[cardbin]		#发卡地区，与卡bin对应
				cardbinRegionName = regionCode[cardbinRegion]
				cardNoEnd = str(random.randint(111111111111,999999999999))
				card_no = cardbin+cardNoEnd				#卡号
				card_type = str(random.randint(1,2))	#卡类型:
				#开卡日期
				cTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime( now - random.randint(60*60,60*60*24*365*10) ) )
				
				#格式:【客户号,卡号,卡类型,发卡地区】
				data1.write( str(tmpId) + ',' 
				+ card_no + ','
				+ card_type + ','
				+ cardbinRegion + ','
				+ cTime
				+ '\n' )
			
	print('--generate cards END--')

if __name__ == '__main__':
	getCards(10000)