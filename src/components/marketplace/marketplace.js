import React from "react";
import Card from "../cards/cards";
import { toast } from 'react-toastify';
import "./marketplace.scss";

const Marketplace = () => {

  const onCardClick = () => {
    toast("Added to cart");
  }

  return (
    <div className='spacer'>
      <div className='marketplace'>
        <h3>Marketplace</h3>
        <h4>View upcycled products and pre-loved items</h4>
        <div className='wrapper'>
          <Card 
            onClick={onCardClick}
            img='https://i.pinimg.com/originals/4f/eb/ed/4febedaa89e8bb159fd5e0cc37efd236.jpg'
            itemName='Pineapple Leather Boots'
            description='Made from pineapple leaves that are shredded into fibres and turned into leather' 
            creator='Ananas Anam'
            time="$89"
            btn="Add to cart"/>
        </div>
      </div>
    </div>
      
  );
}

export default Marketplace; 