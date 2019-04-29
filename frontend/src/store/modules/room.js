import { handleActions } from 'redux-actions';
import { API_SERVER } from '../../settings';
import client from '../../lib/ApiClient';


const GetRoomList = page => {
  return client.get(`${API_SERVER}/api/room?page=${page}`)
}

const GetRoom = roomId => {
  return client.get(`${API_SERVER}/api/room/${roomId}`)
}

const CreateRoom = (data) => {
  return client.post(`${API_SERVER}/api/room`, data);
}

const GET_LIST = 'GET_LIST';
const GET_LIST_PENDING = 'GET_LIST_PENDING';
const GET_LIST_SUCCESS = 'GET_LIST_SUCCESS';
const GET_LIST_FAILURE = 'GET_LIST_FAILURE';

const GET_ROOM = 'GET_ROOM';
const GET_ROOM_PENDING = 'GET_ROOM_PENDING';
const GET_ROOM_SUCCESS = 'GET_ROOM_SUCCESS';
const GET_ROOM_FAILURE = 'GET_ROOM_FAILURE';

const WRITE_POST = 'WRITE_POST';
const WRITE_POST_PENDING = 'WRITE_POST_PENDING';
const WRITE_POST_SUCCESS = 'WRITE_POST_SUCCESS';
const WRITE_POST_FAILURE = 'WRITE_POST_FAILURE';

export const getRoomListAPI = (page) => ({
  type: GET_LIST,
  payload: GetRoomList(page),
});

export const getRoomAPI = (roomId) => ({
  type: GET_ROOM,
  payload: GetRoom(roomId),
});


const initState = {
  roomList: [],
  pending: false,
  error: false,
};

export default handleActions({
  [GET_LIST_SUCCESS]: (state, action) => {
    return {
      roomList: action.payload.data.results,
      pending: false,
      error: false,
    };
  },
  [GET_LIST_PENDING]: (state, action) => {
    return {
      roomList: [],
      pending: true,
      error: false,
    };
  },
  [GET_LIST_FAILURE]: (state, action) => {
    return {
      roomList: [],
      pending: false,
      error: false,
    };
  },
  [GET_ROOM_SUCCESS]: (state, action) => {
    return {
      
    }
  },
  [GET_ROOM_PENDING]: (state, action) => {

  },
  [GET_ROOM_FAILURE]: (state, action) => {

  },
}, initState);