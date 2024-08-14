from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.dbfactory import db_startup, db_shutdown


# 서버시작시 디비 생성
# asynccontextmanager : 비동기 컨텍스트 관리자
# 비동기 지원 프로그램에서 각종 리소스 등을 관리하는데 사용하는 특수한 프로그램
# 주로 비동기 데이터베이스 연결, 네트워크 관련 작업들을 처리하는데 사용
# 단, 비동기 처리 대상 함수들은 async라는 지정자로 정의해야 함
@asynccontextmanager
async def lifespan(app: FastAPI):
    await db_startup()      # 애플리케이션 시작시 실행 
    yield                   # 애플리케이션 실행중에는 일시 중지
    await db_shutdown()     # 애플리케이션 종료시 실행                       # 4


# lifespan : FastAPI 애플리케이션의 수명주기동안 실행ㅇ할 코드를 정의한 함수
# asynccontextmanager에 의해 관리될 작업을 정의하는 용도로 사용
app = FastAPI(lifespan=lifespan)                                         # 1


@app.get('/')
def index():
    return 'Hello, APIRouter!!'                                          # 3


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('apirouter01:app', reload=True)                     # 2