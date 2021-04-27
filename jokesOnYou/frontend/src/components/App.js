import React, {Component} from "react";
import {render} from "react-dom";
import HomePage from "./HomePage";
import TopBar from "./TopBar";

export default class App extends Component {
    constructor(props) {
        super(props);
    }
    render() {
        return (
            <div className="center">
                <TopBar />
                <HomePage />
            </div>
        );
    }
}

const appDiv = document.getElementById('app');
render(<App name="dani"/>, appDiv);
