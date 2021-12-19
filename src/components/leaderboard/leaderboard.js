import React from "react";
import Card from "../cards/cards";
import "./leaderboard.scss";

const Leaderboard = () => {
    return (
			<div className='spacer'>
				<div className='donate'>
					<h2>Donate</h2>
					<h4>List of Participating Companies</h4>
					<div className='wrapper'>
							<Card 
                title='TerraCycle' 
                description='TerraCycle converts the waste into new products, such as park benches or backpacks.' 
                time="Plastics"
                btn="Select"/>
							<Card 
                title='Playback' 
                description='Playback clothing creates tees, hoodies, and sweatshirts by transforming trash - plastic bottles and clothing scraps - into eco-clothing!' 
                time="Textiles"
                btn="Sign Up"/>
							<Card 
                title='Hipcycle' 
                description='Online retailer Hipcycle, upcycles goods to create home decor, jewelry and fashionp' 
                time="Plastics, books, textiles"
                btn="Sign Up"/>
							<Card 
                title='Preserve' 
                description='Preserve is a company that collects recycled goods and makes toothbrushes and kitchenware' 
                time="Plastics, wood, glass"
                btn="Sign Up"/>
					</div>
				</div>
			</div>
       
    );
}

export default Leaderboard; 