import React from "react";
import "./index.css";
import { Button  } from 'reactstrap';

export default function Joke(props) {
    return (
    <div className="containerMainJoke">
      <div className="card">
        <h3 className="card-title">{props.title}</h3>
        <div className="card-content">{props.children}</div>
      </div>
      <Button outline color="blue">Save Joke</Button>
    </div>
    );
}

