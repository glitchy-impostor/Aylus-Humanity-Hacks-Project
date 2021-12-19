import React from 'react';
import './cards.scss'

const Card = (props) => {
  return (
    <div className='event-card' onClick={props.onClick}>
        <div className='card_body'>
          {(props.img !== undefined) &&
            <div className='image'>
              <img src={props.img} alt="logo" />
            </div>
          }
          <h2 className='card_title'>{props.title}</h2>
          <h4 className='card_title'>{props.itemName}</h4>
          <h4 className='card_creator'>{props.creator}</h4>
          <p className='card_description'>{props.description}</p>
          <p className='event_date'>{props.date}</p>
          {(props.time !== undefined) && 
            <li className='event_time'>{props.time}</li>
          }
          <p className='event_location'>{props.location}</p>
        </div>
        <button className='card_btn'>{props.btn}</button>
    </div>
  );
}

export default Card; 