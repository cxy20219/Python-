import sys                   # 导入系统模块
import pygame
from pygame.locals import *  # 导入pygame中常量

SCREENWIDTH = 822              # 窗口宽度 
SCREENHEIGHT = 199             # 窗口高度
FPS = 30                       # 更新画面时间

class MyMap():
    def __init__(self,x,y):
        # 加载背景图片定义x,y坐标
        self.bg=pygame.image.load("image/bg.png").convert_alpha()
        self.x=x
        self.y=y
    def map_rolling(self):
        # 根据x坐标判断是否移出窗体
        if self.x <-790:   # 小于-790说明地图已经移动完毕
            self.x=800     # 给地图一个新的坐标点
        else:
            self.x-=5      # 向左移动5个像素
    # 更新地图
    def map_update(self):
        SCREEN.blit(self.bg,(self.x,self.y))

from itertools import cycle    # 导入迭代工具
class Marie():
    def __init__(self):
        # 初始化玛丽矩形
        self.rect= pygame.Rect(0,0,0,0)
        self.jumpState = False # 跳跃的状态
        self.jumpHeight = 130  # 跳跃的高度
        self.lowest_y = 140    # 最低坐标
        self.jumpValue = 0     # 跳跃增变量
        # 玛丽地图索引
        self.marieIndex = 0
        self.marieIndexGen = cycle([0,1,2])
        # 加载玛丽图片
        self.adventure_img=(
            pygame.image.load("image/adventure1.png").convert_alpha(),
            pygame.image.load("image/adventure2.png").convert_alpha(),
            pygame.image.load("image/adventure3.png").convert_alpha(),
        )
        self.jump_audio=pygame.mixer.Sound("audio/jump.wav")  # 跳音效
        self.rect.size=self.adventure_img[0].get_size()
        self.x=50              # 绘制玛丽的x坐标
        self.y=self.lowest_y   # 绘制玛丽的y坐标
        self.rect.topleft = (self.x, self.y)
    # 跳状态
    def jump(self):
        self.jumpState=True
    
    # 玛丽移动
    def move(self):
        if self.jumpState:                                      # 当起跳的时候 
            if self.rect.y >= self.lowest_y:                    # 如果站在地上
                self.jumpValue = -5                             # 以5个像素值向上移动
            if self.rect.y <= self.lowest_y - self.jumpHeight:  # 玛丽到达顶部回落
                self.jumpValue = 5                              # 以5个像素值向下移动
            self.rect.y += self.jumpValue                       # 通过循环改变玛丽的y坐标
            if self.rect.y >= self.lowest_y:                    # 如果玛丽回到地面关闭跳跃状态
                self.jumpState = False                              

    # 绘制玛丽
    def draw_marie(self):
        # 匹配玛丽动图
        marieIndex=next(self.marieIndexGen)
        # 绘制玛丽
        SCREEN.blit(self.adventure_img[marieIndex],(self.x,self.rect.y))

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

    # 创建地图对象
    bg1 = MyMap(0,0)
    bg2 = MyMap(800,0)

    # 创建玛丽对象
    marie = Marie()

    while True:
        # 实现无限循环滚动的地图
        if over == False:
            # 绘制地图起到更新地图的作用
            bg1.map_update()

            # 移动地图
            bg1.map_rolling()
            bg2.map_update()
            bg2.map_rolling()

            # 玛丽移动
            marie.move()

            # 绘制玛丽
            marie.draw_marie()

        # 获取单击事件
        for event in pygame.event.get():
            # 如果单击了关闭窗体就将窗体关闭
            if event.type == QUIT:
                pygame.quit()   # 退出窗口
                sys.exit()      # 关闭窗口

            # 按下空格键开启跳状态
            if event.type == KEYDOWN and event.key == K_SPACE:
                if marie.rect.y >= marie.lowest_y:   # 如果玛丽在地面上
                    marie.jump_audio.play()          # 播放玛丽跳跃音效
                    marie.jump()                     # 开启玛丽跳的状态     

        pygame.display.update() # 更新整个窗体
        FPSCLOCK.tick(FPS)      # 循环多长时间运行一次
if __name__=="__main__":
    mainGame()


