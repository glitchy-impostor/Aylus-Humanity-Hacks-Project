import React from 'react'; 

const Card = (props) => {
    return (
        <div className='event-card'>
            <div className='card_body'>
                <h2 className='card_title'>{props.title}</h2>
                <p className='card_description'>{props.description}</p>
            </div>
            <button className='card_btn'>View Event</button>
        </div>
    );
}

export default Card; 