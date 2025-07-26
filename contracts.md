# Portfolio Website Backend API Contracts

## Overview
This document outlines the API contracts for Surabhi Pilane's portfolio website backend integration.

## Current Mock Data (frontend/src/data/mock.js)
- **Personal Information**: Name, title, contact details, social links
- **Projects**: 5 projects with images, descriptions, GitHub links, technologies
- **Experience**: 2 internship experiences with company details and descriptions

## Backend API Endpoints

### 1. Portfolio Data Management

#### GET /api/portfolio
- **Purpose**: Retrieve all portfolio data
- **Response**: Complete portfolio object with personal info, projects, and experience
- **Mock Data**: Currently using `portfolioData` from mock.js

#### GET /api/portfolio/personal
- **Purpose**: Get personal information
- **Response**: Personal details, contact info, social links

#### GET /api/portfolio/projects
- **Purpose**: Get all projects with optional category filtering
- **Query Parameters**: `category` (optional) - filter by "Data Analytics" or "Machine Learning"
- **Response**: Array of project objects with images, descriptions, technologies

#### GET /api/portfolio/experience
- **Purpose**: Get work experience
- **Response**: Array of experience objects with company, duration, descriptions

### 2. Contact Form (Future Enhancement)

#### POST /api/contact
- **Purpose**: Handle contact form submissions
- **Request Body**: `{ name, email, message }`
- **Response**: Success/error message

### 3. Analytics (Future Enhancement)

#### GET /api/analytics/views
- **Purpose**: Track portfolio views
- **Response**: View count and basic analytics

## Database Schema

### Portfolio Collection
```javascript
{
  _id: ObjectId,
  personal: {
    name: String,
    title: String,
    subtitle: String,
    email: String,
    phone: String,
    location: String,
    linkedin: String,
    github: String
  },
  projects: [{
    id: Number,
    title: String,
    description: String,
    image: String,
    github: String,
    technologies: [String],
    category: String,
    createdAt: Date
  }],
  experience: [{
    id: Number,
    title: String,
    company: String,
    duration: String,
    description: String,
    technologies: [String],
    createdAt: Date
  }],
  updatedAt: Date
}
```

### Contact Messages Collection (Future)
```javascript
{
  _id: ObjectId,
  name: String,
  email: String,
  message: String,
  createdAt: Date,
  read: Boolean
}
```

## Frontend Integration Points

### Current Mock Usage
- `portfolioData` object in `/frontend/src/data/mock.js`
- Used in Hero, Projects, Experience, and Contact components

### Integration Steps
1. Replace mock data imports with API calls
2. Add loading states and error handling
3. Implement data fetching hooks
4. Update components to use API responses

### Component Updates Required
- **Hero.jsx**: Replace `portfolioData.personal` with API call
- **Projects.jsx**: Replace `portfolioData.projects` with API call + filtering
- **Experience.jsx**: Replace `portfolioData.experience` with API call
- **Contact.jsx**: Replace `portfolioData.personal` with API call

## Error Handling
- Loading states for all API calls
- Fallback to cached data if API fails
- User-friendly error messages
- Retry mechanisms for failed requests

## Performance Considerations
- Cache portfolio data in localStorage
- Implement data revalidation strategies
- Optimize image loading for project cards
- Add pagination for future scalability

## Security Considerations
- Input validation for contact forms
- Rate limiting for API endpoints
- CORS configuration for frontend domain
- Sanitize user inputs to prevent XSS

## Future Enhancements
- Admin panel for content management
- Blog/articles section
- Project filtering by technology
- Contact form with email notifications
- Analytics dashboard
- SEO optimization with dynamic meta tags