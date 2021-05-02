import Joke from "./components/Joke";
import "./App.css";
import axios from "axios";
import { useEffect, useState } from "react";
import React from 'react';
import { Button } from 'reactstrap';

function App() {
  const [notes, setNotes] = useState([]);

  useEffect(() => {
    axios
      .get("http://localhost:8000/api/joke/")
      .then((res) => setNotes(res.data));
  }, []);

  console.log(notes);

  return (
    <div className="App">
        <div className="appbar">
            <img className="logo_joker" src="/logo_joker.png" alt="" />
            <p className="top-bar-text">Timão piadas mesmo!</p>
        </div>

      <div className="mainContainer">
        <Joke title={notes.setup}>{notes.delivery}</Joke>
        <Button outline color="primary">Save Joke</Button>
        <img className="jokeImg" src="/mini-joker.jpg" alt="" />
      </div>   

    </div>
  );
}

export default App;
