import React from 'react';
import { usePersonalInfo } from '../hooks/usePortfolioData';

const Footer = () => {
  const { personalInfo } = usePersonalInfo();
  const currentYear = new Date().getFullYear();

  return (
    <footer className="bg-muted/50 py-8 px-6 border-t">
      <div className="container mx-auto max-w-6xl">
        <div className="text-center">
          <p className="text-muted-foreground">
            &copy; {currentYear} {personalInfo?.name || 'Portfolio'}. All rights reserved.
          </p>
          <p className="text-sm text-muted-foreground mt-2">
            Built with React, Tailwind CSS, and shadcn/ui
          </p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;