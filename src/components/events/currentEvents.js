import React, { useState } from "react";
import Card from "../cards/cards";
import "./currentEvents.scss";
const CurrentEvents = () => {
  const [data, setData] = useState([]);
	function getEvents(){
		const jq = window.$;
		let city = 'San Francisco, USA';
		jq.ajax({
			url: '/api/search/events',
			type: 'POST',
			data: {'city_name': city},
			success: function(res){
        console.log("get events")
        console.log(res.data)
				setData(res.data);
			}
		})
	}
  console.log(data)
	getEvents();
    return (
			<div className='spacer'>
				<div className='current-events'>
					<h2>Events</h2>
					<h4>Activities Going On</h4>
					<div className='wrapper'>
            {data.map(dp => (
            <Card
							title={dp.name}
							description={dp.description}
							date={dp.date}
							time={dp.time}
							creator={dp.organiser}
							location={dp.location}
							btn="Sign Up"/>
            ))}
						<Card
              img='https://compote.slate.com/images/c465d192-5e36-4533-90fc-e198da3f061a.jpeg?width=780&height=520&rect=1560x1040&offset=0x0'
							title='Tree Plantr'
							description='A tree planting meetup'
							date="11-25-2022"
							creator='Save the Trees'
							location='Yosemite National Park, California'
							btn="Sign Up"/>
						<Card
              img='https://images.unsplash.com/photo-1507525428034-b723cf961d3e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8dHJvcGljYWwlMjBiZWFjaHxlbnwwfHwwfHw%3D&w=1000&q=80'
							title='Ocean Cleanup'
							description='An ocean cleanup meetup'
							date='12-19-2021'
							creator='Kenneth Choi'
							location='New Delhi, India'
							btn="Sign Up"/>
						<Card
              img='https://communityimpact.com/wp-content/uploads/2016/12/Fotolia_112023896_Subscription_XXL.jpg'
							title='Nature Cleanup'
							description='A tree planting meetup'
							date="1-5-2022"
							creator='Shannon Lee'
							location='Seattle, Washington'
							btn="Sign Up"/>
					</div>
				</div>
			</div>

    );
}

export default CurrentEvents;
