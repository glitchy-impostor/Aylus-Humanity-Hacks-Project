import React, { useState } from "react";
import { Redirect } from 'react-router-dom/cjs/react-router-dom.min';
import Card from "../cards/cards";
import "./donate.scss";

const Donate = () => {
  const [redirect, setRedirect] = useState('');

  const onCardClick = (company) => {
    setRedirect(company);
  }

  if (redirect !== '') {
    return <Redirect to={{
      pathname: '/schedule',
      state: { company: redirect }
    }}/>
  }

  return (
    <div className='spacer'>
      <div className='donate'>
        <h3>Donate</h3>
        <h4>List of Participating Companies</h4>
        <div className='wrapper'>
          {/* {companies.map(c => {
            <Card 
            onClick={() =>{ return(onCardClick(c.name))}}
            title={c.name} 
            description={c.description}
            time={c.materials}
            btn="Select"/>
          })} */}
            <Card 
              onClick={() =>{ return(onCardClick('TerraCycle'))}}
              title='TerraCycle' 
              description='TerraCycle converts the waste into new products, such as park benches or backpacks.' 
              time="Plastics"
              btn="Select"/>
            <Card 
              onClick={() =>{ return(onCardClick('TerraCycle'))}}
              title='Playback' 
              description='Playback clothing creates tees, hoodies, and sweatshirts by transforming trash - plastic bottles and clothing scraps - into eco-clothing!' 
              time="Textiles"
              btn="Select"/>
            <Card 
              onClick={() =>{ return(onCardClick('TerraCycle'))}}
              title='Hipcycle' 
              description='Online retailer Hipcycle, upcycles goods to create home decor, jewelry and fashionp' 
              time="Plastics, books, textiles"
              btn="Select"/>
            <Card 
              onClick={() =>{ return(onCardClick('TerraCycle'))}}
              title='Preserve' 
              description='Preserve is a company that collects recycled goods and makes toothbrushes and kitchenware' 
              time="Plastics, wood, glass"
              btn="Select"/>
        </div>
      </div>
    </div>
      
  );
}

export default Donate; 