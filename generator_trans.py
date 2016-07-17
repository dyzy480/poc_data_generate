#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime,time
import random
import math,string,os
import getEName,getPhoneNo
import linecache


#类定义
class CardInfo(object):
	def __init__(self,card_no,balance,limit):
		self.card_no = card_no
		self.balance = balance
		self.limit = limit

		
#public values
cardCount = 0
cardObject = CardInfo('xxx',0,0)

	
#functions:
#获取交易时间:其中hour符合高斯分布;
def getTime():
	hour = 12
	r = random.gauss(0, 1)
	while abs(r)>=3:
		r = random.gauss(0, 1)
	rr = r/3
	mi=random.randint(0,59)
	ss=random.randint(0,59)
	return str(' %02d:%02d:%02d' % ( round(hour*(rr+1)-0.5),mi,ss) )

	
#获取交易类型:  ( 动账类: 03、04、05、07、08、09、10 )
# 01登录20%，02修改手机号2%，03信用卡刷卡消费13%，04借记卡ATM取现10%，05转账20%
# 06绑卡5%，07充值5%，08提现5%，09支付10%，10缴费10%
def get_transType():
	d = random.randint(1,100)
	if d<=20:
		return '01'
	elif d<=22:
		return '02'
	elif d<=35:
		return '03'
	elif d<=45:
		return '04'
	elif d<=65:
		return '05'
	elif d<=70:
		return '06'
	elif d<=75:
		return '07'
	elif d<=80:
		return '08'	
	elif d<=90:
		return '09'
	else:
		return '10'
		
#获取IP地址随机
def getIp():
	a=random.randint(0,255)
	b=random.randint(0,255)
	c=random.randint(0,255)
	d=random.randint(0,255)
	return str('%d.%d.%d.%d' % (a,b,c,d))
		
#获取渠道:
#0网银，1手机银行，2POS，3ATM，4直销银行		
def getChannel():
	return random.choice(['0','1','2','3','4'])

