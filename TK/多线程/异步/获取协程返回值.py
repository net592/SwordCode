import asyncio
import time
async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)
    return "bobby"

def callback(url, future):
    print(url)
    print("send email to bobby")

if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    get_future = asyncio.ensure_future(get_html("http://www.imooc.com")) # 相当于开启一个future
    loop.run_until_complete(get_future) # 事件循环
    print(get_future.result()) # 获取结果