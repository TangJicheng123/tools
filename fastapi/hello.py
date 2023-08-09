import time
from fastapi import FastAPI, Request, Response

# 创建FastAPI应用
app = FastAPI()

# 自定义计时中间件
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = (time.time() - start_time) * 1000
    response.headers["X-Process-Time"] = str(process_time)
    return response

# 定义一个路由，将HTTP GET请求映射到根路径
@app.get("/")
def read_root():
    return {"Hello": "World"}

# 定义另一个路由，将HTTP GET请求映射到路径 /items/{item_id}
@app.get("/items/{item_id}")
def read_item(item_id: int, query_param: str = None):
    return {"item_id": item_id, "query_param": query_param}
