import os
import json
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse  # 新增：用于流式响应
from openai import OpenAI

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

# 新增：这是一个“生成器函数”，它会一段一段地吐出数据
def stream_generator(question: str):
    response = client.chat.completions.create(
        model="qwen-turbo",
        messages=[{"role": "user", "content": question}],
        stream=True  # 关键：开启流式模式
    )
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            # 把每个字打包成 JSON 格式，方便前端解析
            data = {"content": chunk.choices[0].delta.content}
            yield f"data: {json.dumps(data, ensure_ascii=False)}\n\n"

@app.get("/chat")
def chat_with_ai(question: str):
    # 返回一个流式响应，媒体类型必须是 text/event-stream (SSE)
    return StreamingResponse(stream_generator(question), media_type="text/event-stream")

app.mount("/", StaticFiles(directory=".", html=True), name="static")