import React, { Component } from 'react'
import axios from 'axios';

const PostView = ({data: {title, description, writter, created_time, isAlive, members, id} }) => {
  return (
    <div className="ListItem">
       <div className="item">{id}</div>
       <div className="item">{title}</div>
      <div className="item">{created_time}</div>
     </div>
  );
}

export default PostView;


// export function PostView({item}) {
//   return (
//     <div className="ListItem">
//       <div className="item">{item.id}</div>
//       <div className="item">{item.title}</div>
//       <div className="item">{item.created_time}</div>
//     </div>
//   )
// }