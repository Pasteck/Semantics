import './index.css';
import React from 'react';

class Selecter extends React.Component {

  state = {
    stateBox1:false,
    stateBox2:false,
    statecity:'---'
  };


  get_data_by_link = async (link) =>{
    let data =  await window.fetch(link);
    data = await data.json()


    let res = data.body.map(x=>{
      let lu = x.lu.includes('-')?x.lu.split(" ")[0]:new Date(parseInt(x.lu)*1000).toLocaleDateString()
      return {'Name':x.name, 
              'Lat':x.lat, 
              'Long':x.long, 
              'AvailableBikes':x.ab, 
              'AvailableBikesStands':x.abs,
              'Type':x.type,
              'lu':lu,
              'id':x.s.split('#').pop()}
            })
    return res
  }

  select_stations = async (event) =>{
    await this.setState({statecity:event.target.value})
    await this.setState({stateBox1:false})
    await this.setState({stateBox2:false})
    

    var res = this.state.statecity === '---'?[]:await this.get_data_by_link(`/getAllData?city=${this.state.statecity}`)
    
    await this.props.set_stations(res)
    
    if(this.state.statecity !== '---'){
      await this.props.set_center({lat:this.props.stations[0].Lat, lng:this.props.stations[0].Long})
    }
    await this.props.set_copy_stations(this.props.stations)
    await this.props.set_toggle(true)
  }
  

  handleInputChange = async (event) => {
    if(event.target.name === "ab"){
      await this.setState({stateBox1:!this.state.stateBox1})
    }
    else{
      await this.setState({stateBox2:!this.state.stateBox2})
    }

    if(this.state.statecity !== '---' ){
      await this.select_special_stations()
    }
    await this.setState({n:this.props.stations.length})
  }

  select_special_stations = async (type) => {
    var url
    if(this.state.stateBox1 && this.state.stateBox2){
      url = `/getAllFreeStation?city=${this.state.statecity}`
    }
    else if(this.state.stateBox1){
      url = `/getBikeFreeStation?city=${this.state.statecity}`
    }
    else if(this.state.stateBox2){
      url = `/getStandFreeStation?city=${this.state.statecity}`
    }
    else{
      url = `/getAllData?city=${this.state.statecity}`
    }
    let res = await this.get_data_by_link(url)

    await this.props.set_copy_stations(res)
    
    if(!this.props.toggle){
      let list_id = res.map(x=>x.id)
      res = this.props.copy_near.filter(x=>list_id.includes(x.id))
    }
    
    this.props.set_stations(res)

  }

  reload = async () => {
    await window.fetch('/reload_all');
    alert('Ontology loaded !')
  }
 
  render() {
    return (
    <div className='mainselecter'>
      <div className='leftcontainer'>

        <div className='reload' onClick={this.reload}>
          <button className="btn-green"> 
            <img className="icon" alt='Actualise ontologies' src="https://htmlacademy.ru/assets/icons/reload-6x-white.png"/> Reload
          </button>
        </div>

        <select value={this.state.statecity} onChange={this.select_stations}>
          <option>---</option>
          <option>StEtienne</option>
          <option>Paris</option>
          <option>Lyon</option>
        </select>

      </div>
      

      <div className='checkboxs'>
        <div className='box1'>
          <input type="checkbox" id="ab" name="ab" checked={this.state.stateBox1} onChange={this.handleInputChange}/>
          <label>Available bikes</label>
        </div>

        <div className='box2'>
          <input type="checkbox" checked={this.state.stateBox2} onChange={this.handleInputChange} id="as" name="as"/>
          <label>Available stands</label>
        </div>

      </div>
      
      <p className="count">Number of stations: {this.props.stations.length} </p>
    </div>
    )};
}

export default Selecter;
