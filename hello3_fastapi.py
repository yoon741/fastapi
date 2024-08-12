from fastapi import FastAPI

# fastapi 앱 실행 방법
# python -m uvicorn 파일명:app --reload             (파일명은 확장자 없이 입력 밑에 줄 처럼)
# python -m uvicorn hello2_fastapi:app --reload

app = FastAPI()
@app.get('/')
def index():
    return 'Hello, World!!'

# 추천 하지 않는 방식
@app.get('/sayHello')
def sayhello(msg :str):
    return f'Hello, {msg}!!'

# RESTful API 방식
@app.get('/sayAgain/{msg}')
def sayagain(msg :str):
    return f'Hello, {msg}!!'

# __name__: 실행중인 모듈 이름을 의미하는 매직키워드
# 만일, 파일을 직접 실행하면 __name__이름은 __main__으로 자동지정
if __name__ == "__main__":
    import uvicorn
    uvicorn.run('hello3_fastapi:app', reload=True)