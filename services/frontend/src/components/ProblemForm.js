import React, { useState } from 'react';
import { TextField, Button } from '@mui/material';

export default function ProblemForm({ onSubmit }) {
  const [variables, setVariables] = useState('');
  
  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({
      type: 'tsp',
      distance_matrix: JSON.parse(variables)
    });
  };

  return (
    <form onSubmit={handleSubmit}>
      <TextField
        label="Distance Matrix"
        multiline
        rows={4}
        value={variables}
        onChange={(e) => setVariables(e.target.value)}
        variant="outlined"
      />
      <Button type="submit" variant="contained">
        Submit
      </Button>
    </form>
  );
}