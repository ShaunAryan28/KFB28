import { useEffect, useState } from "react";
import "./App.css";
import { initializeApp } from "firebase/app";
import { getMessaging, getToken, onMessage } from "firebase/messaging";

import Navbar from "./components/Navbar";

// Firebase config
const firebaseConfig = {
  apiKey: "AIzaSyCuGM7HsgSjyXzomV6I6mw0CyA0iECCVoo",
  authDomain: "kraftbase-494b6.firebaseapp.com",
  projectId: "kraftbase-494b6",
  storageBucket: "kraftbase-494b6.firebasestorage.app",
  messagingSenderId: "850200648537",
  appId: "1:850200648537:web:38b811655859e9aa380a48",
  measurementId: "G-CWYZPKW3H7",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const messaging = getMessaging(app);

function App() {
  const [status, setStatus] = useState("Click to subscribe");

  const subscribe = async () => {
    try {
      const permission = await Notification.requestPermission();
      if (permission !== "granted") {
        setStatus("Permission denied");
        return;
      }

      const token = await getToken(messaging, {
        vapidKey:
          "BOGB7zbq3fXSMMG5cvHMJDj8JN8Nz3WHxIXc9MWpA0DEFsT5M5gEO1aarDN4iTnTik1qc305Otq32BOMzWSAd70",
      });

      console.log("FCM Token:", token);

      const res = await fetch(
        `${import.meta.env.VITE_BACKEND_URL}/devices/register`,
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ fcm_token: token }),
        }
      );

      const data = await res.json();
      setStatus(data.message || "Subscribed!");
    } catch (err) {
      console.error("Subscription failed", err);
      setStatus("Subscription failed");
    }
  };

  // 👉 Handle foreground messages
  useEffect(() => {
    const unsubscribe = onMessage(messaging, (payload) => {
      console.log("📩 Foreground message received:", payload);
      const { title, body, image } = payload.notification;

      // Show a native browser notification
      new Notification(title, {
        body,
        icon: image || "/icon.png",
      });
    });

    return unsubscribe;
  }, []);

  return (
    <div>
      <Navbar />
      <div style={{ textAlign: "center", paddingTop: "2rem" }}>
        <h1>🔔 Web Notification System</h1>
        <button onClick={subscribe}>Subscribe</button>
        <p>{status}</p>
      </div>

      
    </div>
  );
}

export default App;
