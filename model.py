from pydantic import BaseModel, Field
from typing import List, Optional

class CaloriesKcal(BaseModel):
    low: float
    high: float

class MacrosG(BaseModel):
    protein: float
    carbs: float
    fat: float

class Item(BaseModel):
    name: str
    type: str
    portion_size: str
    cooking_method: Optional[str] = None
    macros_g: MacrosG
    calories_kcal: CaloriesKcal
    assumptions: str

class TotalMacros(BaseModel):
    proteins: CaloriesKcal
    carbs: CaloriesKcal
    fat: CaloriesKcal

class GeminiVisionResponse(BaseModel):
    overview: str
    short_name: str
    items: List[Item]
    total_calories_kcal: CaloriesKcal
    total_macros: TotalMacros
    notes: str


