import React, { useState } from 'react';
import axios from 'axios';
import './styles/App.css';
import AverageDisplay from './components/AverageDisplay';

function App() {
  const [averageData, setAverageData] = useState(null);
  const [inputId, setInputId] = useState('');

  const handleInputChange = (event) => {
    setInputId(event.target.value);
  };

  const fetchData = async () => {
    try {
      const response = await axios.get(`http://localhost:9876/numbers/${inputId}`);
      // rest of your code
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };
  

  return (
    <div className="app-container">
      <h1>Average Calculator App</h1>
      <div>
        <label htmlFor="numberId">Enter Number ID (p, f, e, r):</label>
        <input 
          type="text" 
          id="numberId" 
          value={inputId} 
          onChange={handleInputChange} 
        />
        <button onClick={fetchData}>Fetch Average</button>
      </div>
      {averageData && <AverageDisplay data={averageData} />}
    </div>
  );
}

export default App;
