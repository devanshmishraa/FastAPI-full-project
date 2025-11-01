from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/login") #this decorator turn this into an actual path operaion. / is the root path 
def get_user():
	return {"message": "Hello World!!!!"} 
	# What ever we return here is gonna send back to the user


@app.get("/get_posts")
def get_posts():
	return{"data": "this is the post"}

@app.post("/createposts")
def createposts(payload: dict = Body(...)):
	print(payload)
	return {"new post": f"title: {payload['title']}, content: {payload['content']}"}