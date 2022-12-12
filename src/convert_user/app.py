import uvicorn
from fastapi import FastAPI
from src.convert_user.views.route import (
    delete_route,
    forgot_password_route,
    login_router,
    signup_router,
    protected_router
)
from fastapi_jwt_auth import AuthJWT   
from src.convert_user.user.schema.user import Settings
app = FastAPI()

@AuthJWT.load_config
def get_config():
    return Settings()

@app.get("/")
def user_info():
    return {"get started with": "user authentic panel"}


app.include_router(signup_router, prefix="/v1/authenticate")
app.include_router(login_router, prefix="/v1/authenticate")
app.include_router(protected_router , prefix="/v1/authenticate")
app.include_router(forgot_password_route, prefix="/v1/authenticate")
app.include_router(delete_route, prefix="/v1/authenticater")


if __name__ == "__main__":
    uvicorn.run("src.conver_user.app:app", host="127.0.0.1", port=6070)
