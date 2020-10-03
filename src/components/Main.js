import React, { Component } from "react";
import socketIOClient from "socket.io-client";
const ENDPOINT = "http://127.0.0.1:4001";

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
    this.interval = setInterval(() => this.tick(), 5000);
    this.socket = socketIOClient(ENDPOINT);
    this.socket.on("update", data => {
      console.log(data);
      this.setState({ response: data });
    });
    this.socket.emit('new user', this.props.token);
  }

  componentWillUnmount(props) {
    clearInterval(this.interval);
    this.socket.disconnect();
  }

  tick() {
    if(this.props.item) {
      const requestOptions = {
        method : 'POST',
        headers: { 'Content-Type' : 'application/json'},
        body: JSON.stringify(this.props.item)
      }

      // Send POST request and then update states in App.js
      fetch('/endpoint', requestOptions)
        .then(res => res.json())
        .then(res => {
          /*
            props.setSentiment(res.sentiment);
            props.setVerdict(res.verdict);
            props.setKeywords(res.keywords);
            props.setSentences(res.worstSentence.map((sentence, i) => {
              return [sentence, res.worstScore[i]];
          }).filter((item) => item[0] !== ''));
          */
          console.log("success")
      });
    }
  }

  render() {
    return (
      <div className="h-100 row">
        <div className="col d-flex align-items-center">
          <div className="card">
            {JSON.stringify(this.state.response)}
          </div>
        </div>
      </div>
    )
  }
}

export default Main;
