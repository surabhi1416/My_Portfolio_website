from fastapi import APIRouter, HTTPException, Depends, Query
from typing import List, Optional
from models.portfolio import Portfolio, Project, Experience, ContactMessage, ContactMessageCreate
from services.portfolio_service import PortfolioService
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/portfolio", tags=["portfolio"])

# Database dependency
async def get_portfolio_service():
    mongo_url = os.environ['MONGO_URL']
    client = AsyncIOMotorClient(mongo_url)
    db = client[os.environ['DB_NAME']]
    return PortfolioService(db)

@router.get("/", response_model=Portfolio)
async def get_portfolio(service: PortfolioService = Depends(get_portfolio_service)):
    """Get complete portfolio data"""
    try:
        portfolio = await service.get_portfolio()
        if not portfolio:
            # Initialize with seed data if no portfolio exists
            portfolio = await service.initialize_portfolio()
        return portfolio
    except Exception as e:
        logger.error(f"Error in get_portfolio: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/personal")
async def get_personal_info(service: PortfolioService = Depends(get_portfolio_service)):
    """Get personal information"""
    try:
        personal_info = await service.get_personal_info()
        if not personal_info:
            raise HTTPException(status_code=404, detail="Personal information not found")
        return personal_info
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error in get_personal_info: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/projects", response_model=List[Project])
async def get_projects(
    category: Optional[str] = Query(None, description="Filter projects by category"),
    service: PortfolioService = Depends(get_portfolio_service)
):
    """Get projects with optional category filtering"""
    try:
        projects = await service.get_projects(category)
        return projects
    except Exception as e:
        logger.error(f"Error in get_projects: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/experience", response_model=List[Experience])
async def get_experience(service: PortfolioService = Depends(get_portfolio_service)):
    """Get work experience"""
    try:
        experience = await service.get_experience()
        return experience
    except Exception as e:
        logger.error(f"Error in get_experience: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.post("/contact", response_model=ContactMessage)
async def create_contact_message(
    message_data: ContactMessageCreate,
    service: PortfolioService = Depends(get_portfolio_service)
):
    """Create a new contact message"""
    try:
        contact_message = await service.create_contact_message(message_data)
        return contact_message
    except Exception as e:
        logger.error(f"Error in create_contact_message: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/contact", response_model=List[ContactMessage])
async def get_contact_messages(
    limit: int = Query(50, ge=1, le=100, description="Limit number of messages"),
    service: PortfolioService = Depends(get_portfolio_service)
):
    """Get contact messages (admin only in production)"""
    try:
        messages = await service.get_contact_messages(limit)
        return messages
    except Exception as e:
        logger.error(f"Error in get_contact_messages: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")