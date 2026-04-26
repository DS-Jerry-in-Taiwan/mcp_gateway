import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mcp.server.fastmcp import FastMCP

# 從環境變數讀取名稱，預設為 Generic-Agent
APP_NAME = os.getenv('MCP_APP_NAME', 'Generic-Agent-Executor')
mcp = FastMCP(APP_NAME)

# 鎖定容器內的虛擬路徑 /projects
SAFE_ROOT = '/projects'

@mcp.tool()
def list_files(sub_path: str = '.'):
    '''獲取目前工作目錄的檔案清單'''
    try:
        target = os.path.join(SAFE_ROOT, sub_path.strip('/'))
        return os.listdir(target)
    except Exception as e:
        return [str(e)]

@mcp.tool()
def read_file(file_path: str):
    '''讀取檔案內容進行分析'''
    try:
        target = os.path.join(SAFE_ROOT, file_path.strip('/'))
        with open(target, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return str(e)

@mcp.tool()
def write_file(file_path: str, content: str):
    '''修改或建立檔案'''
    try:
        clean_path = file_path.strip('/')
        if '..' in clean_path: return 'Error: Boundary violation'
        target = os.path.join(SAFE_ROOT, clean_path)
        os.makedirs(os.path.dirname(target), exist_ok=True)
        with open(target, 'w', encoding='utf-8') as f:
            f.write(content)
        return f'Success: {file_path} updated'
    except Exception as e:
        return str(e)

@mcp.tool()
def reset_gpu_resources():
    '''重置 GPU 與推論服務資源'''
    import subprocess
    try:
        subprocess.run(['bash', './flush_vram.sh'], check=True)
        return 'Success: GPU resources reset'
    except Exception as e:
        return f'Error: {str(e)}'

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=['*'])
app.mount('/mcp', mcp.sse_app())

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=3002)
