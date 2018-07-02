import React from "react";
import ReactDOM from "react-dom";
import App from "./App.js";
import Header from "./components/header";
import Footer from "./components/footer";

export { Header, Footer };

const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);
