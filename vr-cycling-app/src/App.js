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
        <h1>🚴 VR Cycling — Live Tracking Dashboard</h1>
        <p className="subtitle">Real-time Device Tracking on Nuwara Eliya Route</p>
      </div>
      
      <div className="main-container">
        <div className="left-panel">
          <InfoPanel devices={devices} />
        </div>
        
        <div className="map-container">
          <MapComponent devices={devices} pathData={pathData} />
        </div>
      </div>
    </div>
  );
}

export default App;
