FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install mcp[cli] fastapi uvicorn sse-starlette starlette pydantic-settings
EXPOSE 3002
CMD ["python", "server.py"]
