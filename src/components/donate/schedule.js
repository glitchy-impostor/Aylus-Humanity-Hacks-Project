import { format, isSameDay, nextSunday } from 'date-fns';
import React, { useState } from "react";
import { Redirect } from 'react-router-dom';
import { toast } from 'react-toastify';
import "./schedule.scss"

const Schedule = (props) => {

  const [redirect, setRedirect] = useState(false)
  const [collectionDate, setCollectionDate] = useState(nextSunday(new Date()));

  const onSubmitHandler = (e) => {
    e.preventDefault();
    var data = {
      name: e.target[0].value,
      email: e.target[1].value,
      contact: e.target[2].value,
      address: e.target[3].value,
      postal: e.target[4].value,
    }
    toast("Yay you scheduled a pickup!");
    setRedirect(true);
  }

    const sunday = nextSunday(new Date());
    const sunday2 = nextSunday(sunday);
    const sunday3 = nextSunday(sunday2);
    const sunday4 = nextSunday(sunday3);  
    const dates = [
      sunday, sunday2, sunday3, sunday4
    ]

    if (redirect) {
      return (
        <Redirect
          to={{
            pathname: "/",
            state: { showToast: true }
          }}
        />
      )
    }
    
    return (
      <div className="outer schedule">
        <div className="inner">
            <form onSubmit={onSubmitHandler}>

                <h3>Schedule a Pickup for {props.location.state.company}</h3>

                {dates.map((d) => {
                  return (
                    <div className="form-group">
                      <div 
                        className={'btn ' + (isSameDay(collectionDate, d) ? 'btn-success' : 'btn-light')}
                        onClick={() => setCollectionDate(d)}>
                          {format(d, 'PPPP')}
                      </div>
                    </div>
                  )
                })}

                <div className="form-group">
                  <label>Name</label>
                  <input required type="text" className="form-control" placeholder="Name" />
                </div>
                <div className="form-group">
                  <label>Email</label>
                  <input required type="text" className="form-control" placeholder="Email" />
                </div>
                <div className="form-group">
                  <label>Contact number</label>
                  <input required type="text" className="form-control" placeholder="Contact number" />
                </div>
                <div className="form-group">
                  <label>Street Address</label>
                  <input required type="text" className="form-control" placeholder="Street Address" />
                </div>
                <div className="form-group">
                  <label>Postal Code</label>
                  <input required type="text" className="form-control" placeholder="Postal Code" />
                </div>

                    <button type="submit" className="btn btn-dark btn-lg btn-block">Confirm</button>
                
                </form>
            </div>
          </div>
            
        );
    }
export default Schedule;

