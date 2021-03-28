import React from 'react';
import { GoogleMap, Marker, InfoWindow, TrafficLayer} from "react-google-maps";


class Map extends React.Component {

  state={
    selected:null
  }

  

  render() {
    return (
      <div>
        <GoogleMap defaultZoom={12} defaultCenter={this.props.center} center={this.props.center}>
            {this.props.stations.map(s => (
                <Marker
                  key={s.id}
                  position={{
                    lat: s.Lat,
                    lng: s.Long
                  }}
                  icon={{
                    url: `/marker.png`,
                    scaledSize: new window.google.maps.Size(25, 25)
                  }}
                  onClick={async () => {await this.setState({selected:s}); }}
                />
             ))}

              {this.state.selected!=null && (
              <InfoWindow
                onCloseClick={async() => {await this.setState({selected:null});}}
                position={{
                  lat: this.state.selected.Lat,
                  lng: this.state.selected.Long
                }}
              >
                <div>
                  <h2>{this.state.selected.Name}</h2>
                  <p>AvailableBikes: {this.state.selected.AvailableBikes}</p>
                  <p>AvailableBikesStands: {this.state.selected.AvailableBikesStands}</p>
                  <i>Last update: {this.state.selected.lu}</i>
                </div>
              </InfoWindow>
            )}
            <TrafficLayer autoUpdate />
        </GoogleMap>

      </div>
      
    )
  };
}

export default Map;
