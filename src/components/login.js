import React from "react";

const Login = () => {

    const onSubmitHandler = (e) => {
        e.preventDefault();
        const jq = window.$;
        let email_address = document.getElementById('email').value;
        let password = document.getElementById('password').value; //replace these with actual vals later
        jq.ajax({
            url: '/api/login',
            type: 'POST',
            data: {'username': email_address, 'password': password},
            success: function(res){
             if(res.conf == 0){
                 document.cookie = `doa=${res.doa}; path=/`;
                 document.cookie = `random_key=${res.randomKey}; path=/`;
                 window.location.href = "/donate";
             }else if(res.conf == 1){
                 alert('You entered the wrong password. Enter the correct password to log in!');
             }else if(res.conf == 2){
                 alert('The Email Address Entered is not registered. Sign Up or use a registered address!');
             }
             }
         })
        window.location.href = "/donate";
    }

    return (
      <div className="outer">
        <div className="inner">
            <form onSubmit={onSubmitHandler}>

                <h3>Log in</h3>

                <div className="form-group">
                    <label>Email</label>
                    <input id="email" type="email" className="form-control" placeholder="Enter email" />
                </div>

                <div className="form-group">
                    <label>Password</label>
                    <input id="password" type="password" className="form-control" placeholder="Enter password" />
                </div>

                <div className="form-group">
                    <div className="custom-control custom-checkbox">
                        <input type="checkbox" className="custom-control-input" id="customCheck1" />
                        <label className="custom-control-label" htmlFor="customCheck1">Remember me</label>
                    </div>
                </div>

                <button type="submit" className="btn btn-dark btn-lg btn-block">Sign In</button>
                <p className="forgot-password text-right">
                    <a href="/sign-up">Sign up</a>
                </p>
                
                </form>
            </div>
          </div>
            
        );
    }
export default Login;

