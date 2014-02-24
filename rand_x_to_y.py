# Convert a random range from 1-x to 1-y

import sys
import random
from collections import defaultdict

def rand_x_to_y(x, y):
  i, j = 0, 1
  while True:
    i = i * x + random.randint(1, x) - 1
    j *= x
    if (i < j - j % y):
      return i % y + 1
    i, j = i % y, j % y

def test():
  x = int(sys.argv[1])
  y = int(sys.argv[2])
  ans1 = defaultdict(int)
  ans2 = defaultdict(int)
  for i in xrange(100000):
    ans1[rand_x_to_y(x, y) - 1] += 1
    ans2[random.randint(1, y) - 1] += 1
  print 'Ans\tCnt1\tCnt2\tDiff\n'
  for i in xrange(y):
    print '%d\t%d\t%d\tDiff%.2f%%\n' % (
        i, ans1[i], ans2[i],
        100.0 * abs(ans1[i] - ans2[i]) / min(ans1[i], ans2[i]))

if __name__ == '__main__':
  test()
