import React, { useState } from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from './ui/card';
import { Badge } from './ui/badge';
import { Button } from './ui/button';
import { ExternalLink, Github, Filter } from 'lucide-react';
import { useProjects } from '../hooks/usePortfolioData';
import LoadingSpinner from './LoadingSpinner';
import ErrorMessage from './ErrorMessage';

const Projects = () => {
  const [selectedCategory, setSelectedCategory] = useState('All');
  const { projects, loading, error } = useProjects(selectedCategory === 'All' ? null : selectedCategory);
  
  const categories = ['All', 'Data Analytics', 'Machine Learning'];

  if (loading) {
    return (
      <section id="projects" className="py-20 px-6">
        <div className="container mx-auto max-w-6xl">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold mb-4">Featured Projects</h2>
            <p className="text-xl text-muted-foreground max-w-2xl mx-auto">
              A showcase of my work in data science, analytics, and machine learning
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
      <section id="projects" className="py-20 px-6">
        <div className="container mx-auto max-w-6xl">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold mb-4">Featured Projects</h2>
            <p className="text-xl text-muted-foreground max-w-2xl mx-auto">
              A showcase of my work in data science, analytics, and machine learning
            </p>
          </div>
          <ErrorMessage error={error} />
        </div>
      </section>
    );
  }

  return (
    <section id="projects" className="py-20 px-6">
      <div className="container mx-auto max-w-6xl">
        <div className="text-center mb-16">
          <h2 className="text-3xl md:text-4xl font-bold mb-4">Featured Projects</h2>
          <p className="text-xl text-muted-foreground max-w-2xl mx-auto">
            A showcase of my work in data science, analytics, and machine learning
          </p>
        </div>

        <div className="flex flex-wrap justify-center gap-2 mb-12">
          {categories.map((category) => (
            <Button
              key={category}
              variant={selectedCategory === category ? "default" : "outline"}
              onClick={() => setSelectedCategory(category)}
              className="mb-2"
            >
              <Filter className="mr-2 h-4 w-4" />
              {category}
            </Button>
          ))}
        </div>

        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          {projects.map((project) => (
            <Card key={project.id} className="group hover:shadow-lg transition-all duration-300 border-0 shadow-md">
              <div className="aspect-video overflow-hidden rounded-t-lg">
                <img
                  src={project.image}
                  alt={project.title}
                  className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
                />
              </div>
              <CardHeader>
                <div className="flex justify-between items-start">
                  <div>
                    <CardTitle className="text-xl mb-2">{project.title}</CardTitle>
                    <Badge variant="secondary" className="mb-2">
                      {project.category}
                    </Badge>
                  </div>
                </div>
                <CardDescription className="text-base">
                  {project.description}
                </CardDescription>
              </CardHeader>
              <CardContent>
                <div className="flex flex-wrap gap-1 mb-4">
                  {project.technologies.map((tech, index) => (
                    <Badge key={index} variant="outline" className="text-xs">
                      {tech}
                    </Badge>
                  ))}
                </div>
                <div className="flex gap-2">
                  <Button
                    size="sm"
                    variant="outline"
                    onClick={() => window.open(project.github, '_blank')}
                    className="flex-1"
                  >
                    <Github className="mr-2 h-4 w-4" />
                    Code
                  </Button>
                  <Button
                    size="sm"
                    onClick={() => window.open(project.github, '_blank')}
                    className="flex-1"
                  >
                    <ExternalLink className="mr-2 h-4 w-4" />
                    View
                  </Button>
                </div>
              </CardContent>
            </Card>
          ))}
        </div>

        {projects.length === 0 && (
          <div className="text-center py-12">
            <p className="text-muted-foreground text-lg">
              No projects found for the selected category.
            </p>
          </div>
        )}
      </div>
    </section>
  );
};

export default Projects;