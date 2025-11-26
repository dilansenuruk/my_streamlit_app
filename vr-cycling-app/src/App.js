import React, { useState, useEffect } from 'react';
import './App.css';
import MapComponent from './components/MapComponent';
import InfoPanel from './components/InfoPanel';

function App() {
  const [devices, setDevices] = useState(null);
  const [pathData, setPathData] = useState([]);

  useEffect(() => {
    // Fetch path data once on mount
    fetch('http://localhost:5000/api/path')
      .then(res => res.json())
      .then(data => {
        setPathData(data.path);
      })
      .catch(err => console.error('Error fetching path:', err));

    // Poll device positions every 2 seconds
    const interval = setInterval(() => {
      fetch('http://localhost:5000/api/devices')
        .then(res => res.json())
        .then(data => {
          setDevices(data);
        })
        .catch(err => console.error('Error fetching devices:', err));
    }, 2000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="App">
      <div className="header">
        <h1>🚴 Get the VR Cycling Experience </h1>
        <p className="subtitle">Ride Freely on Nuwara Eliya Route</p>
      </div>
      
      <div className="main-container">
        <div className="left-panel">
          <InfoPanel />
        </div>
        
        <div className="right-panel">
          <div className="map-container">
            <MapComponent devices={devices} pathData={pathData} />
          </div>
          
          {/* Legend below the map */}
          <div className="map-legend">
            <div className="legend-items">
              <div className="legend-item">
                <div className="legend-color" style={{ backgroundColor: '#3498db' }}></div>
                <span className="legend-name">Colombo</span>
              </div>
              <div className="legend-item">
                <div className="legend-color" style={{ backgroundColor: '#e74c3c' }}></div>
                <span className="legend-name">Kandy</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
