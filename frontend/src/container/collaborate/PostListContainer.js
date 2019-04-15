import React, { Component } from 'react'
import PropTypes from 'prop-types'
import { connect } from 'react-redux'
import { getPostList } from '../../store/modules/collaborate'
import PostListTemplate from '../../components/collaborate/PostListTemplate'
import { withRouter } from "react-router";



export class PostListContainer extends Component {
  render() {
    const { postList, getPostList, match } = this.props;
    return (
      <PostListTemplate data={postList}
                    mountEvt={getPostList}
                    page={match.params.pageId}
      />
    )
  }
}


export default withRouter(connect(
  ({ collaborate }) => ( {postList: collaborate} ), 
  { getPostList }
)(PostListContainer));