#获取设备编号
def getDeviceId(type):
	n=random.randint(1000,9999)
	if type == '03': 	#POS
		name='POS'
	elif type == '04':	#ATM
		name='ATM'
	else:
		tmp = "".join(random.sample(['A','B','C','D','E','F','G','H','I','J','K','L'
			,'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],10)).replace(" ","")
		return tmp
	return name+str(n)

#获取手机号
def getPhone(type):
	if type=='02':
		return getPhoneNo.get_phone_no()
	else:
		return ''
	
#获取交易金额(单位到分)
def getTransAmt(type,status):
	trans_amt=0
	limit_amt = cardObject.balance if cardObject.balance<cardObject.limit else cardObject.limit
	t = random.randint(1,10)
		
	if status=='0':		#交易失败
		if type in ('03','04','05','07','08','09','10')	:	#动账类交易
			if t<=5:
				trans_amt = random.randint(5*100,limit_amt if limit_amt>500 else 500)
			elif t<=7:
				trans_amt = random.randint(cardObject.balance,cardObject.balance+10000*100)
			else:
				trans_amt = random.randint(cardObject.limit,cardObject.limit+10000*100)
		else:
			trans_amt = 0
	
	else:
		if type in ('03','04','05','07','08','09','10')	:	#动账类交易
			trans_amt = random.randint(1,limit_amt if limit_amt>1 else 1)
		else:
			trans_amt = 0
	
	
	return str(trans_amt)
	

#获取交易前余额()
def getPreBalance():	
	t = random.randint(1,100)
	if t<=50:
		return random.randint(50*100,10000*100)
	elif t<=80:
		return random.randint(10000*100,100000*100)
	elif t<=95:
		return random.randint(100000*100,500000*100)
	else:
		return random.randint(500000*100,10000000*100)
	
	
#获取交易限额:单位到分
def  getAccountLimit():
	t = random.randint(1,100)
	if t<=30:
		return 500*100
	elif t<=70:
		return 5000*100
	elif t<=95:
		return 10000*100
	else:
		return 50000*100
	
	
	
#获取地区标识: 	CHN-中国 USA-美国	,95% CHN,5% USA;
def getArea(type):
	d = random.randint(1,100)
	if d<=95:
		return 'CHN'
	else:
		return 'USA'
	
#交易状态:	0-失败10%;1-成功90%
def getStatus():
	d = random.randint(1,10)
	if d<=1:
		return '0'
	else:
		return '1'

#交易说明: 0-密码错误；1-成功；2-超出限额
def getMsg(status,type):
	if status == '1':
		return "success"
	else:
		if type == '01':
			return 'password wrong'
		else:
			return 'balance not enough'

#随机生成行外账号
def getAccount():
	flag = random.choice(['a','b','c','d','e'])
	num = random.randint(11111111111,99999999999)
	return str('%s%11d' % (flag,num))

#随机获取行内卡号
def getCard(cardCount):
	number = random.randint(1,cardCount-1)
	line = linecache.getline('data/card.csv', number )
	return line	
			
#支付对手信息: 目标账户，目标客户姓名，目标客户手机号，行外标志(0-行内50% ; 1-行外50%)
def getTarget(cardCount):
	flag = 'N'
	name = 'N'
	phone = 'N'
	account = 'N'
	
	i = random.randint(0,1)
	if i == 0:		#行内
		flag = '0'
		acc_line = getCard(cardCount)
		accountLine = acc_line.split(',')
		name = ''
		phone = ''
		account = accountLine[1]
		
	elif i == 1:	#行外
		flag = '1'
		name = getEName.gen_two_words(split=' ',lowercase=True)
		phone = getPhoneNo.get_phone_no()
		account = getAccount()
		
	result = [account,name,phone,flag]
	return result
	
	
	
#从startDate至endDate，每天产生transNum交易数据;
def getTransData(startDate,days,TRANS_NUM):

	print('generator transList begin: from ' + str(startDate)+' days:'+str(days) + '(' +str(TRANS_NUM) +')' )
	#卡数据行数:
	cardCount = len(open('data/card.csv','rU').readlines())
	
	#开始日期:
	s=str(startDate)
	year=s[:4]
	month=s[5:6]
	day=s[7:8]
	begin=datetime.datetime(int(year),int(month),int(day),0,0,0)
	
	#每天产生一份数据文件
	#for file in range(startDate,endDate):
	for x in range(0,days):
	
		today_time=begin + datetime.timedelta(x)
		today=today_time.strftime("%Y-%m-%d")
		toMonth=today_time.strftime("%Y-%m")
		today_number=today_time.strftime("%Y%m%d")
		#交易流水计数器
		trans_no = 1
		#每天最大的流水数量
		transSerial = (x for x in range(10000001,99999999))
		
		with open( 'data/'+ toMonth +'.csv' , 'a') as data:
			while trans_no<TRANS_NUM :
				with open('data/card.csv','r') as cards:
					for line in cards:
					
						#每张卡每天随机产生x条交易记录：
						card_trans_num = random.randint(1,30)
						#产生该卡的当前余额、交易限额
						c = line.split(',')
						cardObject.card_no = c[1]
						cardObject.balance = getPreBalance()
						cardObject.limit = getAccountLimit()
												
						
						#每张卡每天产生x条交易信息: 
						for x in range(1,card_trans_num):
							#交易流水号
							trans_list = today_number + str(next(transSerial))
							#客户号、卡号
							card_line = line.split(',')
							#交易时间
							trans_time=today+getTime()
							#交易类型
							trans_type = get_transType()
							#Ip地址
							ip = getIp()
							#渠道编号
							channel = getChannel()
							#设备编号					modified at 0717
							device_id=getDeviceId(trans_type)
							#手机号
							phone_no = getPhone(trans_type)
							#交易状态
							status = getStatus()
							#账户交易前余额:			add at 0717
							pre_balance = cardObject.balance
							#账户交易限额:				add at 0717
							account_limit = cardObject.limit
							#交易金额					modified at 0717
							trans_amt = getTransAmt(trans_type,status)
							#地区标识
							area = getArea(type)
							#交易说明
							msg = getMsg(status,trans_type)
							#对手信息
							party_info = getTarget(cardCount)
							
							
							#写文件:	【流水号,客户号,卡号,交易时间,卡类型,交易类型,ip,设备编号,渠道编号,
							#				手机号,交易金额,地区,交易状态,交易信息,对手信息,余额,交易限额】
							data.write( trans_list + ','
							+ card_line[0] +','
							+ card_line[1] +','
							+ trans_time + ','
							+ card_line[2] + ','
							+ trans_type + ','
							+ ip + ','
							+ device_id  + ','
							+ channel +','
							+ phone_no + ','
							+ trans_amt + ','
							+ area + ','
							+ status + ','
							+ msg + ','
							+ party_info[0] + ','
							+ party_info[1] + ','
							+ party_info[2] + ','
							+ party_info[3] + ','
							+ str(pre_balance) + ','
							+ str(account_limit)
							+'\n')
							
							#更新 pre_balance:
							cardObject.balance = cardObject.balance-int(trans_amt) if (cardObject.balance-int(trans_amt) )>0 else 0
							
							if(trans_no < TRANS_NUM):
								trans_no=trans_no+1
							else:
								break
						
						if(trans_no>=TRANS_NUM):
							break
	
	print('generator transList end')
	
if __name__ == '__main__':
	getTransData(20160601,2,100000)