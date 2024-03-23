import { useEffect, useRef, useState } from 'react';
import axios from 'axios';
import styles from '../css/Home.module.css';

export default function Home() {
  const imgRef = useRef(null);
  const [message, setMessage] = useState('');

  useEffect(() => {
    // MJPEG URL
    const videoStreamUrl = 'http://127.0.0.1:5000/video_feed';
    // Set the image source to the MJPEG URL
    if (imgRef.current) {
      imgRef.current.src = videoStreamUrl;
    }
  }, []);

  async function takeSnapshot() {
    try {
      await axios.post('http://127.0.0.1:5000/take_snapshot');
      setMessage('Snapshot taken successfully!');
    } catch (error) {
      console.error('Error taking snapshot:', error);
      setMessage('Error taking snapshot.');
    }
  }

  return (
    <div>
      <h1>Pocket Fit</h1>
      <div className={styles.container}>
        {/* Use the traditional src attribute for MJPEG stream */}
        <img ref={imgRef} width="100%" height="100%" alt="Video Stream" />
      </div>
      <button onClick={takeSnapshot}>Take Snapshot</button>
      {message && <p>{message}</p>}
    </div>
  );
}