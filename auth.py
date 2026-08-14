from h11._abnf import status_code
from database import supabase
from fastapi import HTTPException , Request

def ip_(request:Request):
    try:
        clint_ip = request.client.host
        header = request.headers("user-agent")
        return clint_ip,header
    except Exception as e:
        raise HTTPException(status_code=400,detail=f"Error: {e}")
    


def isexist(email):
    result = supabase.table('users').select('*').eq('email',email).execute()
    if result.data:
        return True
    else :
        return False


def strong_password(password):
    if not any(c.isupper() for c in password):
        raise HTTPException(status_code=401,detail="Password must contain One Uppercase Letter")
    elif not any(c.islower() for c in password):
        raise HTTPException(status_code=401,detail="Password must contain One lowercase Letter")
    elif any(c.isspace()for c in password):
        raise HTTPException(status_code=401,detail="Remove all spaces from password")
    elif not any(c.isdigit() for c in password):
        raise HTTPException(status_code=401,detail="password must contain One digit")
    elif not any (c in '!@#$%' for c in password):
        raise HTTPException(status_code=401,detail="Password must contain One Spacial Character")
    else:
        return True

def signup(business_name,name,Username,password,request:Request):
    ip_address = ip_(request)
    exist = isexist(Username)
    if exist == True:
        raise HTTPException(status_code=400,detail="user already exists")
    else:
        is_strong = strong_password(password)
        try:
            result = supabase.table('users').insert({
                'business_name':business_name,
                'name':name,
                'email':Username,
                'password':password
            }).execute()
        except Exception as e:
            raise HTTPException(status_code=400,detail=f"ERROR:-{e}")
    return {
        'message':'user created sussefully'
    }










