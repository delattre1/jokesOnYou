import React, {Component, useState, useEffect} from "react";
import axios from "axios";

export default function HomePage(props) {
    const [joke, setJoke] = useState([]);
    useEffect(() => {
    axios
      .get("https://cat-fact.herokuapp.com/facts/random")
      .then((res) => setJoke(res.data.text));
    }, []);


    return (
        <h1> YAUU page HEHEHE {joke} </h1>
    );
}

