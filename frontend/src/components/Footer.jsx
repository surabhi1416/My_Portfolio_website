import React from 'react';
import { portfolioData } from '../data/mock';

const Footer = () => {
  const { personal } = portfolioData;
  const currentYear = new Date().getFullYear();

  return (
    <footer className="bg-muted/50 py-8 px-6 border-t">
      <div className="container mx-auto max-w-6xl">
        <div className="text-center">
          <p className="text-muted-foreground">
            &copy; {currentYear} {personal.name}. All rights reserved.
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