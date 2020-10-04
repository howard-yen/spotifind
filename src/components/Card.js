import React from "react";
import Default from "../Assets/default.png";

const Card = props => {
  return (
    <div className="card rec-card">
      <div className="">
        <div className="card-img-top">
          {props.data.image.url ?
          <img className="album-art" src={props.data.image.url} alt="" /> :
          <img className="album-art" src={Default} alt="" />
          }
        </div>
        <div className="card-body">
          <div className="card-title">{props.data.albumname}</div>
          <div className="card-text">
            {props.data.artist}
          </div>
          <div className="btn-container">
            <a
              className="card-btn btn btn-success"
              href={props.data.uri}
            >
              Play
            </a>
            <a
              className="card-btn btn btn-success"
              href={props.data.url}
            >
              Link
            </a>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Card;
