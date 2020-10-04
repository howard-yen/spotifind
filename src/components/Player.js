import React from "react";
import defaultImage from "../Assets/default.png";

const Player = props => {
  const backgroundStyles = {
    backgroundImage:`url(${
      props.item.album.images[0].url
    })`,
  };

  const progressBarStyles = {
    width: (props.progress_ms * 100 / props.item.duration_ms) + '%'
  };

  return (
    <div className="card player">
      <div className="">
        <div className="card-img-top">
          {props.item.album.images[0].url !== "" ?
            <img className="album-art" src={props.item.album.images[0].url} /> :
            <img className="album-art" src={defaultImage} />
          }
        </div>
        <div className="card-body">
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
