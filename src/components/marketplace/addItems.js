import React from "react";
import "./addItems.scss"
const AddItems = () => {

    const onSubmitHandler = (e) => {
        e.preventDefault();
        const jq = window.$;
        let name = document.getElementById('item_name').value;
        let brand = document.getElementById('brand').value;
        let description = document.getElementById('description').value;
        let mrp = document.getElementById('cost').value;
        let random_key = '';
        let doa = '';
        let location = document.getElementById('location').value;
        let contact_info = document.getElementById('contact_info').value;
        let cookieData = decodeURIComponent(document.cookie).split('; ');
        let m;
        let condition = 0; //0 or 1 => 0 == Resell | 1 == Recycle
        for(m in cookieData){
          if(cookieData[m].includes('random_key=')){
            random_key = cookieData[m].replace('random_key=', '');
          }else if(cookieData[m].includes('doa')){
            doa = cookieData[m].replace('doa=', '');
          }
        }
        if(random_key != '' && doa != ''){
          jq.ajax({
            url: '/api/add/items',
            type: 'POST',
            data: {'name': name, 'brand': brand, 'description': description, 'mrp': mrp, 'random_key': random_key, 'doa':doa, 'location': location, 'contact_info': contact_info, 'condition': condition},
            success: function(res){
              if(res.conf == 0){
                alert('Item Successfully Added!');
                //Redirection Code Here
              }else{
                alert('You are not logged in! Please Log in to add Items!');
                //Redirect to login Page
              }
            }
          })
        }else{
          alert('You are not logged in! Please Log in to add Items!');
          //Redirect to login Page
        }
    }

    return (
      <div className="outer add-items">
        <div className="inner">
            <form onSubmit={onSubmitHandler}>

                <h3>Add Items to Marketplace</h3>

                <div className="form-group">
                    <label>Item Name</label>
                    <input id="item_name" type="text" className="form-control" placeholder="Enter Item Name" />
                </div>

                <div className="form-group">
                    <label>Brand</label>
                    <input id="brand" type="text" className="form-control" placeholder="Enter Brand Name" />
                </div>

                <div className="form-group">
                    <label>Location (City)</label>
                    <input id="location" type="text" className="form-control" placeholder="Enter City Name" />
                </div>

                <div className="form-group">
                    <label>Selling Price</label>
                    <input id="cost" type="text" className="form-control" placeholder="Enter Selling Price in $" />
                </div>

                <div className="form-group">
                    <label>Contact Info</label>
                    <input id="contact_info" type="text" className="form-control" placeholder="Enter a way to Contact You" />
                </div>

                <div className="form-group">
                    <label>Description</label>
                    <input id="description" type="text" className="form-control" placeholder="Enter Description" />
                </div>

                <div className="form-group">
                    <div className="custom-control custom-checkbox">
                        <input type="checkbox" className="custom-control-input" id="customCheck1" />
                        <label className="custom-control-label" htmlFor="customCheck1">Remember me</label>
                    </div>
                </div>

                    <button type="submit" className="btn btn-dark btn-lg btn-block">Sign In</button>
                    <p className="forgot-password text-right">
                        <a href="#">Forgot Password?</a>
                    </p>

                </form>
            </div>
          </div>

        );
    }
export default AddItems;
