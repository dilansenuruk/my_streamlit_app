import React from 'react';
import './InfoPanel.css';

function InfoPanel() {
  return (
    <div className="info-panel">
      <div className="info-section">
        {/* <h2 className="section-title">🌍 About VR Cycling</h2> */}
        <div className="info-card">
          {/* <h3>English</h3> */}
          <p>
            {/* This <b> VR cycling </b> dashboard allows you to track live location data and view 
            progress in real time. Monitor two devices as they traverse the beautiful 
            Nuwara Eliya route. */}
            <font size = "3"><b> VR Cycling </b> offers an immersive real-world riding experience, 
            allowing you to pedal freely through realistic 360° environments. 
            It effectively bridges the gap between virtual simulation and real-world cycling.</font>
          </p>
        </div>
        <div className="info-card">
          {/* <h3>සිංහල</h3> */}
          <p>
            <font size = "3"><b> VR cycling </b> ඔබට සජීවීකරණයකින් ඔබ්බට ගිය, 360° පරිසරයන් හරහා නිදහසේ සයිකල් පැදීමේ අත්දැකීමක් ලබා දෙයි. 
            මෙමගින් පරිගණක මගින් නිර්මාණය කරන ලද අනුකරණවල සහ ස්වභාවික ලෝකයේ සයිකල් පැදීම අතර ඇති පරතරය කාර්යක්ෂමව පුරවා දේ.</font>
          </p>
        </div>
        <div className="info-card">
          {/* <h3>தமிழ்</h3> */}
          <p>
            <font size = "3"><b> VR Cycling </b> </font> <font size = "2"> ஒரு அதிவேக நிஜ உலக சவாரி அனுபவத்தை வழங்குகிறது, 
            இது 360° சூழல்களில் சுதந்திரமாக சைக்கிள் ஓட்ட உங்களை அனுமதிக்கிறது. 
            இது மெய்நிகர் உருவகப்படுத்துதலுக்கும் நிஜ உலக சைக்கிள் ஓட்டுதலுக்கும் இடையிலான 
            இடைவெளியை திறம்பட இணைக்கிறது.</font>
          </p>
        </div>
      </div>
    </div>
  );
}

export default InfoPanel;
