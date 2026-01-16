from fastapi import FastAPI
from routers import users, posts, comments, likes

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(posts.router, prefix="/posts", tags=["Posts"])
app.include_router(comments.router, prefix="/post", tags=["Comments"])
app.include_router(likes.router, prefix="/post", tags=["Likes"])
@app.get("/")
def read_root():
    return {"message": "Cloud Community Server is Running!"}