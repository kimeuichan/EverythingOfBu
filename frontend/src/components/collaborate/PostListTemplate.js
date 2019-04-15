import React, { Component, Fragment } from 'react'
import PostList from './PostList';
import { Link } from 'react-router-dom';
import PostWriteButton from '../base/PostWriteButton';

export default class PostListTemplate extends Component {
  componentDidMount = () => {
    const { mountEvt, page } = this.props;
    mountEvt(page);
  }

  componentWillReceiveProps(nextProps) {
    const { mountEvt, page } = this.props;
    if(nextProps.page != page)
      mountEvt(nextProps.page);
  }

  render() {
    const { data, page } = this.props;
    const list = data.postList;
    console.log(list);
    return (
      <Fragment>
        { data.error && <h1>Error Occur</h1> }
        { data.pending && <h1>Wait a minutes</h1> }
        <PostList list={list}/>
        <PostWriteButton toUrl="/collaborate/post" />
        <Link to={'/collaborate/posts/' + (parseInt(page) - 1) }>&lt;</Link>
        {page}
        <Link to={'/collaborate/posts/' + (parseInt(page) + 1) }>&gt;</Link>
      </Fragment>
    )
  }
}

PostListTemplate.defaultProps = {
  page: 1,
};
