import React, { Component } from "react";

class Main extends Component {
  constructor(props) {
    super(props);
    this.state = {
      nearby: [],
    };
    this.tick = this.tick.bind(this);
  }

  componentDidMount() {
    this.interval = setInterval(() => this.tick(), 5000);
  }

  componentWillUnmount(props) {
    clearInterval(this.interval);
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
      <div>
      {JSON.stringify(this.props.item)}
      </div>
    )
  }
}

export default Main;
