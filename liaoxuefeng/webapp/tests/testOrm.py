from liaoxuefeng.webapp.www.orm import *

import asyncio

loop  = asyncio.get_event_loop()
loop.run_until_complete(create_pool(loop, user='root', password='', db='test'))

data = select('select * from python WHERE id = ?', [2])
print(data)