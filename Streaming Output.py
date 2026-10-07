import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

print("--- AI 正在思考（流式输出） ---")

# 关键参数：stream=True
response = client.chat.completions.create(
    model="qwen-turbo",
    messages=[
        {"role": "system", "content": "你是一个资深的电商运营专家。"},
        {"role": "user", "content": "帮我写一篇200字左右的便携榨汁杯小红书文案，要带emoji。"}
    ],
    stream=True  # 开启流式输出
)

# 遍历生成器，逐字打印
for chunk in response:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="", flush=True)

print("\n\n--- 输出完毕 ---")