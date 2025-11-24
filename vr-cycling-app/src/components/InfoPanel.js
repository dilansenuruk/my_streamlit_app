import React from 'react';
import './InfoPanel.css';

function InfoPanel({ devices }) {
  return (
    <div className="info-panel">
      <div className="info-section">
        <h2 className="section-title">🌍 About VR Cycling</h2>
        <div className="info-card">
          <h3>English</h3>
          <p>
            This VR cycling dashboard allows you to track live MQTT data and view 
            progress in real time. Monitor two devices as they traverse the beautiful 
            Nuwara Eliya route.
          </p>
        </div>
        <div className="info-card">
          <h3>සිංහල</h3>
          <p>
            මෙම VR බයිසිකල් ඩැෂ්බෝර්ඩ් මගින් ඔබට සජීවී MQTT දත්ත නිරීක්ෂණය කළ හැක. 
            නුවරඑළිය මාර්ගය හරහා ගමන් කරන උපාංග දෙක නිරීක්ෂණය කරන්න.
          </p>
        </div>
        <div className="info-card">
          <h3>தமிழ்</h3>
          <p>
            இந்த VR சைக்கிளிங் டாஷ்போர்ட் வழியாக நேரடி MQTT தரவை கண்காணிக்க முடியும். 
            நுவரேலியா வழித்தடத்தில் பயணிக்கும் இரண்டு சாதனங்களை கண்காணிக்கவும்.
          </p>
        </div>
      </div>

      <div className="info-section device-status">
        <h2 className="section-title">📍 Device Status</h2>
        {devices ? (
          <>
            <div className="device-card device-h">
              <div className="device-header">
                <div className="device-icon" style={{ backgroundColor: '#3498db' }}></div>
                <h3>{devices.deviceH.name}</h3>
              </div>
              <div className="device-stats">
                <div className="stat">
                  <span className="stat-label">Position Index:</span>
                  <span className="stat-value">{devices.deviceH.index}</span>
                </div>
                <div className="stat">
                  <span className="stat-label">Latitude:</span>
                  <span className="stat-value">{devices.deviceH.position[0].toFixed(6)}</span>
                </div>
                <div className="stat">
                  <span className="stat-label">Longitude:</span>
                  <span className="stat-value">{devices.deviceH.position[1].toFixed(6)}</span>
                </div>
              </div>
              <div className="progress-bar">
                <div 
                  className="progress-fill" 
                  style={{ 
                    width: `${(devices.deviceH.index / 300) * 100}%`,
                    backgroundColor: '#3498db'
                  }}
                ></div>
              </div>
            </div>

            <div className="device-card device-g">
              <div className="device-header">
                <div className="device-icon" style={{ backgroundColor: '#e74c3c' }}></div>
                <h3>{devices.deviceG.name}</h3>
              </div>
              <div className="device-stats">
                <div className="stat">
                  <span className="stat-label">Position Index:</span>
                  <span className="stat-value">{devices.deviceG.index}</span>
                </div>
                <div className="stat">
                  <span className="stat-label">Latitude:</span>
                  <span className="stat-value">{devices.deviceG.position[0].toFixed(6)}</span>
                </div>
                <div className="stat">
                  <span className="stat-label">Longitude:</span>
                  <span className="stat-value">{devices.deviceG.position[1].toFixed(6)}</span>
                </div>
              </div>
              <div className="progress-bar">
                <div 
                  className="progress-fill" 
                  style={{ 
                    width: `${(devices.deviceG.index / 300) * 100}%`,
                    backgroundColor: '#e74c3c'
                  }}
                ></div>
              </div>
            </div>
          </>
        ) : (
          <div className="loading">Loading device data...</div>
        )}
      </div>
    </div>
  );
}

export default InfoPanel;
