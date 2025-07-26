import React from 'react';
import { Button } from './ui/button';
import { Badge } from './ui/badge';
import { Github, Linkedin, Mail, MapPin } from 'lucide-react';
import { usePersonalInfo } from '../hooks/usePortfolioData';
import LoadingSpinner from './LoadingSpinner';
import ErrorMessage from './ErrorMessage';

const Hero = () => {
  const { personalInfo, loading, error } = usePersonalInfo();

  if (loading) {
    return (
      <section id="about" className="min-h-screen flex items-center justify-center py-20 px-6">
        <LoadingSpinner size="xl" />
      </section>
    );
  }

  if (error) {
    return (
      <section id="about" className="min-h-screen flex items-center justify-center py-20 px-6">
        <div className="max-w-md">
          <ErrorMessage error={error} />
        </div>
      </section>
    );
  }

  if (!personalInfo) {
    return (
      <section id="about" className="min-h-screen flex items-center justify-center py-20 px-6">
        <div className="max-w-md">
          <ErrorMessage error="Personal information not available" />
        </div>
      </section>
    );
  }

  return (
    <section id="about" className="min-h-screen flex items-center justify-center py-20 px-6">
      <div className="container mx-auto max-w-4xl text-center">
        <div className="space-y-8">
          <div className="space-y-4">
            <Badge variant="outline" className="text-sm px-4 py-2">
              👩‍💻 Available for opportunities
            </Badge>
            <h1 className="text-4xl md:text-6xl font-bold tracking-tight">
              {personalInfo.name}
            </h1>
            <h2 className="text-xl md:text-2xl text-muted-foreground font-medium">
              {personalInfo.title}
            </h2>
            <p className="text-lg md:text-xl text-muted-foreground max-w-3xl mx-auto leading-relaxed">
              {personalInfo.subtitle}
            </p>
          </div>

          <div className="flex flex-col sm:flex-row gap-4 justify-center items-center">
            <Button 
              size="lg" 
              className="bg-gradient-to-r from-blue-600 to-teal-600 hover:from-blue-700 hover:to-teal-700 text-white"
              onClick={() => window.open(personalInfo.linkedin, '_blank')}
            >
              <Linkedin className="mr-2 h-5 w-5" />
              LinkedIn
            </Button>
            <Button 
              size="lg" 
              variant="outline"
              onClick={() => window.open(personalInfo.github, '_blank')}
            >
              <Github className="mr-2 h-5 w-5" />
              GitHub
            </Button>
            <Button 
              size="lg" 
              variant="outline"
              onClick={() => window.open(`mailto:${personalInfo.email}`, '_blank')}
            >
              <Mail className="mr-2 h-5 w-5" />
              Email
            </Button>
          </div>

          <div className="flex justify-center items-center gap-2 text-sm text-muted-foreground">
            <MapPin className="h-4 w-4" />
            <span>{personalInfo.location}</span>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Hero;