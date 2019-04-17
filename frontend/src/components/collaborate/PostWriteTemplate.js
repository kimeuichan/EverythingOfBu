import React, { Component } from 'react'
import PostWrite from './PostWrite';

export default class PostWriteTemplate extends Component {
  render() {
    const { createPost } = this.props;
    return (
      <div>
        <PostWrite createPost={createPost}/>
      </div>
    )
  }
}
