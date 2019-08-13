import random

class Meiro():
    WALL = 1
    ROOT = 0

    def __init__(self, field_x, field_y, mode):
        self.field_x = field_x
        self.field_y = field_y
        self.field = []
        self.mode = mode  # 棒倒し法の場合は１、穴掘り法は２、それ以外は０
        # 迷路は5*5以上、奇数
        if self.field_x < 5 or self.field_y < 5:
            print('大きさは５*５以上')
            exit()
        if self.field_x % 2 == 0:
            self.field_x += 1
        if self.field_y % 2 == 0:
            self.field_y += 1

        if mode != 0:
            print('正しいモードを選択(0)')
            exit()

    # 迷路の枠を生成
    def meiro_frame(self):
        if self.mode == 0:
            for i in range(self.field_y):
                row = []
                for j in range(self.field_x):
                    if i == 0 or i == self.field_y - 1 or j == 0 or j == self.field_x - 1:  # 上下枠
                        sell = self.WALL
                    else:
                        sell = self.ROOT
                    row.append(sell)
                self.field.append(row)
        self.field[1][1] = 'S'
        self.field[self.field_y - 2][self.field_x - 2] = 'G'

    # 迷路を表示
    def meiro_show(self):
        for i in range(self.field_y):
            for j in range(self.field_x):
                if self.field[i][j] == self.WALL:
                    print('###', end="")
                elif self.field[i][j] == self.ROOT:
                    print('   ', end="")
                elif self.field[i][j] == 'S':
                    print('STR', end="")
                elif self.field[i][j] == 'G':
                    print('GOL', end="")
            print()
        print()

    # 迷路生成(棒倒し法)
    def meiro_make_stick(self):
        # 基礎を生成(一つ起きにブロックを配置)
        # 上下左右を定義
        x_dir = [1, 0, -1, 0]
        y_dir = [0, 1, 0, -1]
        for i in range(self.field_y):
            for j in range(self.field_x):
                # 1マス置きに倒す方向を考える
                if j > 0 and j < self.field_x - 1 and j % 2 == 0 and i > 1 and i < self.field_y - 2 and i % 2 == 0:
                    while True:
                        direction = random.randint(0, 3)
                        if self.field[i + y_dir[direction]][j + x_dir[direction]] == self.WALL or (
                                i > 2 and direction == 3):
                            continue
                        else:
                            self.field[i + y_dir[direction]][j + x_dir[direction]] = self.WALL
                            self.field[i][j] = self.WALL
                            break

# 与えられたモードで与えられた個数迷路を生成する
def meiro_generator(width, height, mode, count):
    meiros = []
    for i in range(count):
        meiro = Meiro(width, height, mode)
        meiro.meiro_frame()
        if mode == 0:
            meiro.meiro_make_stick()
        meiro.meiro_show()