import pygame
from plane_sprites import *


#游戏的初始化
pygame.init()
#创建游戏窗口 391*628
screen = pygame.display.set_mode((391,628))

#绘制背景图像，家在图像数据，blit绘制图像,update更新显示

background = pygame.image.load("./images/background.png")

screen.blit(background,(0,0))

#pygame.display.update()

#绘制飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero,(100,400))
#统一调用update进行渲染
pygame.display.update()
#创建时钟对象
clock = pygame.time.Clock()
#1.定义rect记录飞机的初始位置
hero_rect = pygame.Rect(100,400,80,80)


#创建敌机的精灵和精灵组

enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png",2)

enemy_group = pygame.sprite.Group(enemy , enemy1)


#游戏循环-》意为着游戏正式开始
while True:
    #每秒移动多少次，循环体内代码执行频率
    clock.tick(60)

    #监听事件
    for event in  pygame.event.get():
        #判断事件类型是否是退出事件
        if event.type == pygame.QUIT:
            print("退出游戏...")
            #卸载所有模块
            pygame.quit()
            #exit直接终止当前正在执行的程序
            exit()

    #2.修改飞机位置
    hero_rect.y -=1
    #判断飞机位置
    if (hero_rect.y+hero_rect.height)<=0:
        hero_rect.y = 628

    #3.用bilt方法绘制图像
    screen.blit(background,(0,0))
    screen.blit(hero,hero_rect)

    #让精灵祖调用两个方法
    #update更新组中所有精灵的位置
    enemy_group.update()
    #draw绘制在屏幕上
    enemy_group.draw(screen)


    #4.调用update刷新
    pygame.display.update()

pygame.quit()