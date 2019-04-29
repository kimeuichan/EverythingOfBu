import React, { Component } from 'react'
import RoomList from './RoomList';
import { Link } from 'react-router-dom';

export default class RoomListTemplate extends Component {
  componentDidMount() {
    const { mountEvt, page } = this.props;
    mountEvt(page);
  }

  componentWillReceiveProps(nextProps) {
    const { mountEvt, page } = this.props;
    if(nextProps.page !== page)
      mountEvt(nextProps.page);
  }
  
  render() {
    const { data, page } = this.props;
    return (
      <div>
        <RoomList list={data} />
        <Link to={"/room/" + page - 1}>&lt;</Link>
        { page }
        <Link to={"/room/" + page + 1}>&gt;</Link>
      </div>
    )
  }
};


RoomListTemplate.deafultProps = {
  page: 1,
};
