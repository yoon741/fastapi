from fastapi import FastAPI
from sqlalchemy import create_engine, Column, String, select
from sqlalchemy.orm import declarative_base, Session
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

# Jinja2Template
# 파이썬용 템플릿 엔진
# 다양한 웹 프레임워크에서 템플릿 렌더링을 위해 사용
# 템플릿(html)에 동적으로 데이터(db 조회 객체)를 삽입해서
# 최종 결과물을 만드는 역할 담당
# jinja.palletsprojects.com


sqlite_url = 'sqlite:///app/cloud2024.db'
engine = create_engine(sqlite_url, connect_args={}, echo=True)

Base = declarative_base()

class Zipcode(Base):
    __tablename__ = 'zipcode'

    zipcode = Column(String, index=True)
    sido = Column(String)
    gugun = Column(String)
    dong = Column(String)
    ri = Column(String)
    bunji = Column(String)
    seq = Column(String, primary_key=True)

app = FastAPI()
templates = Jinja2Templates(directory="views/templates")



@app.get('/')
def index():
    return 'Hello, jinja2!!'


@app.get('/zipcode/{dong}')
def zipcode(dong: str):
    result = ''

    # sessionmaker 없이 디비 객체 직접 생성
    with Session(engine) as sess:
        stmt = select(Zipcode).where(Zipcode.dong.like(f'{dong}%'))
        rows = sess.scalars(stmt)

        for row in rows:
            result += f'{row.zipcode} {row.sido} {row.gugun} {row.dong}'

    return f'{result}'



@app.get('/zipcode2/{dong}', response_class=HTMLResponse)
def zipcode(dong: str, req: Request):
    # 입력한 동으로 zipcode에서 검색하고 결과를 result에 저장
    with Session(engine) as sess:
        stmt = select(Zipcode).where(Zipcode.dong.like(f'{dong}%'))
        result = sess.scalars(stmt).all()

    # 저장된 검색 결과를 템플릿 엔진을 이용해서 html 결과문서를 만들기 위해
    # TemplateResponse 함수 호출
    return templates.TemplateResponse('zipcode.html',
                {'request': req, 'rows': result, 'sayhello': 'Hello, Jinja2!!'})

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('jinja01:app', reload=True)



