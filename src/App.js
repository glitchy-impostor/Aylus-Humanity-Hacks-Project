import React from 'react';
import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";

import NavBar from './components/navbar';
import Login from "./components/login";
import SignUp from "./components/signup";
import CurrentEvents from './components/events/currentEvents';
import Donate from './components/donate/donate';

function App() {

  return (<Router>
    <div className="App">
      <NavBar/>
      <Switch>
        <Route exact path='/' component={Login} />
        <Route path="/sign-in" component={Login} />
        <Route path="/sign-up" component={SignUp} />
        <Route path='/current-events' component={CurrentEvents}/>
        <Route path='/donate' component={Donate}/>
      </Switch>
    </div>
    
    </Router>
    
  );
}

export default App;