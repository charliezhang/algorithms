# Expand a random range from 1-5 to 1-7
# http://stackoverflow.com/questions/137783

import random
from collections import defaultdict

def rand5():
  return random.randint(1, 5)

def rand7():
  i, j = 0, 1
  while True:
    i = i * 5 + rand5() - 1
    j *= 5
    if (i < j - j % 7):
      return i % 7 + 1
    i, j = i % 7, j % 7

def test():
  ans1 = defaultdict(int)
  ans2 = defaultdict(int)
  for i in xrange(100000):
    ans1[rand7()-1] += 1
    ans2[random.randint(0, 6)] += 1
  print 'Ans\tCnt1\tCnt2\tDiff\n'
  for i in xrange(7):
    print '%d\t%d\t%d\tDiff%.2f%%\n' % (
        i, ans1[i], ans2[i],
        100.0 * abs(ans1[i] - ans2[i]) / min(ans1[i], ans2[i]))

if __name__ == '__main__':
  test()
