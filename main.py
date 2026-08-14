from fastapi import Request
from fastapi.exceptions import FastAPIDeprecationWarning
from fastapi import FastAPI
from pydantic import BaseModel
from auth import signup,ip_

app = FastAPI()
@app.get('/')
def read_root():
    return {f"Welocome to our BackendS"}
@app.get('/ip')
def get_ip(request:Request):
    ip_address , browser_name = ip_(request)
    return{
        "ip_address":ip_address,
        "browser_name":browser_name
    }
class signup_request(BaseModel):
    business_name:str
    name:str
    Username:str
    password:str

@app.post('/signup')
def signup_request_handler(request:signup_request):
    return signup(
        business_name=request.business_name,
        name=request.name,
        Username=request.Username,
        password=request.password
    )





