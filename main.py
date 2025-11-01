from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Post(BaseModel):
	title: str
	content: str
	published: bool = True
	rating: Optional[int] = None

@app.get("/login") #this decorator turn this into an actual path operaion. / is the root path 
def get_user():
	return {"message": "Hello World!!!!"} 
	# What ever we return here is gonna send back to the user


@app.get("/get_posts")
def get_posts():
	return{"data": "this is the post"}

@app.post("/createposts")
def createposts(post: Post):
	print(post)
	print(post.dict())
	return {"data": post}