import React, { Component } from 'react'
import PropTypes from 'prop-types'
import { connect } from 'react-redux'
import { getPostList } from '../../store/modules/collaborate'
import PostTemplate from '../../components/collaborate/PostTemplate'


export class PostListContainer extends Component {
  render() {
    const { getPostList, postList } = this.props;
    return (
      <PostTemplate mountEvt={getPostList} data={postList}/>
    )
  }
}


export default connect(
  ({ collaborate }) => ( {postList: collaborate} ), 
  { getPostList }
)(PostListContainer);
