// Navbar.js

import React from 'react';
import './navbar.css'; // Import the CSS file for styling
import home from './home.js';

function Navbar() {
  // Function to open Flask application
  function openFlaskApp() {
    window.open('http://localhost:5000', '_blank');
  }

  return (
    <div>
      {/* Original Navbar */}
      <nav className="navbar">
        <ul>
          <li><a href="/home">Home</a></li>
          <li><a href="/about">About</a></li>
          <li><a href="/contact">Contact</a></li>
        </ul>
      </nav>
      
      {/* Subnavbar */}
      <nav className="subnavbar">
        <ul>
          <li><a href="/prediction" onClick={openFlaskApp}>Prediction</a></li>
          <li><a href="/home">Analysis</a></li> {/* Set href to "/" */}
        </ul>
      </nav>
    </div>
  );
}

export default Navbar;
