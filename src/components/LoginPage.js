import React from "react";
import Login from "./Login";

const LoginPage = props => {
  return (
    <div className="login-page h-100 row">
      <div className="col" />
      <div className="col d-flex align-items-center">
        <div className="login-container">
          <div id="welcome">
            Welcome to XDDDd!
          </div>
          <div id="description">
            lorem ipsum asjidkhasdkjahksdjhdkajshdajk
          </div>
          <Login />
        </div>
      </div>
      <div className="col" />
    </div>
  )
}

export default LoginPage;
