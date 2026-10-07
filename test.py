import os
from dotenv import load_dotenv

# 1. 加载 .env 文件
load_dotenv() 

# 2. 读取环境变量
api_key = os.getenv("DASHSCOPE_API_KEY")

# 3. 打印结果
if api_key:
    print("✅ 成功！环境变量已生效。")
    # 安全起见，只显示头尾
    print(f"Key 预览: {api_key[:6]}******{api_key[-4:]}")
else:
    print("❌ 失败！没有读取到环境变量。")