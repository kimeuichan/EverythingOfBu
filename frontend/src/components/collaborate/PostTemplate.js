import React, { Component, Fragment } from 'react'
import { Header } from '../common/Header';
import PostList from './PostList';
import { Link } from 'react-router-dom';

export default class PostTemplate extends Component {
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
    const list = data.data.results;
    return (
      <Fragment>
        <PostList list={list}/>
        <Link to={'/collaborate/' + (parseInt(page) - 1) }>&lt;</Link>
        {page}
        <Link to={'/collaborate/' + (parseInt(page) + 1) }>&gt;</Link>
      </Fragment>
    )
  }
}

PostTemplate.defaultProps = {
  page: 1,
};
