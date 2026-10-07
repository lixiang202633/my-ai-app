# 🤖 我的 AI 助手 (My AI Assistant)

一个基于 **FastAPI + 通义千问 API + HTML/JS** 构建的轻量级 AI 对话应用。

## 📸 项目截图
*(在这里你可以插入你刚刚截的网页截图)*

## 🛠️ 技术栈
*   **前端**：HTML5, CSS3 (Flexbox布局), JavaScript (Fetch API, 异步请求)
*   **后端**：Python 3.13, FastAPI, Uvicorn
*   **AI 模型**：通义千问 (qwen-turbo)
*   **环境管理**：python-dotenv (安全存储 API Key)

## ✨ 核心功能
1.  **全栈闭环**：前端输入 -> 后端转发 -> 大模型生成 -> 前端展示。
2.  **防抖优化**：请求期间自动禁用按钮并显示“思考中”，防止重复提交。
3.  **现代 UI**：响应式卡片布局，支持回车快捷发送，提供流畅的悬停与聚焦反馈。
4.  **安全规范**：API Key 通过 `.env` 文件管理，不在代码中硬编码。

## 🚀 如何运行
1.  克隆项目到本地。
2.  安装依赖：`pip install fastapi uvicorn python-dotenv openai`
3.  创建 `.env` 文件并填入：`DASHSCOPE_API_KEY=你的Key`
4.  启动后端：`uvicorn api_demo:app --reload`
5.  双击打开 `index.html` 即可使用。