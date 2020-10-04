import React from "react";
import defaultImage from "../Assets/default.png";

const Player = props => {

  return (
    <div className="card player">
      <div className="">
        <div className="card-img-top">
          {props.item.album.images[0].url !== "" ?
            <img className="album-art" src={props.item.album.images[0].url} alt="" /> :
            <img className="album-art" src={defaultImage} alt="" />
          }
        </div>
        <div className="card-body">
          <div className="card-title">NOW PLAYING</div>
          <div className="card-title">{props.item.name}</div>
          <div className="card-text">
            {props.item.artists[0].name !== "" ?
            `${props.item.artists[0].name} - ${props.item.album.name}` :
            `No music current playing`
            }
          </div>
        </div>
      </div>
    </div>
  );
}

export default Player;
