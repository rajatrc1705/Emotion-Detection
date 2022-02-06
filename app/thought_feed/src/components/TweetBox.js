import React, { useState } from "react";
import "./TweetBox.css";
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import db from "./firebase";
import Details from "./Details";

function TweetBox() {
  const [tweetMessage, setTweetMessage] = useState("");
  const [tweetImage, setTweetImage] = useState("");
  const data=Details();

  const sendTweet = (e) => {
    e.preventDefault();
    if(tweetMessage.length!=0||tweetImage.length!=0)
    {
      db.collection("posts").add({
        displayName: data.name,
        username: data.name,
        verified: true,
        text: tweetMessage,
        image: tweetImage,
        avatar:
          "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQzH6TfTtq91hzmeIvm_4JOdb5y1UWjTlYZdA&usqp=CAU",
      });
  
      setTweetMessage("");
      setTweetImage("");
    }
    
  };

  return (
    <div className="tweetBox">
      <form>
        <div className="tweetBox__input">
          <Avatar src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQzH6TfTtq91hzmeIvm_4JOdb5y1UWjTlYZdA&usqp=CAU" />
          <input
            onChange={(e) => setTweetMessage(e.target.value)}
            value={tweetMessage}
            placeholder="What's happening?"
            type="text"
            autoFocus="True"
          />
        </div>
        <input
          value={tweetImage}
          onChange={(e) => setTweetImage(e.target.value)}
          className="tweetBox__imageInput"
          placeholder="Optional: Enter image URL"
          type="text"
        />

        <Button
          onClick={sendTweet}
          type="submit"
          className="tweetBox__tweetButton"
        >
         <div>Tweet</div>
        </Button>
      </form>
    </div>
  );
}

export default TweetBox;
