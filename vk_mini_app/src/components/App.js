import React, { Component } from "react";
import { render } from "react-dom";


class App extends Component {

  render() {
    return (
        <div>
          <button onClick={this.click}>Click</button>
        </div>
    );
  }

  click() {
    console.log('click111');
    fetch('api/click', {credentials: "include"});
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);