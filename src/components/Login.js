import React from "react";
import { authEndpoint, clientId, redirectUri, scopes } from "../services/config";

const Login = props => {
  return (
    <a
      className="btn btn-primary"
      href={`${authEndpoint}?client_id=${clientId}&redirect_uri=${redirectUri}&scope=${scopes.join(
        "%20"
      )}&response_type=token&show_dialog=true`}
    >
      Login to Spotify
    </a>
  )
}

export default Login;
