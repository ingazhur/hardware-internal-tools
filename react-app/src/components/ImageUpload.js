import React, { useState, useRef, useEffect } from 'react';
import axios from 'axios';
import './components.css';

const ImageUpload = () => {
    const [image, setImage] = useState(null);
    const [rectangles, setRectangles] = useState([]);
    const canvasRef = useRef(null);
    const isDrawingRef = useRef(false);
    const startPointRef = useRef(null);
    const [mouseMove, setMouseMove] = useState({ x: 0, y: 0 });
  
    useEffect(() => {
      if (image) {
        const canvas = canvasRef.current;
        const ctx = canvas.getContext('2d');
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.drawImage(image, 0, 0);
        rectangles.forEach(rectangle => {
          ctx.beginPath();
          ctx.rect(rectangle.x, rectangle.y, rectangle.width, rectangle.height);
          ctx.strokeStyle = 'red';
          ctx.lineWidth = 2;
          ctx.stroke();
        });
      }
    }, [image, rectangles]);

    const handleMouseMove = e => {
      const canvas = canvasRef.current;
      const rect = canvas.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      setMouseMove({ x, y });
    };
  
    const handleImageUpload = e => {
      const file = e.target.files[0];
      const img = new Image();
      img.src = URL.createObjectURL(file);
      img.onload = () => {
        setImage(img);
      };
  
      e.preventDefault();
    };
  
    const handleMouseDown = e => {
      const canvas = canvasRef.current;
      const rect = canvas.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
  
      isDrawingRef.current = true;
      startPointRef.current = { x, y };
    };
  
    const handleMouseUp = e => {
      if (isDrawingRef.current) {
        const canvas = canvasRef.current;
        const rect = canvas.getBoundingClientRect();
        const x = startPointRef.current.x - rect.left;
        const y = startPointRef.current.y - rect.top;
        const width = e.clientX - rect.left - startPointRef.current.x;
        const height = e.clientY - rect.top - startPointRef.current.y;
  
        const newRectangle = { x, y, width, height };
        setRectangles(prevRectangles => [...prevRectangles, newRectangle]);
  
        isDrawingRef.current = false;
      }
    };

  return (
    <div className="image-upload">
      <div className="flex items-center justify-center w-full" style={{ overflow: 'hidden' }}>
      {image ? (
        <div style={{ maxWidth: '100%', height: '100%'}}>
            <canvas
                ref={canvasRef}
                width={image.width}
                height={image.height}
                style={{ objectFit: 'contain', width: '100%', height: '100%' }}
                className="uploaded-image"
                onMouseDown={handleMouseDown}
                onMouseUp={handleMouseUp}
                onMouseMove={handleMouseMove}
            />
            <p>Mouse X: {mouseMove.x}</p>
            <p>Mouse Y: {mouseMove.y}</p>
        </div>
        ) : (
          <label
            htmlFor="dropzone-file"
            className="flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 light:hover:bg-bray-800 light:bg-gray-700 hover:bg-gray-100 light:border-gray-600 light:hover:border-gray-500 light:hover:bg-gray-600"
          >
            <div className="flex flex-col items-center justify-center pt-6 pb-6 pl-4 pr-4">
              <svg
                aria-hidden="true"
                className="w-10 h-10 mb-3 text-gray-400"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth="2"
                  d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"
                ></path>
              </svg>
              <p className="mb-2 text-sm text-gray-500 light:text-gray-400">
                <span className="font-semibold">Click to upload</span> or drag and drop
              </p>
              <p className="text-xs text-gray-500 light:text-gray-400">PNG, JPG, JPEG</p>
            </div>
            <input
              id="dropzone-file"
              type="file"
              className="hidden"
              onChange={handleImageUpload}
            />
          </label>
        )}
      </div>
    </div>
  );
};

export default ImageUpload;
