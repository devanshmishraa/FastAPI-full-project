from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

class Post(BaseModel):
	title: str
	content: str
	published: bool = True
	rating: Optional[int] = None


my_posts = [
  {"title": "Introduction to FinTech", "content": "Overview of FinTech innovations and applications.", "id": 1},
  {"title": "AI in Finance", "content": "How AI is transforming financial decision-making.", "id": 2},
  {"title": "Understanding Blockchain", "content": "A beginner's guide to blockchain technology.", "id": 3},
  {"title": "Digital Payments Trends", "content": "Latest trends in digital and contactless payments.", "id": 4},
  {"title": "Risk Management Strategies", "content": "Methods for managing financial and operational risks.", "id": 5},
  {"title": "Customer Analytics", "content": "Using data to understand customer behavior.", "id": 6},
  {"title": "Investment Strategies", "content": "Different approaches to investing in markets.", "id": 7},
  {"title": "Cybersecurity in Finance", "content": "Protecting financial data from cyber threats.", "id": 8},
  {"title": "Regulatory Compliance", "content": "Understanding financial regulations and compliance.", "id": 9},
  {"title": "Future of Banking", "content": "How technology is shaping the future of banking.", "id": 10}
]

def find_post(id):
	for p in my_posts:
		if p["id"]==id:
			return p
		
def remove_post(id):
	for i, post in enumerate(my_posts):
		if post["id"]==id:
			removed_post = my_posts.pop(i)
			return removed_post
	return None

@app.get("/login") #this decorator turn this into an actual path operaion. / is the root path 
def get_user():
	return {"message": "Hello World!!!!"} 
	# What ever we return here is gonna send back to the user


@app.get("/get_posts")
def get_posts():
	return{"data": my_posts}

@app.post("/createposts", status_code=status.HTTP_201_CREATED)
def createposts(post: Post):
	post_dict = post.dict()
	post_dict['id'] = randrange(0,100000)
	my_posts.append(post_dict)
	return {"data": post_dict}


@app.get("/posts/latest")
def get_latest_post():
	if not my_posts:
		return {"error":"No posts found"}
	post = my_posts[-1]
	return {"latest_post": post}



@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int ):
	post = remove_post(id)
	if not post:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with the id {id} not found")
	return Response(status_code=status.HTTP_204_NO_CONTENT)
	



@app.get("/posts/{id}")
def get_post(id:int):
	post = find_post(id)
	if not post:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"post with id {id} not found")
		# response.status_code = status.HTTP_404_NOT_FOUND
		# return {"message": f"post with id {id} not found"}

	print(type(id))
	return {"post_detail": post}

			