import pygame

pygame.init()
#创建游戏窗口 391*628
screen = pygame.display.set_mode((391,628))

#绘制北京图向，家在图像数据，blit绘制图像,update更新显示

background = pygame.image.load("./images/background.png")

screen.blit(background,(0,0))

#pygame.display.update()

#绘制飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero,(100,400))
#统一调用update进行渲染
pygame.display.update()


#游戏循环-》意为着游戏正式开始
while True:
    pass

pygame.quit()