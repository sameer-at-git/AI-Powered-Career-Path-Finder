from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uvicorn

# Database configuration
DATABASE_URL = "mysql+pymysql://username:password@localhost/career_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define a sample model for logging user requests
class UserProfile(Base):
    __tablename__ = "user_profiles"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    skills = Column(Text)
    experience = Column(Integer)

Base.metadata.create_all(bind=engine)

# FastAPI app instance
app = FastAPI(title="AI Career Path Definer API")

# Request and response models
class CareerRequest(BaseModel):
    name: str
    skills: str
    experience: int

class CareerResponse(BaseModel):
    recommendation: str

# Dummy recommendation function (replace with actual ML model integration)
def get_career_recommendation(profile: CareerRequest) -> str:
    # A placeholder logic using skills and experience.
    skills_list = [skill.strip().lower() for skill in profile.skills.split(',')]
    if "python" in skills_list and profile.experience < 2:
        return "Consider pursuing roles in Data Analysis or Machine Learning Internships."
    elif "javascript" in skills_list:
        return "Front-End Web Development might be a great fit for you."
    else:
        return "Explore opportunities in emerging tech fields to find your niche."

@app.post("/api/career-recommendation", response_model=CareerResponse)
def career_recommendation(request: CareerRequest):
    # Save profile data to database
    db = SessionLocal()
    try:
        user_profile = UserProfile(name=request.name, skills=request.skills, experience=request.experience)
        db.add(user_profile)
        db.commit()
        db.refresh(user_profile)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database Error")
    finally:
        db.close()

    # Get recommendation from our dummy function
    recommendation = get_career_recommendation(request)
    return CareerResponse(recommendation=recommendation)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
