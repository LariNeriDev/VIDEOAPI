from pydantic import BaseModel

class VideoPost(BaseModel):
    video: str
    description: str
