import React, { useState } from "react";
import { Redirect } from 'react-router-dom';
import { toast } from 'react-toastify';
import "./registration.scss";

const Registration = () => {
  const [redirect, setRedirect] = useState(false)

  const onSubmitHandler = (e) => {
    e.preventDefault();
    // var data = {
    //   name: e.target[0].value,
    //   email: e.target[1].value,
    //   contact: e.target[2].value,
    //   address: e.target[3].value,
    //   postal: e.target[4].value,
    // }
    toast("Your company has been registered!");
    setRedirect(true);
  }

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
    <div className='spacer'>
      <div className='donate'>
        <h2>Register Your Company</h2>
        <h4>Registered companies can list products and receive donations</h4>

        
        <form onSubmit={onSubmitHandler}>

        <div className="form-group">
          <label>Company Name</label>
          <input required type="text" className="form-control" placeholder="Goggle" />
        </div>
        <div className="form-group">
          <label>Company Website</label>
          <input required type="text" className="form-control" placeholder="www.goggle.com" />
        </div>
        <div className="form-group">
          <label>Company Description</label>
          <input required type="text" className="form-control" placeholder="We make goggles from recycled materials" />
        </div>
        <div className="form-group">
          <label>Materials Wanted for Donation</label>
          <input required type="text" className="form-control" placeholder="Plastics, glass, textiles" />
        </div>
        <div className="form-group">
          <label>Company Email</label>
          <input required type="text" className="form-control" placeholder="Email" />
        </div>
        <div className="form-group">
          <label>Contact Number</label>
          <input required type="text" className="form-control" placeholder="Contact number" />
        </div>
        <div className="form-group">
          <label>Contact Person</label>
          <input required type="text" className="form-control" placeholder="Contact Person" />
        </div>
        <div className="form-group">
          <label>Street Address</label>
          <input required type="text" className="form-control" placeholder="Street Address" />
        </div>
        <div className="form-group">
          <label>Postal Code</label>
          <input required type="text" className="form-control" placeholder="Postal Code" />
        </div>

        <button type="submit" className="btn btn-dark btn-lg btn-block">Register</button>

        </form>
      </div>
    </div>
      
  );
}

export default Registration; 