from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
import uuid

class PersonalInfo(BaseModel):
    name: str
    title: str
    subtitle: str
    email: str
    phone: str
    location: str
    linkedin: str
    github: str

class Project(BaseModel):
    id: int
    title: str
    description: str
    image: str
    github: str
    technologies: List[str]
    category: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Experience(BaseModel):
    id: int
    title: str
    company: str
    duration: str
    description: str
    technologies: List[str]
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Portfolio(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    personal: PersonalInfo
    projects: List[Project]
    experience: List[Experience]
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class ContactMessage(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    email: str
    message: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    read: bool = False

class ContactMessageCreate(BaseModel):
    name: str
    email: str
    message: str