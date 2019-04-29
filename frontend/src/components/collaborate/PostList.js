import React, { Component } from 'react'
import { Link } from 'react-router-dom';
import './PostList.scss';

export function PostListItem({item}) {
  return (
    <Link to={"/collaborate/post/" + item.id}>
      <div className="ListItem">
        <div className="item">{item.id}</div>
        <div className="item">{item.title}</div>
        <div className="item">{item.created_time}</div>
      </div>
    </Link>
  )
}


export default class PostList extends Component {
  render() {
    const { list } = this.props;
    const post = list.map(item => 
        <PostListItem item={item} key={item.id}/>
      );
    return (
      <div className="PostList">
        {post}
      </div>
    )
  }
}
