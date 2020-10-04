import React, { Component } from "react";
import io from "socket.io-client";
import Player from "./Player";
import Card from "./Card";

const PORT = process.env.PORT || 5000;
const ENDPOINT = `https://ivyhacks-spotifind.herokuapp.com`;

class Main extends Component {
  constructor(props) {
    super(props);
    this.state = {
      nearby: [],
    };
    this.tick = this.tick.bind(this);
  }

  componentDidMount() {
    this.socket = io.connect(ENDPOINT, {
      reconnection: true,
    });
    this.socket.on("update", data => {
      console.log(data);
      this.setState({ nearby: data });
    });
    this.socket.emit('new user', this.props.token);
    this.interval = setInterval(() => this.tick(), 5000);
    this.tick();
  }

  componentWillUnmount(props) {
    clearInterval(this.interval);
    this.socket.disconnect();
  }

  tick() {
    if("geolocation" in navigator) {
      navigator.geolocation.getCurrentPosition(async pos => {
        let coords = {lat: pos.coords.latitude, lon: pos.coords.longitude};
        await this.socket.emit('update ping', coords);
      });
    } else {
      console.log("called");
      this.socket.emit('update ping', {});
    }
    /* if(this.props.item) {
      const requestOptions = {
        method : 'POST',
        headers: { 'Content-Type' : 'application/json'},
        body: JSON.stringify(this.props.item)
      }

      // Send POST request and then update states in App.js
      fetch('/endpoint', requestOptions)
        .then(res => res.json())
        .then(res => {
            props.setSentiment(res.sentiment);
          props.setVerdict(res.verdict);
            props.setKeywords(res.keywords);
            props.setSentences(res.worstSentence.map((sentence, i) => {
              return [sentence, res.worstScore[i]];
          }).filter((item) => item[0] !== ''));
          console.log("success")
      });
    }*/
  }
  /*
          <div className="card">
            {JSON.stringify(this.state.response)}
          </div>
  */
  render() {
    return (
      <div className="outer-container">
        <div className="row">
          <div className="col-sm-4 h-100 d-flex justify-content-center">
            <Player item={this.props.item} />
          </div>
          <div className="col-sm-8 h-100 d-flex justify-content-center">
            <div className="card-columns">
              {this.state.nearby.map(data => {
                return (
                  <Card data={data} />
                );
              })}
            </div>
          </div>
        </div>
      </div>
    )
  }
}

export default Main;
