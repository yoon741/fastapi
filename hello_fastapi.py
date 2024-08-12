from fastapi import FastAPI

# fastapi 앱 실행 방법
# python -m uvicorn 파일명:app --reload             (파일명은 확장자 없이 입력 밑에 줄 처럼)
# python -m uvicorn hello_fastapi:app --reload

app = FastAPI()

@app.get('/')
def index():
    return 'Hello, World!!'