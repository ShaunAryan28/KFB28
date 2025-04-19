import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import { Buffer } from 'buffer';

window.Buffer = Buffer;


if (!globalThis.Buffer) globalThis.Buffer = Buffer;

if (!globalThis.crypto?.getRandomValues) {
  const { webcrypto } = require('crypto');
  globalThis.crypto = webcrypto;
}
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/firebase-messaging-sw.js')
    .then(reg => console.log('Service Worker Registered'))
    .catch(err => console.error('SW registration failed:', err));
}

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
