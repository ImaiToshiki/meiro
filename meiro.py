from meiro_oth import Meiro
from meiro_oth import meiro_generator

#20*20の迷路を棒倒し法で生成する
meiro1 = Meiro(20, 20, 0)
meiro1.meiro_frame()
meiro1.meiro_make_stick()
meiro1.meiro_show()