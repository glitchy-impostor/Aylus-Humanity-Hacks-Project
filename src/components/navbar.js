import React from "react";
import {Link} from "react-router-dom";

const NavBar = () => {
    return <nav className="navbar navbar-expand-lg navbar-light fixed-top">
        <div className="container">
          <Link className="navbar-brand" to={"/"}>TrashsureCove</Link>
          <div className="collapse navbar-collapse" id="navbarTogglerDemo02">
            <ul className="navbar-nav ml-auto">
              <li className='nav-item'>
                <Link className='nav-link' to={'/current-events'}>Current Events</Link>
              </li>
              <li className='nav-item'>
                <Link className='nav-link' to={'/donate'}>Donate</Link>
              </li>
              <li>
                <Link className='nav-link' to={'/add-event'}>Host Event</Link>
              </li>
              <li>
                <Link className='nav-link' to={'/marketplace'}>Marketplace</Link>
              </li>
              <li>
                <Link className='nav-link' to={'/registration'}>Business</Link>
              </li>
            </ul>
            <ul className="navbar-nav ml-auto">
              <li>
                <Link className='nav-link' to={'/leaderboard'}>Leaderboard</Link>
              </li>
              <li className='nav-item'>
                <Link className='nav-link' to={'/sign-in'}>Sign In</Link>
              </li>
            </ul>
          </div>
        </div>
      </nav>
}

export default NavBar; 