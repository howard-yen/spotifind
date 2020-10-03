import React, { Component } from "react";
import * as $ from "jquery";
import hash from "../services/hash";
import Main from "./Main";
import Login from "./Login";
import LoginPage from "./LoginPage";
import Player from "./Player";

class Home extends Component {
  constructor() {
    super();
    this.state = {
      token: null,
      item: {
        album: {
          images: [{ url: "" }]
        },
        name: "",
        artists: [{ name: "" }],
        duration_ms: 0
      },
      is_playing: "Paused",
      progress_ms: 0,
      no_data: false,
    };

    this.getCurrentlyPlaying = this.getCurrentlyPlaying.bind(this);
    this.tick = this.tick.bind(this);
  }

  componentDidMount() {
    let _token = hash.access_token;

    if (_token) {
      this.setState({
        token: _token
      });
      this.getCurrentlyPlaying(_token);
    }

    this.interval = setInterval(() => this.tick(), 5000);
  }

  componentWillUnmount() {
    clearInterval(this.interval);
  }

  componentDidUpdate() {
    console.log(this);
  }

  tick() {
    if(this.state.token) {
      this.getCurrentlyPlaying(this.state.token);
    }
  }

  getCurrentlyPlaying(token) {
    $.ajax({
      url: "https://api.spotify.com/v1/me/player",
      type: "GET",
      beforeSend: xhr => {
        xhr.setRequestHeader("Authorization", "Bearer " + token);
      },
      success: data => {
        if(!data) {
          this.setState({
            no_data: true,
          });
          return;
        }

        console.log(data);

        this.setState({
          item: data.item,
          no_data: false /* We need to "reset" the boolean, in case the
                            user does not give F5 and has opened his Spotify. */
        });
      }
    });
  }

  render() {
    return (
      <div className="home">
        <div className="main-page container">
          {/* Not logged in */ }
          {!this.state.token && (
            <LoginPage />
          )}

          {/* Logged in */}
          {this.state.token && (
            <Main
              item={this.state.item}
              token={this.state.token}
            />
          )}
        </div>
      </div>
    );
  }
}

export default Home;

