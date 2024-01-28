from pydantic import BaseModel, conint

class CreateComment(BaseModel):
    show_id: int
    comment: str
    rating: conint(ge=0, le=5) = 0
