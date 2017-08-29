from liaoxuefeng.webapp.www.orm import *

import asyncio

loop  = asyncio.get_event_loop()
loop.run_until_complete(create_pool(loop, user='root', password='', db='test'))
data = loop.run_until_complete(select('select * from python WHERE id = ?', [2]))

print(data)

data2 = loop.run_until_complete(execute("INSERT INTO `python` (`id`, `num`) VALUES (NULL, ?)", [5], False))
print(data2)