import React from 'react';
import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";

import NavBar from './components/navbar';
import Login from "./components/login";
import SignUp from "./components/signup";
import CurrentEvents from './components/events/currentEvents';
import Donate from './components/donate/donate';
import Schedule from './components/donate/schedule';
import AddEvent from './components/addEvent';
import Registration from './components/business/registration';
import Leaderboard from './components/leaderboard/leaderboard';
import Marketplace from './components/marketplace/marketplace';
import AddItem from './components/marketplace/addItems';
import Homepage from './components/homepage/homepage';
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

function App() {

  return (<Router>
    <div className="App">
      <NavBar/>
      <Switch>
        <Route exact path='/' component={Homepage} />
        <Route path="/sign-in" component={Login} />
        <Route path="/sign-up" component={SignUp} />
        <Route path='/current-events' component={CurrentEvents}/>
        <Route path='/donate' component={Donate}/>
        <Route path='/schedule' component={Schedule}/>
        <Route path='/add-event' component={AddEvent}/>
        <Route path='/registration' component={Registration}/>
        <Route path='/leaderboard' component={Leaderboard}/>
        <Route path='/marketplace' component={Marketplace}/>
        <Route path='/add-item' component={AddItem}/>
      </Switch>
      <ToastContainer/>
    </div>
    
    </Router>
    
  );
}

export default App;