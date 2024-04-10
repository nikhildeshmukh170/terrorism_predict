// src/App.js

import React, { useState, useEffect } from 'react';
import './App.css'; // Import CSS file for styling if needed
import Navbar from './navbar';

function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await fetch('/api/data'); // Make API call to Flask backend
      const jsonData = await response.json();
      setData(jsonData);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  return (
    <div className="App">
      <Navbar />
      <header className="App-header">
        {/* <h1>{data ? data.message : 'Loading...'}</h1>  */}
        <iframe title="GLOBAL TERRORISM ANALYSIS" width="1200" height="573.5" src="https://app.powerbi.com/view?r=eyJrIjoiMmM2NWU2NzctYzBmMi00ODE4LTg1MWYtYTg0M2M4OWQ4ZWZhIiwidCI6ImRmODY3OWNkLWE4MGUtNDVkOC05OWFjLWM4M2VkN2ZmOTVhMCJ9" frameborder="0" allowFullScreen="true"></iframe>
      </header>
    </div>
  );
}

export default App;
