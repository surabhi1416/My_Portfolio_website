import { useState, useEffect } from 'react';
import { portfolioService } from '../services/api';

export const usePortfolioData = () => {
  const [portfolio, setPortfolio] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchPortfolio = async () => {
      try {
        setLoading(true);
        setError(null);
        const data = await portfolioService.getPortfolio();
        setPortfolio(data);
      } catch (err) {
        setError(err.message || 'Failed to fetch portfolio data');
        console.error('Error fetching portfolio:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchPortfolio();
  }, []);

  return { portfolio, loading, error, refetch: () => fetchPortfolio() };
};

export const usePersonalInfo = () => {
  const [personalInfo, setPersonalInfo] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchPersonalInfo = async () => {
      try {
        setLoading(true);
        setError(null);
        const data = await portfolioService.getPersonalInfo();
        setPersonalInfo(data);
      } catch (err) {
        setError(err.message || 'Failed to fetch personal information');
        console.error('Error fetching personal info:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchPersonalInfo();
  }, []);

  return { personalInfo, loading, error };
};

export const useProjects = (category = null) => {
  const [projects, setProjects] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchProjects = async () => {
      try {
        setLoading(true);
        setError(null);
        const data = await portfolioService.getProjects(category);
        setProjects(data);
      } catch (err) {
        setError(err.message || 'Failed to fetch projects');
        console.error('Error fetching projects:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchProjects();
  }, [category]);

  return { projects, loading, error };
};

export const useExperience = () => {
  const [experience, setExperience] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchExperience = async () => {
      try {
        setLoading(true);
        setError(null);
        const data = await portfolioService.getExperience();
        setExperience(data);
      } catch (err) {
        setError(err.message || 'Failed to fetch experience');
        console.error('Error fetching experience:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchExperience();
  }, []);

  return { experience, loading, error };
};