#!/bin/bash
echo '正在徹底清空 3080 顯存...'
sudo systemctl restart ollama
echo '✅ 顯存已完全釋放，Ollama 已重啟。'
