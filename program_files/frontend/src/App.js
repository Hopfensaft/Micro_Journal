import React from "react";
import { Header, Footer } from "./";
import JournalEntries from "./components";

export default class extends React.Component {
  render() {
    return (
      <React.Fragment>
        <Header />
        <JournalEntries />
        <h1> Hello </h1>
        <Footer />
      </React.Fragment>
    );
  }
}
