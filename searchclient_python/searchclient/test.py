import argparse
import re
import sys

import memory
from state import State
from strategy import StrategyBFS, StrategyDFS, StrategyBestFirst
from heuristic import AStar, WAStar, Greedy


h=[]
h.append(2,1)
h.append(2,4)
h.append(1,5)
print(sum(min(h)))
