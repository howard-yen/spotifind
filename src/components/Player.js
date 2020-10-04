import React from "react";

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
    <div className="">
      <div className="">
        <div className="album-art">
          <img src={props.item.album.images[0].url} />
        </div>
        <div className="">
          <div className="">{props.item.name}</div>
          <div className="">
            {props.item.artists[0].name}
          </div>
          <div className="">
            {props.is_playing ? "Playing" : "Paused"}
          </div>
          <div className="">
            <div className="" style={progressBarStyles} />
          </div>
        </div>
        <div className="" style={backgroundStyles} />
      </div>
    </div>
  );
}

export default Player;
