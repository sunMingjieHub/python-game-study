import pygame

pygame.init()
#创建游戏窗口 391*628
screen = pygame.display.set_mode((391,628))

#绘制北京图向，家在图像数据，blit绘制图像,update更新显示

background = pygame.image.load("./images/background.png")
screen.blit(background,(0,0))

pygame.display.update()
#游戏循环
while True:
    pass

pygame.quit()