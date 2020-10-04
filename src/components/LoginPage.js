import React from "react";
import Login from "./Login";
import logo from "../Assets/icon_color.svg";
import catJAM from "../Assets/catJAM.gif";

const LoginPage = props => {
  return (
    <div className="container">
      <div className="login-page h-100 row">
        <div className="col" />
        <div className="col d-flex align-items-center">
          <div className="card login-container">
            <div logo="logo">
            </div>
            <div id="welcome">
              Welcome to Spotifind!
            </div>
            <div className="description">
              Need some new tracks for your mixtape?
            </div>
              <img src={logo} alt="" />
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
