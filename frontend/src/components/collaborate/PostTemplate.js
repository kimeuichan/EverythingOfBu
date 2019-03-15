import React, { Component, Fragment } from 'react'
import { Header } from '../common/Header';
import PostList from './PostList';

export default class PostTemplate extends Component {

  componentDidMount = () => {
    const {mountEvt} = this.props;
    mountEvt();
  }

  render() {
    const { data } = this.props;
    const list = data.data.results;
    return (
      <PostList list={list}/>
    )
  }
}
