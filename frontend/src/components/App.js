import React, { Component } from "react";
import { createRoot } from "react-dom/client";

export default class App extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div>
                <h1>Hello World</h1>
            </div>
        );
    }
}

const container = document.getElementById("app");
const root = createRoot(container);
root.render(<App />);