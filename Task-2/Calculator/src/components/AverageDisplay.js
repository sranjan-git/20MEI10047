import React from 'react';
import './AverageDisplay.css';

const AverageDisplay = ({ data }) => {
  return (
    <div className="average-display">
      <h2>Previous Window State: {data.windowPrevState.join(', ')}</h2>
      <h2>Current Window State: {data.windowCurrState.join(', ')}</h2>
      <h2>Numbers: {data.numbers.join(', ')}</h2>
      <h2>Average: {data.avg}</h2>
    </div>
  );
};

export default AverageDisplay;
