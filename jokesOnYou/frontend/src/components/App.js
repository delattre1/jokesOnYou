import React, {Component} from "react";
import {render} from "react-dom";
import HomePage from "./HomePage";
import TopBar from "./TopBar";
import JokeContainer from "./JokeContainer";


export default class App extends Component {
    constructor(props) {
        super(props);
    }
    render() {
        return (
            <div >
                <TopBar />
                <JokeContainer />
            </div>
        );
    }
}

const appDiv = document.getElementById('app');
render(<App name="dani"/>, appDiv);
