import React from 'react';
import ReactDOM from 'react-dom';
import logo from './logo.svg';
import { Button } from 'antd';
import './App.css';
import 'antd/dist/antd.css';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";


function App() {
  return (
    <div className="App">
    <Router>
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <Link to="/customer">
        <Button>
          Customer
        </Button>
        </Link>
        
        <Button href="/owner">
          Drink Stall Owner
        </Button>
      </header>
      </Router>
    </div>
  );
}

export default App;
