from pydantic import BaseModel

class PlaceBody(BaseModel):
  formattedAddress: str
  price: str
  rating: float