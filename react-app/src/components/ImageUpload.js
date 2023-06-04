import React, { useState } from 'react';
import axios from 'axios';
import './components.css';

const ImageUpload = () => {
  const [image, setImage] = useState(null);

  const handleImageUpload = (e) => {
    const file = e.target.files[0];
    setImage(URL.createObjectURL(file));
  };

  const handleSubmit = () => {
    if (image) {
      const formData = new FormData();
      formData.append('image', image);

      axios.post('http://localhost:5000/upload', formData)
        .then((response) => {
          console.log(response.data); // Handle response from the backend
        })
        .catch((error) => {
          console.error(error); // Handle error if any
        });
    }
  };

  return (
    <div className="image-upload">
      <div className="flex items-center justify-center w-full">
        {image ? (
          <img src={image} alt="Uploaded" className="uploaded-image" />
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
      <button onClick={handleSubmit}>Upload Image</button>
    </div>
  );
};

export default ImageUpload;
