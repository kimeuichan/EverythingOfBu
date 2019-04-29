import React, { Component } from 'react'
import { connect } from 'react-redux'
import { withRouter } from 'react-router-dom';

export class RoomListContainer extends Component {
  static propTypes = {
    prop: PropTypes
  }

  render() {
    return (
      <div>
        
      </div>
    )
  }
}


export default withRouter(
  connect(mapStateToProps, mapDispatchToProps)(RoomListContainer));
