#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�л�պ�
���ڣ�2019/11/14
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��



def number_to_name(num):
	if num==0:
		return "ʯͷ"
	elif num==1:
		return "ʷ����"
	elif num==2:
		return "ֽ"
	elif num==3:
		return "����"
	elif num==4:
		return "����"


def rpsls(a,choice_name):
	if a=="����" and choice_name=="ֽ":
		print("����Ӯ��")
	elif a=="����" and choice_name=="����":
		print("����Ӯ��")
	elif a=="ֽ" and choice_name=="ʯͷ":
		print("����Ӯ��")
	elif a=="ֽ" and choice_name=="ʷ����":
		print("����Ӯ��")
	elif a=="ʯͷ" and choice_name=="����":
		print("����Ӯ��")
	elif a=="ʯͷ" and choice_name=="����":
		print("����Ӯ��")
	elif a=="����" and choice_name=="ֽ":
		print("����Ӯ��")
	elif a=="����" and choice_name=="ʷ����":
		print("����Ӯ��")
	elif a=="ʷ����" and choice_name=="����":
		print("����Ӯ��")
	elif a=="ʷ����" and choice_name=="ʯͷ":
		print("����Ӯ��")
	elif a=="ֽ" and choice_name=="����":
		print("��Ӯ��")
	elif a=="����" and choice_name=="����":
		print("��Ӯ��")
	elif a=="ʯͷ" and choice_name=="ֽ":
		print("��Ӯ��")
	elif a=="ʷ����" and choice_name=="ֽ":
		print("��Ӯ��")
	elif a=="����" and choice_name=="ʯͷ":
		print("��Ӯ��")
	elif a=="����" and choice_name=="ʯͷ":
		print("��Ӯ��")
	elif a=="��" and choice_name=="����":
		print("��Ӯ��")
	elif a=="ʷ����" and choice_name=="����":
		print("��Ӯ��")
	elif a=="����" and choice_name=="����":
		print("ƽ��")
	elif a=="ʯͷ" and choice_name=="ʯͷ":
		print("ƽ��")
	elif a=="ʷ����" and choice_name=="ʷ����":
		print("ƽ��")
	elif a=="����" and choice_name=="����":
		print("ƽ��")
	elif a=="ֽ" and choice_name=="ֽ":
		print("ƽ��")
	elif a=="����" and choice_name=="ʷ����":
		print("��Ӯ��")
	elif a=="ʯͷ" and choice_name=="ʷ����":
		print("��Ӯ��")
	else:
		print("Error: No Correct Name")
import random
x=random.randint(0,4)
a=number_to_name(x)

print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
print("----------------")
print("����ѡ��Ϊ��%s"%(choice_name))
print("�������ѡ��Ϊ��%s"%(a))
rpsls(a,choice_name)


   










   
