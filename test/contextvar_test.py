import asyncio
import contextvars

# 创建一个上下文变量
request_id = contextvars.ContextVar("request_id")

# 定义一个异步任务，打印上下文变量的值
async def print_request_id():
    id = request_id.get()
    print(f"Request ID: {id}")

# 定义一个异步函数，设置上下文变量的值，并调用异步任务
async def process_request(id, tid):
    token = request_id.set(id)
    print(f"{tid}: {request_id.get()}")
    await print_request_id()
    request_id.reset(token)

# 在主函数中创建事件循环，调用异步函数
async def main():
    await asyncio.gather(
        process_request("123", 1),
        process_request("456", 2),
    )

# 运行主函数
asyncio.run(main())
