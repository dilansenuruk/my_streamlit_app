import React, { useEffect, useRef } from 'react';
import { MapContainer, TileLayer, Polyline, CircleMarker, Popup, useMap } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import './MapComponent.css';

// Component to update marker positions smoothly
function DeviceMarkers({ devices }) {
  if (!devices) return null;

  return (
    <>
      {/* Device H (Blue) */}
      <CircleMarker
        center={devices.deviceH.position}
        radius={12}
        pathOptions={{
          color: '#3498db',
          fillColor: '#3498db',
          fillOpacity: 0.8,
          weight: 3
        }}
      >
        <Popup>
          <div className="popup-content">
            <strong>{devices.deviceH.name}</strong>
            <br />
            Position: {devices.deviceH.index}
            <br />
            Lat: {devices.deviceH.position[0].toFixed(6)}
            <br />
            Lon: {devices.deviceH.position[1].toFixed(6)}
          </div>
        </Popup>
      </CircleMarker>

      {/* Device G (Red) */}
      <CircleMarker
        center={devices.deviceG.position}
        radius={12}
        pathOptions={{
          color: '#e74c3c',
          fillColor: '#e74c3c',
          fillOpacity: 0.8,
          weight: 3
        }}
      >
        <Popup>
          <div className="popup-content">
            <strong>{devices.deviceG.name}</strong>
            <br />
            Position: {devices.deviceG.index}
            <br />
            Lat: {devices.deviceG.position[0].toFixed(6)}
            <br />
            Lon: {devices.deviceG.position[1].toFixed(6)}
          </div>
        </Popup>
      </CircleMarker>
    </>
  );
}

// Component to handle map centering
function MapController({ devices }) {
  const map = useMap();
  const initialCenterSet = useRef(false);

  useEffect(() => {
    if (devices && !initialCenterSet.current) {
      // Center map on initial device position
      const center = devices.deviceH.position;
      map.setView(center, 16);
      initialCenterSet.current = true;
    }
  }, [devices, map]);

  return null;
}

function MapComponent({ devices, pathData }) {
  const defaultCenter = [6.953399599775896, 80.78392973728708];
  const defaultZoom = 16;

  return (
    <div className="map-wrapper">
      <MapContainer
        center={defaultCenter}
        zoom={defaultZoom}
        style={{ height: '100%', width: '100%' }}
        zoomControl={true}
      >
        <TileLayer
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
        
        {/* Draw the path */}
        {pathData.length > 0 && (
          <Polyline
            positions={pathData}
            pathOptions={{
              color: '#2ecc71',
              weight: 4,
              opacity: 0.7
            }}
          />
        )}

        {/* Render device markers */}
        <DeviceMarkers devices={devices} />
        
        {/* Map controller */}
        <MapController devices={devices} />
      </MapContainer>
    </div>
  );
}

export default MapComponent;
