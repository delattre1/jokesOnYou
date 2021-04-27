import React, {Component, useState, useEffect} from "react";
import axios from "axios";
import ClipLoader from "react-spinners/ClipLoader";

export default function JokeContainer(props) {
    const [joke, setJoke] = useState([]);
    const [loading, setLoading] = useState(false);

    useEffect(() => {
        axios
          .get("http://localhost:8000/api/joke")
                .then((res) => {
                    setJoke(res.data)
                });
        setLoading(true);
    }, []);

    return (
        <div className="jokeContainer">
            <ClipLoader loading={loading} size={150} />
            <h1> {joke.setup} </h1>
            <h1> {joke.delivery} </h1>
            <img className="jokeImg" src="../../static/images/mini-joker.jpg" />
        </div>
    );
}
