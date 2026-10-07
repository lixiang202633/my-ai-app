import os
from dotenv import load_dotenv
from openai import OpenAI

# 1. 加载 .env 文件
load_dotenv()

# 2. 初始化通义千问客户端（使用阿里云的兼容接口）
client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

# 3. 发送请求
print("正在请求 AI，请稍候...")
response = client.chat.completions.create(
    model="qwen-turbo", # 这里填通义千问的模型名称
    messages=[
        {"role": "system", "content": "你是一个资深的电商运营专家。"},
        {"role": "user", "content": "请帮我写一句便携榨汁杯的独立站广告语。"}
    ]
)

# 4. 打印结果
print("\n--- AI 回复 ---")
print(response.choices[0].message.content)