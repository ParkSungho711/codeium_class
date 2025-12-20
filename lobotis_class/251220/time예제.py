# import time
# hi = '안녕하세요'
# bye = '안녕히가세요'

# print(hi)
# time.sleep(3)
# print(bye)

import time

messege = '''
🎅 : 허허허~ 메리 크리스마스~🎄
올해도 즐거운 선물을 받기를 바래~🔔
🎄🎅🎄Merry~ Merry~ chistmas~~🎄🎅🎄
🔔🔔🎅🎄🔔🔔🎅🎄🔔🔔🎅🎄🔔🔔🎅🎄🔔🔔
'''
for i in messege:
    print(i, end="", flush=True)
    time.sleep(0.1)