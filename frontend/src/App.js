import React from 'react';
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
        <p>
         Welcome To Drink-Drinks. Get started by choosing your user type below.
        </p>
        <Link to="/customer">
        <Button>
          Customer
        </Button>
        </Link>
        <Link to="/owner">
        <Button>
          Drink Stall Owner
        </Button>
        </Link>
      </header>
      </Router>
    </div>
  );
}

export default App;
