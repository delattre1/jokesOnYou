import Joke from "./components/Joke";
import "./App.css";
import axios from "axios";
import { useEffect, useState } from "react";

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
        <div class="appbar">
            <img className="logo_joker" src="/logo_joker.png" alt="" />
            <p class="top-bar-text">Timão piadas mesmo!</p>
        </div>

      <div className="mainContainer">
        <Joke title={notes.setup}>{notes.delivery}</Joke>
        <img className="jokeImg" src="/mini-joker.jpg" alt="" />
      </div>   
    </div>
  );
}

export default App;
