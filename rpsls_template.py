#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：邵清懿
日期：2021年5月27日
"""

import random


# 0 - 石头
# 1 - 史波克
# 2 - 布
# 3 - 蜥蜴
# 4 - 剪刀


def name_to_number(name):#将游戏对象对应到不同的整数
        if name == '石头':
                return 0
        elif name == '史波克':
                return 1
        elif name == '布':
                return 2
        elif name == '蜥蜴':
                return 3
        elif name == '剪刀':
                return 4
        else:
                print('Error:No Correct Name')
 


def number_to_name(number):#将整数对应到不同的游戏对象
        if number in range(0,5):
                if number == 0:
                        return '石头'
                elif number == 1:
                        return '史波克'
                elif number == 2:
                        return '布'
                elif number == 3:
                        return '蜥蜴'
                elif number == 4:
                        return '剪刀'
        else:
                print("请输入您的选择：")
    # 使用if/elif/else语句将不同的整数对应到游戏的不同对象
    # 不要忘记返回结果



def rpsls(player_choice):#用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果
        print()
        print('您的选择为：',player_choice)
        player_number = name_to_number(player_choice)
        comp_number = random.randrange(0,5)
        comp_choice = number_to_name(comp_number)
        print('计算机的选择为：',comp_choice)
        if (player_number - comp_number)%5==1 or (player_number - comp_number)%5==2:
                print('您赢了！')
        elif (player_number - comp_number)%5==3 or (player_number - comp_number)%5==4:
                print('计算机赢了！')
        else:
                print('您和计算机出的一样呢！')

var=0
while(var==0
      ):
        print("欢迎使用RPSLS游戏")
        print("----------------")
        print("请输入您的选择:")
        choice_name=input()
        rpsls(choice_name)
        var=int(input('按0继续，按任意键退出：'))


    # 输出"-------- "进行分割
    # 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice

    # 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number

    # 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number

    # 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象

    # 在屏幕上显示计算机选择的随机对象

    # 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果

    # 如果用户和计算机选择一样，则显示“您和计算机出的一样呢”，如果用户获胜，则显示“您赢了”，反之则显示“计算机赢了”



# 对程序进行测试
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
rpsls(choice_name)


