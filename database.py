from fastapi import status
from fastapi import HTTPException
import os
from supabase import Client , create_client
from dotenv import load_dotenv

load_dotenv()
supabase_url = os.getenv("SUPABASE_URL")
supabase_key= os.getenv("SUPABASE_SERVICE_KEY")
def validation():
    if not supabase_url or not supabase_key:
        raise HTTPException(status_code=500,detail="ENVIRONMENT VARIABLES NOT DEFINED")
    else:
        pass
    return True
validation()
try:
    supabase:Client=create_client(supabase_url,supabase_key)
except Exception as e :
    raise HTTPException(status_code=500,detail=f"ERROR:-{e}")

    

       

            


