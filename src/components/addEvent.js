import React from "react";

const AddEvents = () => {
    return (
        <div className="outer">
        <div className="inner">
            <form>

                <h3>Add Event!</h3>

                <div className="form-group">
                    <label>Event Name</label>
                    <input type="name" className="form-control" placeholder="Enter Event Name" />
                </div>

                <div className="form-group">
                    <label>Creator</label>
                    <input type="name" className="form-control" placeholder="Enter name of the event creator or organizer!" />
                </div>

                <div className="form-group">
                    <label>Location</label>
                    <input type="name" className="form-control" placeholder="Enter location of event!"/>
                </div>

                <div className="form-group">
                    <label>Date</label>
                    <input type="text" className="form-control" placeholder="Enter Date of Event" />
                </div>

                <div className="form-group">
                    <label>Event Description</label>
                    <input type="text" className="form-control" placeholder="Enter a description of the event" />
                </div>

                    <button type="submit" className="btn btn-dark btn-lg btn-block">Add Event!</button>
                    
                
            </form>
        </div>
        </div>
       
    );
}

export default AddEvents; 