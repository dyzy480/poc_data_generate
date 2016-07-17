#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
import time
import random
import math,string
import getEName,getPhoneNo

#other function:
def gen_birth(startyear, endyear):
	year = random.randint(int(startyear),int(endyear))
	month = random.randint(1,12)
	day = random.randint(1,30)
	return str("%04d%02d%02d" % (year,month,day))


def get_users(userNum):
	print('generator user begin: ' + str(userNum) )
	#user_id 产生连续的客户号
	userId = ( x for x in range(1000000000,1000000000+userNum ))
	#createTime 创建时间 
	now = int(time.time())
	createTime = (now for x in range(userNum))
	#身份证号码
	idNos = (x for x in (range(1000000001,9999999999)))


	#write file 
	with open('data/user.csv', 'w') as data1:
		for tmpId in userId:
			#创建时间
			cTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime( next(createTime) - random.randint(60*60,60*60*24*365*10) ) )
			#客户姓名（英文）
			eName = getEName.gen_two_words(split=' ',lowercase=True)
			#出生日期
			birth = gen_birth(1950,2000)
			#证件类型：#1身份证
			id_type='1'
			#身份证号码
			number = str(next(idNos))
			id_no = number[:6] + birth + number[6:10]
			#手机号码
			phone_no = getPhoneNo.get_phone_no()
			#用户类型
			user_type = random.randint(0,1)
			
			#格式： 【客户号,客户名,证件号码,手机号码,创建时间,用户类型】
			data1.write( str(tmpId) + ',' 
				+ eName + ','
				+ id_no + ','
				+ phone_no + ','
				#+ birth + ','
				#+ id_type + ','
				+ cTime + ','
				+ str(user_type)
				+ '\n' )

	print('--users generate END--')

if __name__ == '__main__':
	get_users(1000)