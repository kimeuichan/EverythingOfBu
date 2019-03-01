import React, { Component } from 'react'
import './PostList.scss';

export function PostListItem({item}) {
  return (
    <div className="ListItem">
      <div className="item">{item.id}</div>
      <div className="item">{item.title}</div>
      <div className="item">{item.created_time}</div>
    </div>
  )
}

const ls = [
  {
    id : 0,
    title: 'asdfasdfasdfasdfasdfasdfasasdfdasfasdfasdfasdf',
    created_time: '2018-3-3',
  },
  {
    id : 1,
    title: 'test1',
    created_time: '2018-3-3',
  },
  {
    id : 2,
    title: 'test2',
    created_time: '2018-3-3',
  },
];


export default class PostList extends Component {
  render() {
    const list = ls.map(item => 
        <PostListItem item={item} key={item.id}/>
      );
    return (
      <div className="PostList">
        {list}
      </div>
    )
  }
}
