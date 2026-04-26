# Local Agent Gateway V2.1 - MCP Standard Bridge

## 1. 專案簡介 (Project Overview)
本專案為一套基於 **Model Context Protocol (MCP)** 協議開發的高性能地端 AI 代理閘道器。它作為「算力中心」與「專案工作區」之間的標準化介面，讓 AI 代理具備跨容器的檔案系統操作能力與硬體資源維護權限。採用 **Project-Agnostic (專案無關)** 設計，可隨時掛載至任何開發專案中。

## 2. 專案架構 (System Architecture)
- **大腦層 (Intelligence)**: 位於 `llm-server` 的推理引擎 (Ollama/llama.cpp)，提供大參數專家模型。
- **神經層 (Gateway)**: 本專案 (FastAPI + FastMCP)，處理協議轉換、安全性檢查與跨網域路由。
- **執行層 (Worker)**: Docker 容器化的 MCP Executor，負責實體 I/O，與主機檔案系統隔離。

## 3. 部署與快速啟動 (Quick Start)
本專案支援一鍵部署並對接任何地端專案：
```bash
# 編譯映像檔
sudo docker build -t mcp-agent-gateway .

# 啟動並掛載目標專案 (例如 EA 機器人)
sudo docker run -d --name mcp-ea-agent \
  -p 3002:3002 \
  -e MCP_APP_NAME=EA-Expert \
  -v /home/ubuntu/projects/EA_trade_bot:/projects \
  --restart always \
  mcp-agent-gateway
```

## 4. 調用能力 (Capabilities)
對接端可透過標準 SSE 協議調用以下「專家技能」：
- **Filesystem**: `list_files`, `read_file`, `write_file` (支援專案級代碼讀寫)。
- **Hardware**: `reset_gpu_resources` (一鍵重置 GPU 顯存與推論服務)。

## 5. 版本紀錄 (Changelog)
- **v1.0**: 打通跨容器連線PoC。
- **v2.0**: 引入 FastAPI + FastMCP 標準架構，支援 SSE。
- **v2.1 (Current)**: 
    - 實現專案脫鉤設計 (Project-Agnostic)。
    - 完成 Docker 容器化封裝。
    - 導入 VRAM 自動清理工具與路徑安全校驗。
