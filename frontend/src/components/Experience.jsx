import React from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from './ui/card';
import { Badge } from './ui/badge';
import { Building, Calendar } from 'lucide-react';
import { useExperience } from '../hooks/usePortfolioData';
import LoadingSpinner from './LoadingSpinner';
import ErrorMessage from './ErrorMessage';

const Experience = () => {
  const { experience, loading, error } = useExperience();

  if (loading) {
    return (
      <section id="experience" className="py-20 px-6 bg-muted/50">
        <div className="container mx-auto max-w-4xl">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold mb-4">Work Experience</h2>
            <p className="text-xl text-muted-foreground">
              Professional internships and hands-on experience in data science and AI
            </p>
          </div>
          <div className="flex justify-center">
            <LoadingSpinner size="lg" />
          </div>
        </div>
      </section>
    );
  }

  if (error) {
    return (
      <section id="experience" className="py-20 px-6 bg-muted/50">
        <div className="container mx-auto max-w-4xl">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold mb-4">Work Experience</h2>
            <p className="text-xl text-muted-foreground">
              Professional internships and hands-on experience in data science and AI
            </p>
          </div>
          <ErrorMessage error={error} />
        </div>
      </section>
    );
  }

  return (
    <section id="experience" className="py-20 px-6 bg-muted/50">
      <div className="container mx-auto max-w-4xl">
        <div className="text-center mb-16">
          <h2 className="text-3xl md:text-4xl font-bold mb-4">Work Experience</h2>
          <p className="text-xl text-muted-foreground">
            Professional internships and hands-on experience in data science and AI
          </p>
        </div>

        <div className="space-y-8">
          {experience.map((exp, index) => (
            <Card key={exp.id} className="border-0 shadow-md hover:shadow-lg transition-all duration-300">
              <CardHeader>
                <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
                  <div>
                    <CardTitle className="text-xl mb-2">{exp.title}</CardTitle>
                    <div className="flex items-center gap-2 text-muted-foreground">
                      <Building className="h-4 w-4" />
                      <span className="font-medium">{exp.company}</span>
                    </div>
                  </div>
                  <div className="flex items-center gap-2 text-sm text-muted-foreground">
                    <Calendar className="h-4 w-4" />
                    <span>{exp.duration}</span>
                  </div>
                </div>
              </CardHeader>
              <CardContent>
                <CardDescription className="text-base mb-4">
                  {exp.description}
                </CardDescription>
                <div className="flex flex-wrap gap-1">
                  {exp.technologies.map((tech, techIndex) => (
                    <Badge key={techIndex} variant="outline" className="text-xs">
                      {tech}
                    </Badge>
                  ))}
                </div>
              </CardContent>
            </Card>
          ))}
        </div>

        {experience.length === 0 && (
          <div className="text-center py-12">
            <p className="text-muted-foreground text-lg">
              No work experience available.
            </p>
          </div>
        )}
      </div>
    </section>
  );
};

export default Experience;