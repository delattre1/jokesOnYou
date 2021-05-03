import Joke from "./components/Joke";
import "./App.css";
import axios from "axios";
import { useEffect, useState } from "react";
import React from 'react';
import FavoriteJokes from "./components/FavoriteJokes"

function App() {

  const [notes, setNotes] = useState([]);
  const [favs,  setFavs]  = useState([]);

  useEffect(() => {
    axios
      .get('http://127.0.0.1:8000/api/favorites/')
      .then((res) => {
        setFavs(res.data)
      })
    }, []);


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
        <FavoriteJokes favJokes={favs}></FavoriteJokes>
        <img className="jokeImg" src="/mini-joker.jpg" alt="" />
      </div>   
    </div>
  );
}

export default App;
