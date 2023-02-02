import base64
from fastapi import FastAPI, UploadFile, Response
from pydantic import BaseModel
from bson.objectid import ObjectId
from app.utils.database import get_db, get_posts_collection

app = FastAPI()
db = get_db()
video_posts = get_posts_collection()

class VideoPost(BaseModel):
    video: UploadFile
    description: str

@app.post("/posts")
async def add_video_post(video: UploadFile, description: str):
    video_bytes = await video.read()
    post = {"video": video_bytes, "description": description}
    result = video_posts.insert_one(post)
    return {"message": "Video post added successfully", "id": str(result.inserted_id)}

@app.get("/posts/{post_id}")
async def download_video_post(post_id: str):
    post = video_posts.find_one({"_id": ObjectId(post_id)})
    if not post:
        return {"message": "Video post not found"}, 404
    video = post["video"]
    response = Response(content=video, media_type="video/3gpp")
    response.headers["Content-Disposition"] = f'attachment; filename="video.3gp"'
    return response

@app.put("/posts/{post_id}")
async def update_video_post(post_id: str, video: UploadFile, description: str):
    video_bytes = await video.read()
    post = {"video": video_bytes, "description": description}
    result = video_posts.update_one({"_id": ObjectId(post_id)}, {"$set": post})
    if result.modified_count == 0:
        return {"message": "Video post not found"}, 404
    return {"message": "Video post updated successfully"}

@app.delete("/posts/{post_id}")
async def delete_video_post(post_id: str):
    result = video_posts.delete_one({"_id": ObjectId(post_id)})
    if result.deleted_count == 0:
        return {"message": "Video post not found"}, 404
    return {"message": "Video post deleted successfully"}
