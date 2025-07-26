import React from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from './ui/card';
import { Button } from './ui/button';
import { Mail, Phone, MapPin, Linkedin, Github } from 'lucide-react';
import { portfolioData } from '../data/mock';

const Contact = () => {
  const { personal } = portfolioData;

  const contactInfo = [
    {
      icon: Mail,
      label: 'Email',
      value: personal.email,
      href: `mailto:${personal.email}`
    },
    {
      icon: Phone,
      label: 'Phone',
      value: personal.phone,
      href: `tel:${personal.phone}`
    },
    {
      icon: MapPin,
      label: 'Location',
      value: personal.location,
      href: null
    }
  ];

  const socialLinks = [
    {
      icon: Linkedin,
      label: 'LinkedIn',
      href: personal.linkedin,
      color: 'bg-blue-600 hover:bg-blue-700'
    },
    {
      icon: Github,
      label: 'GitHub',
      href: personal.github,
      color: 'bg-gray-800 hover:bg-gray-900'
    }
  ];

  return (
    <section id="contact" className="py-20 px-6">
      <div className="container mx-auto max-w-4xl">
        <div className="text-center mb-16">
          <h2 className="text-3xl md:text-4xl font-bold mb-4">Get In Touch</h2>
          <p className="text-xl text-muted-foreground">
            I'm always open to new opportunities, collaborations, or just tech talk!
          </p>
        </div>

        <div className="grid md:grid-cols-2 gap-8">
          <Card className="border-0 shadow-md">
            <CardHeader>
              <CardTitle className="text-xl">Contact Information</CardTitle>
              <CardDescription>
                Feel free to reach out through any of these channels
              </CardDescription>
            </CardHeader>
            <CardContent className="space-y-4">
              {contactInfo.map((info, index) => (
                <div key={index} className="flex items-center gap-3">
                  <div className="flex-shrink-0">
                    <info.icon className="h-5 w-5 text-muted-foreground" />
                  </div>
                  <div>
                    <p className="text-sm font-medium">{info.label}</p>
                    {info.href ? (
                      <a
                        href={info.href}
                        className="text-sm text-muted-foreground hover:text-primary transition-colors"
                      >
                        {info.value}
                      </a>
                    ) : (
                      <p className="text-sm text-muted-foreground">{info.value}</p>
                    )}
                  </div>
                </div>
              ))}
            </CardContent>
          </Card>

          <Card className="border-0 shadow-md">
            <CardHeader>
              <CardTitle className="text-xl">Connect With Me</CardTitle>
              <CardDescription>
                Follow my work and connect on social platforms
              </CardDescription>
            </CardHeader>
            <CardContent className="space-y-4">
              {socialLinks.map((social, index) => (
                <Button
                  key={index}
                  variant="outline"
                  className="w-full justify-start gap-3"
                  onClick={() => window.open(social.href, '_blank')}
                >
                  <social.icon className="h-5 w-5" />
                  {social.label}
                </Button>
              ))}
              
              <div className="pt-4 border-t">
                <Button
                  size="lg"
                  className="w-full bg-gradient-to-r from-blue-600 to-teal-600 hover:from-blue-700 hover:to-teal-700 text-white"
                  onClick={() => window.open(`mailto:${personal.email}`, '_blank')}
                >
                  <Mail className="mr-2 h-5 w-5" />
                  Send Email
                </Button>
              </div>
            </CardContent>
          </Card>
        </div>
      </div>
    </section>
  );
};

export default Contact;