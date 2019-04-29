import React, { Component } from 'react'

const RoomListItem = ({}) => {
  return (
    <div>

    </div>
  );
}


export default class RoomList extends Component {
  render() {
    const { items } = this.props;
    const list = items.maps( item => 
      <RoomListItem key={item.id} />
    );
    return (
      <div>
        {list}
      </div>
    )
  }
}
