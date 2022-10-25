# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/10/25 11:46:50

import uvicorn
from fastapi import FastAPI, Response
from api.crawler import main as new
import json

app = FastAPI()

@app.get("/api")
def news(response: Response, index: int = 0, origin: str = 'zhihu', cache: str = 'null'):
    response.headers["Cache-Control"] = "max-age=86400, immutable, stale-while-revalidate"
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    response.headers["Access-Control-Allow-Origin"] = "*"
    if origin == "undefined":
        origin = "zhihu"
    return new(index, origin)


if __name__ == "__main__":
    uvicorn.run("index:app", host="127.0.0.1", port=62, log_level="info", reload=True)



# index = int(input('输入页数：'))
# origin = input('可输入 zhihu 或空：')
# data = new(index=index, origin=origin)
# print(data)