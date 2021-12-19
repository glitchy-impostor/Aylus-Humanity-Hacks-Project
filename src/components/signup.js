import React from "react";

const SignUp = () => {

    const onSubmitHandler = (e) => {
          e.preventDefault();
          const jq = window.$;
          let email_address = document.getElementById('email').value;
          let password = document.getElementById('password').value;
          let name = document.getElementById('firstName').value + ' ' + document.getElementById('lastName').value;
          jq.ajax({
            url: '/api/signup',
            type: 'POST',
            data: {'email_address': email_address, 'password': password, 'name':name},
            success: function(res){
              console.log(res);
              if(res.conf == 0){
                document.cookie = `doa=${res.doa}; path=/`;
                document.cookie = `random_key=${res.randomKey}; path=/`;
                window.location.href = '/home';
              }else if(res.conf == 1){
                alert('Email Address is already registered. Sign up with another Email or Login instead!');
              }
            }
          })
    }
    
    return (
      <div className="outer">
        <div className="inner">
          <form onSubmit={onSubmitHandler}>
              <h3>Register</h3>

              <div className="form-group">
                  <label>First name</label>
                  <input id="firstName" type="text" className="form-control" placeholder="First name" />
              </div>

              <div className="form-group">
                  <label>Last name</label>
                  <input id="lastName" type="text" className="form-control" placeholder="Last name" />
              </div>

              <div className="form-group">
                  <label>Email</label>
                  <input id="email" type="email" className="form-control" placeholder="Enter email" />
              </div>

              <div className="form-group">
                  <label>Password</label>
                  <input id="password" type="password" className="form-control" placeholder="Enter password" />
              </div>

              <button type="submit" className="btn btn-dark btn-lg btn-block">Register</button>
              <p className="forgot-password text-right">
                  Already registered <a href="/sign-in">log in?</a>
              </p>
          </form>
        </div>
      </div>
    );
}
export default SignUp;
