// public/firebase-messaging-sw.js
'use client';
//importScripts("https://www.gstatic.com/firebasejs/9.22.2/firebase-app.js");
importScripts("https://www.gstatic.com/firebasejs/9.22.2/firebase-app-compat.js");
importScripts("https://www.gstatic.com/firebasejs/9.22.2/firebase-messaging-compat.js");

// Initialize Firebase with the config
firebase.initializeApp({
    apiKey: "AIzaSyCuGM7HsgSjyXzomV6I6mw0CyA0iECCVoo",
    authDomain: "kraftbase-494b6.firebaseapp.com",
    projectId: "kraftbase-494b6",
    storageBucket: "kraftbase-494b6.firebasestorage.app",
    messagingSenderId: "850200648537",
    appId: "1:850200648537:web:38b811655859e9aa380a48",
    measurementId: "G-CWYZPKW3H7"
});

// Get Firebase messaging
const messaging = firebase.messaging();

// Background message handler
messaging.onBackgroundMessage(function(payload) {
  const { title, body, image, click_action } = payload.notification;
  self.registration.showNotification(title, {
    body,
    icon: image || "/icon.png",
    data: {
      url: click_action || "/"
    }
  });
});

// Notification click handler
self.addEventListener('notificationclick', function(event) {
  event.notification.close();
  event.waitUntil(clients.openWindow(event.notification.data.url));
});
