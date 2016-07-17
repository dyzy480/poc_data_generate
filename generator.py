#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
import time
import random,os
import math,string
import generator_user
import generator_trans
import generator_card

##参数配置:
user_num =50000		#生成的用户数量,如500个客户
begin=20160201		#交易数据起始日期,如从2016年6月1日起
days=100				#交易数据生成的天数,如一共生成10天的数据
trans_num=100000		#交易数据每天的生成数量,如1000条/天
##参数配置


#建立data目录:
if os.path.exists('data/'):
	pass
else:
	os.mkdir('data/')

start=time.clock()
generator_user.get_users(user_num)
end1=time.clock()
print('user used %f s' % ( end1-start ) ) 
generator_card.getCards(user_num)
end2=time.clock()
print('cards used %f s ' % ( end2-end1 ) ) 
generator_trans.getTransData(begin,days,trans_num)
end3=time.clock()
print('trans used %f s' % ( end3-end2  ) ) 