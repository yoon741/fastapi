from datetime import datetime
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

# 회원정보를 이용한 CRUD
# userid, passwd, name, email, regdate

# 회원 모델 정의
class Member(BaseModel):
    userid: str
    passwd: str
    name: str
    email:  str
    regdate: datetime

# 회원정보 데이터 저장용 변수
member_db: List[Member] = []

app = FastAPI()

@app.get('/')
def index():
    return 'Hello, pydantic2!!'


# 회원정보 데이터 조회
@app.get('/mem', response_model=List[Member])
def member():
    return member_db


# 회원 데이터 추가
@app.post('/memadd', response_model=Member)
def memberok(mem: Member):
    member_db.append(mem)
    return mem


# 회원 정보 데이터 추가
@app.get('/memadd', response_model=Member)
def memberok():
    mem = Member(userid='AA11', passwd='a12', name='13', email='AA@12.13', regdate='2024-01-01T08:35:54.204Z')
    member_db.append(mem)
    mem = Member(userid='BB22', passwd='b23', name='24', email='BB@12.13', regdate='2024-05-01T08:35:54.204Z')
    member_db.append(mem)
    mem = Member(userid='CC11', passwd='c34', name='35', email='CC@12.13', regdate='2024-08-01T08:35:54.204Z')
    member_db.append(mem)
    return mem

# 회원 데이터 userid로 상세 조회
@app.get('/memone/{userid}', response_model=Member)
def memone(userid: str):
    findone = Member(userid='none', passwd='none', name='none', email='none', regdate='1970-01-01T00:00:00.000Z')
    for mem in member_db:
        if mem.userid == userid:
            findone = mem
    return findone


# 회원 데이터 삭제
@app.delete('/mem/{userid}', response_model=Member)
def memrmv(userid: str):
    rmvone = Member(userid='none', passwd='none', name='none', email='none', regdate='1970-01-01T00:00:00.000Z')
    for idx, mem in enumerate(member_db):
        if mem.userid == userid:
            rmvone = member_db.pop(idx)
        return rmvone


# 회원데이터 수정
@app.put('/mem', response_model=Member)
def memmod(one: Member):
    putone = Member(userid='none', passwd='none', name='none', email='none', regdate='1970-01-01T00:00:00.000Z')
    for idx, mem in enumerate(member_db):
        if mem.userid == one.userid:
            member_db[idx] = one
            putone = one
    return putone


if __name__ == "__main__":
    import uvicorn
    uvicorn.run('pydantic02:app', reload=True)
