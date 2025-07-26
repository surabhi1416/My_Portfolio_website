import React from 'react';
import { Alert, AlertDescription } from './ui/alert';
import { Button } from './ui/button';
import { RefreshCw } from 'lucide-react';

const ErrorMessage = ({ error, onRetry, className = '' }) => {
  return (
    <Alert className={`border-destructive ${className}`}>
      <AlertDescription className="flex items-center justify-between">
        <span className="text-destructive">
          {error || 'Something went wrong. Please try again.'}
        </span>
        {onRetry && (
          <Button
            variant="outline"
            size="sm"
            onClick={onRetry}
            className="ml-4"
          >
            <RefreshCw className="h-4 w-4 mr-2" />
            Retry
          </Button>
        )}
      </AlertDescription>
    </Alert>
  );
};

export default ErrorMessage;