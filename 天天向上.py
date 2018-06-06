#天天向上.py

import math

#数值计算

dayup = math.pow( 1+0.001 , 365 )
daydown = math.pow ( 1-0.001 , 365 )

#输出控制

print("天天向上的值为{:.2f},天天向下的值为{:.2f}".format(dayup,daydown))
