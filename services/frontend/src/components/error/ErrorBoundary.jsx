// services/frontend/src/components/error/ErrorBoundary.jsx
import React from 'react';
import { Box, Typography } from '@mui/material';

export default class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError() {
    return { hasError: true };
  }

  render() {
    if (this.state.hasError) {
      return (
        <Box p={2} bgcolor="error.main" color="white">
          <Typography variant="h6">
            Visualization Error
          </Typography>
          <Typography variant="body2">
            Failed to render molecular structure
          </Typography>
        </Box>
      );
    }
    return this.props.children;
  }
}