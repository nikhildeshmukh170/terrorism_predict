import React from 'react';
import './home.css';

const Home = () => {
  return (
    <div className="home-container">
      <h1>Welcome to the Home Page</h1>
      <p>Explore insights with our interactive dashboard.</p>

      <div className="iframe-container">
        <iframe 
          title="hackskill" 
          width="100%" 
          height="100%" 
          src="https://app.powerbi.com/view?r=eyJrIjoiYmQ0OThlNzAtNTQ5OS00MzQ2LWExY2UtOGFhZGZkNDI1YTdkIiwidCI6ImRmODY3OWNkLWE4MGUtNDVkOC05OWFjLWM4M2VkN2ZmOTVhMCJ9" 
          frameBorder="0" 
          allowFullScreen
        ></iframe>
      </div>
    </div>
  );
};

export default Home;
