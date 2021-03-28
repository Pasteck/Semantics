import './index.css';
import React from 'react';

function Station({x, set_stations, stations, copy_stations, toggle, set_toggle, set_copy_near}) {

  const round = (number, X) => {
    X = (!X ? 3 : X);
    return Math.round(number*Math.pow(10,X))/Math.pow(10,X);
  }


  const compute_d = (lat1, lon1, lat2, lon2 ) => {

    let e = (3.14159265358979*lat1/180); 
    let f = (3.14159265358979*lon1/180); 
    let g = (3.14159265358979*lat2/180);
    let h = (3.14159265358979*lon2/180);
    let i = (Math.cos(e)*Math.cos(g)*Math.cos(f)*Math.cos(h)+Math.cos(e)*Math.sin(f)*Math.cos(g)*Math.sin(h)+Math.sin(e)*Math.sin(g)); 
    let j = (Math.acos(i));
    let d = round(6371*j*1000);
    return d

    }


  const handleSelect = (event) =>{  
    if(toggle){
      let res = stations.filter(y=>compute_d(x.Lat, x.Long, y.Lat, y.Long )<=300)
      set_stations(res)
      set_copy_near(res)
    }
    else{
     set_stations(copy_stations)
    }
   set_toggle(!toggle)
  }
 
  return (
    <div className='mainStation' onClick={handleSelect}>
        <h2>{x.Name}</h2>
        <p>Lat: {x.Lat} | Long: {x.Long}</p>
        <p>Available bikes: {x.AvailableBikes} | Available places: {x.AvailableBikesStands}</p>
        <i>Last update: {x.lu}</i>
    </div>
  );
}

export default Station;
