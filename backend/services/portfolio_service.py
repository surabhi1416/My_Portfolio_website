from motor.motor_asyncio import AsyncIOMotorClient
from models.portfolio import Portfolio, Project, Experience, ContactMessage, ContactMessageCreate
from database.seed_data import get_portfolio_seed_data
from typing import List, Optional
import logging

logger = logging.getLogger(__name__)

class PortfolioService:
    def __init__(self, db):
        self.db = db
        self.portfolio_collection = db.portfolio
        self.contact_collection = db.contact_messages

    async def initialize_portfolio(self):
        """Initialize portfolio with seed data if not exists"""
        try:
            existing_portfolio = await self.portfolio_collection.find_one()
            if not existing_portfolio:
                seed_data = get_portfolio_seed_data()
                await self.portfolio_collection.insert_one(seed_data.dict())
                logger.info("Portfolio initialized with seed data")
                return seed_data
            return Portfolio(**existing_portfolio)
        except Exception as e:
            logger.error(f"Error initializing portfolio: {e}")
            raise

    async def get_portfolio(self) -> Optional[Portfolio]:
        """Get complete portfolio data"""
        try:
            portfolio_data = await self.portfolio_collection.find_one()
            if portfolio_data:
                return Portfolio(**portfolio_data)
            return None
        except Exception as e:
            logger.error(f"Error getting portfolio: {e}")
            raise

    async def get_personal_info(self) -> Optional[dict]:
        """Get personal information only"""
        try:
            portfolio = await self.get_portfolio()
            if portfolio:
                return portfolio.personal.dict()
            return None
        except Exception as e:
            logger.error(f"Error getting personal info: {e}")
            raise

    async def get_projects(self, category: Optional[str] = None) -> List[Project]:
        """Get projects with optional category filtering"""
        try:
            portfolio = await self.get_portfolio()
            if not portfolio:
                return []
            
            projects = portfolio.projects
            if category and category.lower() != "all":
                projects = [p for p in projects if p.category.lower() == category.lower()]
            
            return projects
        except Exception as e:
            logger.error(f"Error getting projects: {e}")
            raise

    async def get_experience(self) -> List[Experience]:
        """Get work experience"""
        try:
            portfolio = await self.get_portfolio()
            if portfolio:
                return portfolio.experience
            return []
        except Exception as e:
            logger.error(f"Error getting experience: {e}")
            raise

    async def create_contact_message(self, message_data: ContactMessageCreate) -> ContactMessage:
        """Create a new contact message"""
        try:
            contact_message = ContactMessage(**message_data.dict())
            await self.contact_collection.insert_one(contact_message.dict())
            logger.info(f"New contact message from {message_data.email}")
            return contact_message
        except Exception as e:
            logger.error(f"Error creating contact message: {e}")
            raise

    async def get_contact_messages(self, limit: int = 50) -> List[ContactMessage]:
        """Get contact messages"""
        try:
            messages = await self.contact_collection.find().sort("created_at", -1).limit(limit).to_list(limit)
            return [ContactMessage(**msg) for msg in messages]
        except Exception as e:
            logger.error(f"Error getting contact messages: {e}")
            raise

    async def update_portfolio(self, portfolio_data: Portfolio) -> Portfolio:
        """Update portfolio data"""
        try:
            await self.portfolio_collection.replace_one(
                {"id": portfolio_data.id},
                portfolio_data.dict(),
                upsert=True
            )
            logger.info("Portfolio updated successfully")
            return portfolio_data
        except Exception as e:
            logger.error(f"Error updating portfolio: {e}")
            raise