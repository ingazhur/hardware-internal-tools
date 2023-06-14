import React, { useState } from 'react';

const ImageUploadTool = () => {
  const [image, setImage] = useState(null);

  const handleImageUpload = (e) => {
    const file = e.target.files[0];
    setImage(URL.createObjectURL(file));
  };

  return (
    <div>
      <div className="flex items-center justify-center w-full">
        {image ? (
          <img src={image} alt="Uploaded" className="uploaded-image" />
        ) : (
            <label>
                Upload
                <input type="file" className="hidden" onChange={handleImageUpload} />
            </label>
        )}
      </div>
    </div>
  );
};

export default ImageUploadTool;
