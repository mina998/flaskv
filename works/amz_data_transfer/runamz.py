import time
from amz.dispatch import run

start = int(time.time())
run()
end = int(time.time())
print('运行时长:', end-start, '秒')