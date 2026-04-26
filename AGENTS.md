# 地端 Agent Server V2 拓撲總表

本專案作為地端 3080 算力中心與跨容器工具鏈的「註冊閘道器」。

## 1. 核心算力 (The Brain)
- **服務**: Ollama (14B Models)
- **位址**: http://localhost:11434
- **模型**: qwen2.5-coder:14b, deepseek-r1:14b

## 2. 實體工具 (The Hands)
- **服務名稱**: EA-Bot-Filesystem
- **提供者容器**: 
- **映射端點**: http://10.223.81.130:3002/mcp/sse
- **掛載專案**: /home/ubuntu/projects/EA_trade_bot

## 3. 介面層 (The Interface)
- **入口**: Open WebUI
- **連線協議**: MCP (via FastAPI Gateway)
- **對外路徑**: https://agent.wetrytrysee.cc/gateway/3000/

## 4. 管理指令 (Maintenance)
- **清空顯存**: ~/flush_vram.sh
- **重啟工具**: sudo docker restart mcp-ea-hand
