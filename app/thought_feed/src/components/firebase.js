import { initializeApp } from "firebase";
import { firestore } from "firebase";


const firebaseConfig = {
  apiKey: "AIzaSyCl0YyTsKwsd_NyyJUH6kgo47w67xBiOZI",
  authDomain: "thoughtfeed-44eb6.firebaseapp.com",
  projectId: "thoughtfeed-44eb6",
  storageBucket: "thoughtfeed-44eb6.appspot.com",
  messagingSenderId: "272341376538",
  appId: "1:272341376538:web:9a83bd80e0cb25c283fba3"
};

const firebaseApp = initializeApp(firebaseConfig);

const db = firebaseApp.firestore();

export default db;