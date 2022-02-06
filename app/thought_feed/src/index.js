import React , {Component} from "react";
import Feed from "./components/Feed";
import "./components/App.css";
import ReactDOM,{render} from 'react-dom';
// import axios from 'axios';

export default class App extends Component {
  constructor(props) {
    super(props);
  }

   render() {
    return (
      <div >
      <Feed />
    </div>
    );
  }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);

