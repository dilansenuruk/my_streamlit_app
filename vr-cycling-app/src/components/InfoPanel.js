import React from 'react';
import './InfoPanel.css';

function InfoPanel() {
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
    </div>
  );
}

export default InfoPanel;
