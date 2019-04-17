import React, { Component } from 'react'
import { connect } from 'react-redux'
import { createPost } from '../../store/modules/collaborate';
import PostWriteTemplate from '../../components/collaborate/PostWriteTemplate';
import { withRouter } from "react-router";

class PostWriteContainer extends Component {
  render() {
    const { createPost } = this.props;
    return (
      <div>
        <PostWriteTemplate createPost={createPost}/>
      </div>
    )
  }
}

export default withRouter(connect(
  () => ({}),
  { createPost }
)(PostWriteContainer));
