import axios from 'axios';

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
const API_BASE = `${BACKEND_URL}/api`;

// Create axios instance with default config
const api = axios.create({
  baseURL: API_BASE,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor for logging
api.interceptors.request.use(
  (config) => {
    console.log(`API Request: ${config.method?.toUpperCase()} ${config.url}`);
    return config;
  },
  (error) => {
    console.error('API Request Error:', error);
    return Promise.reject(error);
  }
);

// Response interceptor for error handling
api.interceptors.response.use(
  (response) => {
    console.log(`API Response: ${response.status} ${response.config.url}`);
    return response;
  },
  (error) => {
    console.error('API Response Error:', error.response?.data || error.message);
    return Promise.reject(error);
  }
);

// Portfolio API service
export const portfolioService = {
  // Get complete portfolio data
  async getPortfolio() {
    try {
      const response = await api.get('/portfolio');
      return response.data;
    } catch (error) {
      console.error('Error fetching portfolio:', error);
      throw error;
    }
  },

  // Get personal information
  async getPersonalInfo() {
    try {
      const response = await api.get('/portfolio/personal');
      return response.data;
    } catch (error) {
      console.error('Error fetching personal info:', error);
      throw error;
    }
  },

  // Get projects with optional category filtering
  async getProjects(category = null) {
    try {
      const params = category && category !== 'All' ? { category } : {};
      const response = await api.get('/portfolio/projects', { params });
      return response.data;
    } catch (error) {
      console.error('Error fetching projects:', error);
      throw error;
    }
  },

  // Get work experience
  async getExperience() {
    try {
      const response = await api.get('/portfolio/experience');
      return response.data;
    } catch (error) {
      console.error('Error fetching experience:', error);
      throw error;
    }
  },

  // Submit contact message
  async submitContactMessage(messageData) {
    try {
      const response = await api.post('/portfolio/contact', messageData);
      return response.data;
    } catch (error) {
      console.error('Error submitting contact message:', error);
      throw error;
    }
  },

  // Get contact messages (admin only)
  async getContactMessages(limit = 50) {
    try {
      const response = await api.get('/portfolio/contact', { params: { limit } });
      return response.data;
    } catch (error) {
      console.error('Error fetching contact messages:', error);
      throw error;
    }
  }
};

// Health check
export const healthCheck = async () => {
  try {
    const response = await api.get('/health');
    return response.data;
  } catch (error) {
    console.error('Health check failed:', error);
    throw error;
  }
};

export default api;