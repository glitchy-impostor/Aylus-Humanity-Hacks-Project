import React from "react";
import Card from "./Cards";
const CurrentEvents = () => {
    return (
        <div className="wrapper">
            <h2>Activities Going On</h2>
            <Card title='Tree Plantr' description='A tree planting meetup' time="5:00 PM EST"/>
            <Card title='Ocean Cleanup' description='An ocean cleanup meetup' time='6:00 PM PST'/>        
        </div>
       
    );
}

export default CurrentEvents; 