import React, { useState } from 'react';
import logo from './logo.svg';
import './App.css';
import Nav from './components/Nav';
import Book from './components/Book';
import Services from './components/Services';
import Login from './components/Login';

function App() {
  const [showNav, setShowNav] = useState(true);
  const [showBook, setShowBook] = useState(true);
  const [showServices, setShowServices] = useState(true);
  return (
    <div>
      {/* <Nav /> */}
      {showNav && <Nav />}
      <Book message="hey" />
      <Services />
    </div>
  );
}

export default App;
