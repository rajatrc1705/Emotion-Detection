import React from "react";
import Sidebar from "./Sidebar";
import Feed from "./Feed";
import "./App.css";
// import axios from 'axios';

function App() {
  return (
    // BEM
    <div className="app">
      <Feed />
    </div>
  );
}
// class App extends React.Component {
  
//   state = {
//       name : '',
//   }
  
//   componentDidMount() {

//       axios.get('http://localhost:8000/wel/')
//       .then(res => {
//           this.setState({
//               name : res.data.name    
//           });
          
//       })
//       .catch(err => {})
      
//   }

// render() {
//   return(
//     <div>
//        <h1>{this.state.name}</h1> 
//     </div>
//     );
// }
// }

export default App;
