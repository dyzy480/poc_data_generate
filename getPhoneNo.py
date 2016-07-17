#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import math,string

PHONE_PRE = ["130","131","132","133","150","151","152","158","170","177","180","181","182","183",
"188","189"]

def get_phone_no():
	size = len(PHONE_PRE)-1
	id_pre = random.randint(0,size)
	phone_pre = PHONE_PRE[id_pre]
	phone_last = random.randint(11111111,99999999)
	return phone_pre+str(phone_last)
	
if __name__ == '__main__' :
	print("aaa")
	print (get_phone_no())