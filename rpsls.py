#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：谢钦豪
日期：2019/11/14
"""

import random



# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数



def number_to_name(num):
	if num==0:
		return "石头"
	elif num==1:
		return "史波克"
	elif num==2:
		return "纸"
	elif num==3:
		return "蜥蜴"
	elif num==4:
		return "剪刀"


def rpsls(a,choice_name):
	if a=="剪刀" and choice_name=="纸":
		print("电脑赢了")
	elif a=="剪刀" and choice_name=="蜥蜴":
		print("电脑赢了")
	elif a=="纸" and choice_name=="石头":
		print("电脑赢了")
	elif a=="纸" and choice_name=="史波克":
		print("电脑赢了")
	elif a=="石头" and choice_name=="剪刀":
		print("电脑赢了")
	elif a=="石头" and choice_name=="蜥蜴":
		print("电脑赢了")
	elif a=="蜥蜴" and choice_name=="纸":
		print("电脑赢了")
	elif a=="蜥蜴" and choice_name=="史波克":
		print("电脑赢了")
	elif a=="史波克" and choice_name=="剪刀":
		print("电脑赢了")
	elif a=="史波克" and choice_name=="石头":
		print("电脑赢了")
	elif a=="纸" and choice_name=="剪刀":
		print("您赢了")
	elif a=="蜥蜴" and choice_name=="剪刀":
		print("您赢了")
	elif a=="石头" and choice_name=="纸":
		print("您赢了")
	elif a=="史波克" and choice_name=="纸":
		print("您赢了")
	elif a=="剪刀" and choice_name=="石头":
		print("您赢了")
	elif a=="蜥蜴" and choice_name=="石头":
		print("您赢了")
	elif a=="布" and choice_name=="蜥蜴":
		print("您赢了")
	elif a=="史波克" and choice_name=="蜥蜴":
		print("您赢了")
	elif a=="蜥蜴" and choice_name=="蜥蜴":
		print("平局")
	elif a=="石头" and choice_name=="石头":
		print("平局")
	elif a=="史波克" and choice_name=="史波克":
		print("平局")
	elif a=="剪刀" and choice_name=="剪刀":
		print("平局")
	elif a=="纸" and choice_name=="纸":
		print("平局")
	elif a=="剪刀" and choice_name=="史波克":
		print("您赢了")
	elif a=="石头" and choice_name=="史波克":
		print("您赢了")
	else:
		print("Error: No Correct Name")
import random
x=random.randint(0,4)
a=number_to_name(x)

print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
print("----------------")
print("您的选择为：%s"%(choice_name))
print("计算机的选择为：%s"%(a))
rpsls(a,choice_name)


   










   
