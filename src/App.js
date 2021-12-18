import React from 'react';
import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";

import Login from "./components/login";
import SignUp from "./components/signup";
import CurrentEvents from './components/currentEvents';
import NavBar from './components/navbar';

function App() {

  return (<Router>
    <div className="App">
      <NavBar/>
      <div className="outer">
        <div className="inner">
          <Switch>
            <Route exact path='/' component={Login} />
            <Route path="/sign-in" component={Login} />
            <Route path="/sign-up" component={SignUp} />
            <Route path='/current-events' component={CurrentEvents}/>
          </Switch>
        </div>
      </div>
    </div>
    
    </Router>
    
  );
}

export default App;