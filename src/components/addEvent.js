
import React, { useState } from "react";
import { Redirect } from 'react-router-dom';
import { toast } from 'react-toastify';

const AddEvents = () => {
  const [redirect, setRedirect] = useState(false);


  const onSubmitHandler = (e) => {
    e.preventDefault();
    const jq = window.$;
    let random_key = '';
    let doa = '';
    let cookieData = decodeURIComponent(document.cookie).split('; ');
    let m;
    for(m in cookieData){
      if(cookieData[m].includes('random_key=')){
        random_key = cookieData[m].replace('random_key=', '');
      }else if(cookieData[m].includes('doa')){
        doa = cookieData[m].replace('doa=', '');
      }
    }
    let name = document.getElementById('name').value;
    let description = document.getElementById('description').value;
    let date = document.getElementById('date').value;
    let time = document.getElementById('time').value;
    let location = document.getElementById('location').value;
    if(random_key != '' && doa != ''){
      jq.ajax({
        url: '/api/create/even',
        type: 'POST',
        data: {'random_key': random_key, 'doa': doa, 'name':name, 'description': description, 'date':date, 'time':time, 'location':location},
        success: function(res){
          if(res.conf == 0){
            alert('Event has successfully been Created!');
            window.location.href="/home";
          }else{
            alert('You are not logged in! Please Log in to create Events!');
          }
        }
      })
    }else{
      alert('You are not logged in! Please Log in to create Events!');
    }
    toast("Yay you scheduled a pickup!");
    setRedirect(true);
  }

  if (redirect) {
    return (
      <Redirect
        to={{
          pathname: "/donate",
          state: { showToast: true }
        }}
      />
    )
  }
  
  return (
    <div className="outer">
    <div className="inner">
        <form onSubmit={onSubmitHandler}>

          <h3>Add Event!</h3>

          <div className="form-group">
              <label>Event Name</label>
              <input required id="name" type="name" className="form-control" placeholder="Enter Event Name" />
          </div>
          <div className="form-group">
              <label>Creator</label>
              <input required  type="name" className="form-control" placeholder="Enter name of the event creator or organizer!" />
          </div>
          <div className="form-group">
              <label>Location</label>
              <input required id="location" type="name" className="form-control" placeholder="Enter general location of event! (General Area Will Do)"/>
          </div>

          <div className="form-group">
              <label>Date</label>
              <input required id="date" type="text" className="form-control" placeholder="Enter Date of Event" />
          </div>
  
          <div className="form-group">
              <label>Time</label>
              <input required id="time" type="text" className="form-control" placeholder="Enter Time of Event in 24 Hour Format" />
          </div>

          <div className="form-group">
              <label>Event Description</label>
              <input required id="description" type="text" className="form-control" placeholder="Enter a description of the event! (Also include a way to contact you here)" />
          </div>

          <button type="submit" className="btn btn-dark btn-lg btn-block">Add Event!</button>
                
            
        </form>
      </div>
      </div>
      
  );
}

export default AddEvents; 
