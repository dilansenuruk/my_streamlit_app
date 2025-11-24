const express = require('express');
const cors = require('cors');
const mqtt = require('mqtt');
const fs = require('fs');
const csv = require('csv-parser');
const path = require('path');

const app = express();
app.use(cors());
app.use(express.json());

// MQTT Configuration
const BROKER = 'mqtt://18.140.19.253:8090';
const USERNAME = 'bikeuser';
const PASSWORD = 'DYuKE42w8CoSDyb0HN46Blkk9XSfY8Z9zes6Ek6eA';
const TOPICS = ['VRcycling/UserA/HIncTime', 'VRcycling/UserA/GIncTime'];

// Store device positions
let devicePositions = {
  HIncTime: 0,
  GIncTime: 0
};

// Store path coordinates
let pathCoords = [];

// Load CSV path data
const csvPath = path.join(__dirname, '../../interpolated_path.csv');
fs.createReadStream(csvPath)
  .pipe(csv())
  .on('data', (row) => {
    pathCoords.push([parseFloat(row.latitude), parseFloat(row.longitude)]);
  })
  .on('end', () => {
    console.log(`Loaded ${pathCoords.length} path coordinates`);
  });

// Connect to MQTT
const client = mqtt.connect(BROKER, {
  username: USERNAME,
  password: PASSWORD
});

client.on('connect', () => {
  console.log('Connected to MQTT broker');
  TOPICS.forEach(topic => {
    client.subscribe(topic, (err) => {
      if (err) {
        console.error(`Failed to subscribe to ${topic}:`, err);
      } else {
        console.log(`Subscribed to ${topic}`);
      }
    });
  });
});

client.on('message', (topic, message) => {
  const payload = message.toString();
  try {
    const value = parseInt(payload);
    const clampedValue = Math.max(0, Math.min(301, value));
    
    if (topic.endsWith('HIncTime')) {
      devicePositions.HIncTime = clampedValue;
    } else if (topic.endsWith('GIncTime')) {
      devicePositions.GIncTime = clampedValue;
    }
    
    console.log(`Updated ${topic}: ${clampedValue}`);
  } catch (error) {
    console.error('Error parsing message:', error);
  }
});

client.on('error', (error) => {
  console.error('MQTT connection error:', error);
});

// API Endpoints
app.get('/api/path', (req, res) => {
  res.json({ path: pathCoords });
});

app.get('/api/devices', (req, res) => {
  const h_idx = Math.max(0, Math.min(devicePositions.HIncTime, pathCoords.length - 1));
  const g_idx = Math.max(0, Math.min(devicePositions.GIncTime, pathCoords.length - 1));
  
  const devices = {
    deviceH: {
      position: pathCoords[h_idx] || [6.953399599775896, 80.78392973728708],
      index: devicePositions.HIncTime,
      color: 'blue',
      name: 'Device H'
    },
    deviceG: {
      position: pathCoords[g_idx] || [6.953399599775896, 80.78392973728708],
      index: devicePositions.GIncTime,
      color: 'red',
      name: 'Device G'
    }
  };
  
  res.json(devices);
});

const PORT = 5000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
