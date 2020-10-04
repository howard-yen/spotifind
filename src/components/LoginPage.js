import React from "react";
import Login from "./Login";
import catJAM from "../Assets/catJAM.gif";

const LoginPage = props => {
  return (
    <div className="container">
      <div className="login-page h-100 row">
        <div className="col" />
        <div className="col d-flex align-items-center">
          <div className="card login-container">
            <div id="welcome">
              Welcome to Spotifind!
            </div>
            <div className="description">
              Need some new tracks for your mixtape?
            </div>
            <img id="catjam" src={catJAM} alt="loading..." />
            <div className="description">
              Discover music based on what people are listening to nearby!
            </div>
            <Login />
          </div>
        </div>
        <div className="col" />
      </div>
    </div>
  )
}

export default LoginPage;
