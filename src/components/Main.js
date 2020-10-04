import React, { Component } from "react";
import io from "socket.io-client";
import Player from "./Player";

const ENDPOINT = "http://127.0.0.1:5000";

class Main extends Component {
  constructor(props) {
    super(props);
    this.state = {
      nearby: [],
      response: [],
    };
    this.tick = this.tick.bind(this);
  }

  componentDidMount() {
    this.socket = io.connect(ENDPOINT, {
      reconnection: true,
    });
    this.socket.on("update", data => {
      this.setState({ response: data });
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

  render() {
    return (
      <div className="outer-container h-100 row justify-content-center">
        <div className="">
            <Player item={this.props.item} />
            <div className="card">
              {JSON.stringify(this.state.response)}
            </div>
        </div>
      </div>
    )
  }
}

export default Main;
