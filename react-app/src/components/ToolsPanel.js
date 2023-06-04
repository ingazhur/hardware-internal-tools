import React from 'react';
import './components.css';
import DropDown from './DropDown';
import ImageUploadTool from './ImageUploadTool';
import Main from './Main';

const ToolsPanel = () => {
  return (
    <div className="tools-panel">
        <h1 className="text-xl font-semibold">Tools</h1>
        <DropDown />
        <Main />
    </div>

  );
};

export default ToolsPanel;