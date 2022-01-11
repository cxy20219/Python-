import sys                   # 导入系统模块
import pygame
from pygame.locals import *  # 导入pygame中常量

SCREENWIDTH = 822              # 窗口宽度 
SCREENHEIGHT = 199             # 窗口高度
FPS = 30                       # 更新画面时间

def mainGame():
    score = 0                  # 得分
    over = False               # 游戏结束标志
    global SCREEN, FPSCLOCK
    pygame.init()              # pygame初始化

    # 使用Python时钟控制每个循环多长时间运行一次。
    # 使用时钟前必须创建一个Clock对象的实例
    FPSCLOCK = pygame.time.Clock()

    # 创建窗体实现交互
    SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
    pygame.display.set_caption("玛丽冒险")  # 设置窗体标题
    while True:
        # 获取单击事件
        for event in pygame.event.get():
            # 如果单击了关闭窗体就将窗体关闭
            if event.type == QUIT:
                pygame.quit()   # 退出窗口
                sys.exit()      # 关闭窗口
        pygame.display.update() # 更新整个窗体
        FPSCLOCK.tick(FPS)      # 循环多长时间运行一次
if __name__=="__main__":
    mainGame()


