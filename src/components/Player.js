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
    <div className="card player">
      <div className="">
        <div className="card-img-top">
          <img className="album-art" src={props.item.album.images[0].url} />
        </div>
        <div className="card-body">
          <div className="card-title">{props.item.name}</div>
          <div className="card-text">
            {`${props.item.artists[0].name} - ${props.item.album.name}`}
          </div>
          <div className="btn-container">
            <a
              className="card-btn btn btn-success"
              href={props.item.uri}
            >
              Play
            </a>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Player;
