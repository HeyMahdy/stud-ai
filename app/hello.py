from fastapi import FastAPI
from Models.testModel2 import Comment , CommentCreate

from DatabaseConfiguration.databaseConfig import SessionDep, engine, Base
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
Base.metadata.create_all(bind=engine)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/post")
async def main_post_inthis(cmodel: CommentCreate , db : SessionDep ):
    cbd = Comment(title=cmodel.title,description=cmodel.description)
    db.add(cbd)
    db.commit()
    return {"message": "Comment added successfully"}

@app.get("/all")
async def get_all(db : SessionDep):
    return db.query(Comment).all()