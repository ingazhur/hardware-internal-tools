import React from 'react';
import ToolsPanel from './components/ToolsPanel';
import ImageUpload from './components/ImageUpload';
import Header from './components/Header';
import './App.css';


const App = () => {

  return (
    <div className="app">
      <div className="header">
        <Header />
      </div>
      <div className="container">
        <ToolsPanel />
        <ImageUpload />
      </div>
    </div>
  );
};

export default App;