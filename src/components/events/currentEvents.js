import React from "react";
import Card from "../cards/cards";
import "./currentEvents.scss";
const CurrentEvents = () => {
	let data = [];
	function getEvents(){
		const jq = window.$;
		let city = 'San Francisco, USA';
		jq.ajax({
			url: '/api/search/events',
			type: 'POST',
			data: {'city_name': city},
			success: function(res){
				data = res.data;
			}
		})
	}
	getEvents();
    return (
			<div className='spacer'>
				<div className='current-events'>
					<h2>Events</h2>
					<h4>Activities Going On</h4>
					<div className='wrapper'>
            {data.map(d => {
				      return (
                <Card 
                  title={d.name}
                  description={d.description} 
                  date={d.date}
                  creator={d.organiser}
                  location={d.location}
                  btn="Sign Up"/>
              )
            })}
	   					
						{/* <Card 
							title='Tree Plantr' 
							description='A tree planting meetup' 
							date="11-25-2022"
							creator='Save the Trees'
							location='Yosemite National Park, California'
							btn="Sign Up"/>
						<Card 
							title='Ocean Cleanup' 
							description='An ocean cleanup meetup' 
							date='12-19-2021'
							creator='Kenneth Choi'
							location='New Delhi, India'
							btn="Sign Up"/>
						<Card 
							title='Tree Plantr' 
							description='A tree planting meetup' 
							date="1-5-2022"
							creator='Shannon Lee'
							location='Seattle, Washington'
							btn="Sign Up"/> */}
					</div>
				</div>
			</div>
       
    );
}

export default CurrentEvents; 
