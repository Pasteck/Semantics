import './index.css';
import React from 'react';
import Station from '../Station/index.js'
function Infodisplayer({stations, set_stations, copy_stations, toggle, set_toggle, set_copy_near}) {

  
  
 
  return (
    <div className='mainDisplayer'>
      {stations.map((x,i)=>( <Station key={i} x={x} set_stations={set_stations} stations={stations}
                                                    toggle={toggle} set_toggle={set_toggle}
                                                    copy_stations={copy_stations} set_copy_near={set_copy_near}/>))}
      
    </div>
  );
}

export default Infodisplayer;
