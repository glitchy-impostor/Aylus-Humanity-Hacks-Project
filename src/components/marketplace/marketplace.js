import React from "react";
import Card from "../cards/cards";
import "./marketplace.scss";

const Marketplace = () => {
    return (
			<div className='spacer'>
				<div className='marketplace'>
					<h3>Marketplace</h3>
					<h4>View upcycled products and pre-loved items</h4>
					<div className='wrapper'>
							<Card 
                itemName='Pineapple Leather Boots'
                description='Made from pineapple leaves that are shredded into fibres and turned into leather' 
                creator='Ananas Anam'
                time="$89"
                btn="Select"/>
					</div>
				</div>
			</div>
       
    );
}

export default Marketplace; 