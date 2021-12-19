import React from "react";
import Card from "./Cards";
import "./currentEvents.scss";
const CurrentEvents = () => {
    return (
			<div className='spacer'>
				<div className='current-events'>
					<h2>Activities Going On</h2>
					<div className='wrapper'>
							<Card title='Tree Plantr' description='A tree planting meetup' time="5:00 PM EST"/>
							<Card title='Ocean Cleanup' description='An ocean cleanup meetup' time='6:00 PM PST'/>  
							<Card title='Tree Plantr' description='A tree planting meetup' time="5:00 PM EST"/>
					</div>
				</div>
			</div>
       
    );
}

export default CurrentEvents; 