import React from 'react';
import './components.css';
import DropDown from './DropDown';

const ToolsPanel = () => {
  return (
    <div className="tools-panel">
        <h1 className="text-xl font-semibold">Tools</h1>
        <DropDown />
    </div>

  );
};

export default ToolsPanel;