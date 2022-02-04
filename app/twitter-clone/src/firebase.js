import firebase from "firebase";

//const firebaseConfig = {
//  apiKey: "AIzaSyCw-li0IscS2rJr68dSjoJL3KM3eFq5PfE",
//  authDomain: "twitter-clone-1faac.firebaseapp.com",
//  databaseURL: "https://twitter-clone-1faac.firebaseio.com",
//  projectId: "twitter-clone-1faac",
//  storageBucket: "twitter-clone-1faac.appspot.com",
//  messagingSenderId: "316208638057",
//  appId: "1:316208638057:web:75a37bf24fab32ff145af8",
//  measurementId: "G-HGFP2LDXP9",
//};

const firebaseConfig = {
  apiKey: "AIzaSyCl-0Hfh4ShjirwpC4TqSqrElipwlbxRNM",
  authDomain: "twitter-clone-2abfe.firebaseapp.com",
  projectId: "twitter-clone-2abfe",
  storageBucket: "twitter-clone-2abfe.appspot.com",
  messagingSenderId: "715981202968",
  appId: "1:715981202968:web:217c544ed027f1295b056d"
};

const firebaseApp = firebase.initializeApp(firebaseConfig);

const db = firebaseApp.firestore();

export default db;
