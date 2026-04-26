# Local Agent Gateway V2.2 - MCP Standard Bridge

## 1. 專案簡介 (Project Overview)
本專案是一套基於 **Model Context Protocol (MCP)** 協議開發的高性能地端 AI 代理閘道器。它作為「算力中心」與「專案工作區」之間的標準化介面，讓 AI 代理具備跨容器的檔案系統操作能力與硬體資源維護權限。

## 2. 專案架構 (System Architecture)
- **大腦層 (Intelligence)**: 位於 `llm-server` 的推理引擎 (Ollama/llama.cpp)。
- **神經層 (Gateway)**: 本專案 (FastAPI + FastMCP)，處理協議轉換與安全。
- **執行層 (Worker)**: Docker 容器化的 MCP Executor，負責實體 I/O。

## 3. 部署與快速啟動 (Quick Start)
```bash
# 編譯映像檔
sudo docker build -t mcp-agent-gateway .

# 啟動並掛載目標專案
sudo docker run -d --name mcp-ea-agent \
  -p 3002:3002 \
  -e MCP_APP_NAME=EA-Expert \
  -v /home/ubuntu/projects/EA_trade_bot:/projects \
  --restart always \
  mcp-agent-gateway
```

## 4. 調用能力 (Capabilities)
- **Filesystem**: `list_files`, `read_file`, `write_file`。
- **Hardware**: `reset_gpu_resources` (一鍵清空 VRAM)。

## 5. 版本紀錄 (Changelog)
- **v1.0**: 打通跨容器連線 PoC。
- **v2.0**: 引入 FastAPI + FastMCP 標準架構，支援 SSE。
- **v2.1**: 實現專案脫鉤設計與 Docker 容器化封裝。
- **v2.2 (Current)**: 
    - **解決 421 錯誤**: 修復了跨容器調用時觸發的 `Misdirected Request` 問題。
    - **安全防禦調整**: 透過 `TransportSecuritySettings` 關閉了針對內網環境的 DNS Rebinding Protection。
    - **CORS 優化**: 全面開放跨來源請求，確保 Open WebUI 與 Docker 橋接穩定性。
