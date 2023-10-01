import './App.css';
import leftIcon from './assets/chevron-left-svgrepo-com.svg'
import rightIcon from './assets/chevron-right-svgrepo-com.svg'

import { useEffect, useState } from 'react';
import axios from 'axios';

import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Button from 'react-bootstrap/Button';


import Header from './components/header'
import Columns from './components/columns'
import Tasks from './components/tasks';
import AddTask from './components/addTask';

const tg = window.Telegram.WebApp;

function App() {
  const [stateTasksName, setStateTasksName] = useState(["Сделать", "В работе", "Закрыто", "Готово"]);
  // const [stateTaskName, setStateTaskName] = useState("Сделать");
  const [stateColumns, setStateColumns] = useState([]);
  // const [stateColumn, setStateColumn] = useState("");
  const [updateTasks, setUpdateTasks] = useState("");

  const [comments, setComments] = useState([]);

  const [tasks, setTasks] = useState([]);

  const [index, setIndex] = useState(0);

  const [addTaskShow, setAddTaskShow] = useState(false);

  const [forBoardId, setForBoardId] = useState('');

  const [loading, setLoading] = useState(true);

  const addTaskHandleShow = () => setAddTaskShow(true);
  const addTaskHandleClose = () => setAddTaskShow(false);

  const [projectId, setProjectId] = useState('');
  const [spaceId, setSpaceId] = useState('');
  const [spaceUsers, setSpaceUsers] = useState([]);
  const USER_ID = tg.initDataUnsafe.user.id;

  const getProjectIdFromBoard = (boardId) => {
    axios.get(`https://global-inno-hack-dd509ac0d0a4.herokuapp.com/board/${boardId}`,
    {params:{
      user_id: USER_ID
    }})
      .then(resp=>{
        setProjectId(resp.data.projectId)
        if(data.data.hasOwnProperty('spaceId')){
          setSpaceId(resp.data.spaceId)
        }
      })
      .catch(e=>{
        console.log(e)
      })
  }

  const getUsersFromSpace = (space_id) => {
    axios.get(`https://global-inno-hack-dd509ac0d0a4.herokuapp.com/spaces/${space_id}`, {params:{
      user_id: USER_ID
    }})
      .then(resp=>{
        setSpaceUsers(resp.data.users)
        
      })
      .catch(e=>{
        console.log(e)
      })
  }

  const getUsersNames = (flame_user_id) => {
    axios.get(`https://global-inno-hack-dd509ac0d0a4.herokuapp.com/users/${flame_user_id}`, {params:{
      user_id: USER_ID
    }})
      .then(resp=>{
        console.log(resp)
      })
      .catch(e=>{
        console.log(e)
      })
  }

  const getColumns = (prjId) => {
    axios.get(`https://global-inno-hack-dd509ac0d0a4.herokuapp.com/board/boardsByProject/${prjId}`,
    {params: {
      user_id: USER_ID
    }})
      .then(data=>{
        // if(data.data.hasOwnProperty('spaceId')){
        //   setSpaceId(data.data.spaceId)
        // }

        // data.data.map((val, i)=>{
        //   if(data.data[i].boardId == forBoardId){
        //     setSpaceId(data.data[i].spaceId)
        //     setStateColumns(data.data[i].columns)
        //     setLoading(false)
        //   })

            // setSpaceId(data.data[0].spaceId)
            setStateColumns(data.data[0].columns)
            setLoading(false)
        
        
      })
      .catch(e => {
        console.log(e)
      })
  }

  const getTasksFromColumn = (column_id) => {
    axios.get(`https://global-inno-hack-dd509ac0d0a4.herokuapp.com/tasks/getTasksByColumn/${column_id}`,
    {params:{
      user_id: USER_ID
    }})
      .then(data=>{
        
        if(data.data.hasOwnProperty('spaceId')){
          setSpaceId(data.data.spaceId)
        }
        // console.log(data)
        let column_names = [];
        let comments = [];

        data.data.map((col, i) => {
          column_names.push({"name": col.name, "task_num": col.taskNumber, "task_id": col.id,
                            "author": col.creator.firstName + ' ' + col.creator.lastName,
                            "description": col?.description})
          comments.push(col.comments);
        })
        console.log(comments)
        setComments(comments)
        setTasks(column_names)

        setLoading(false)
      })
      .catch(e=>{
        console.log(e)
      })
  }

  const getBoardId = () => {
    axios.get("https://global-inno-hack-dd509ac0d0a4.herokuapp.com/board/boardsByUser", {
      params:{
        user_id: USER_ID
      }
    })
      .then(response=>{
        setForBoardId(response.data)
      })
      .catch(e=>{
        console.log(e)
      })
  }

  useEffect(() => {
      tg.ready();
      getBoardId();
  }, []);

  useEffect(()=>{
    getProjectIdFromBoard(forBoardId)
  }, [forBoardId])

  useEffect(()=>{
    setLoading(true)
    getColumns(projectId);
  }, [projectId])

  useEffect(()=>{
    getUsersFromSpace(spaceId)
  }, [spaceId])

  useEffect(() => {  
    setLoading(true)
      getTasksFromColumn(stateColumns[index])
    
  }, [index, stateColumns, updateTasks])

  
  const checkUpdate = (index)=>{
    setUpdateTasks(index)
  }

  const nextStateTask = () => {
    setTasks([]);
    if(index < stateColumns.length - 1){
      setIndex(index + 1);
    }
    else{
      setIndex(0);
    }
  }

  const prevStateTask = () => {
    setTasks([]);
    if(index > 0){
      setIndex(index - 1);
    }
    else{
      setIndex(stateColumns.length - 1);
    }
  }

  return (
    <div className="App">
      <Header></Header>
     <Container>
      {/* {forBoardId} */}
      <Row className=''>
        <Col >
          <a onClick={prevStateTask}>
            <svg width="50" height="50" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <rect width="24" height="24" fill="none"/>
            <path d="M14.5 17L9.5 12L14.5 7" stroke={tg.themeParams.text_color} stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </a>
        </Col>
        <Col xs={7}>
          <Columns
            TaskName={stateTasksName[index].toUpperCase()}
          />
        </Col>
        <Col>
          <a onClick={nextStateTask}>
          <svg width="50" height="50" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <rect width="24" height="24" fill="none"/>
          <path d="M9.5 7L14.5 12L9.5 17" stroke={tg.themeParams.text_color} stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
          </a>
        </Col>
      </Row>
      
      {tasks.length > 0 ? tasks.map((val, i) => {
        return (
          <Row className='mt-2' key={i}>
                <Col>
                  <Tasks
                    title={val.task_num}
                    task={val.name}
                    task_id={val.task_id}
                    task_desc={val.description}
                    statuses={stateTasksName}
                    status={stateTasksName[index]}
                    comments={comments[i]}
                    columns_id={stateColumns}
                    author={val.author}

                    checkUpdate={checkUpdate}
                  />
                </Col>
            </Row>
        )
      }) : loading ?
      
      // <Container >
      
        <Row style={{marginLeft: '40%', marginTop:'40%'}}>
          <Col>
            <div className="spinner-border" role="status"></div>
          </Col>
        </Row>
        // </Container>
        : <Row><Col><h3>Нет задач</h3></Col></Row>
      }
      
      <Row className='position-fixed' style={{bottom:35, right:35}}>
        <a onClick={addTaskHandleShow}>
          <svg width="50" height="50" viewBox="0 0 24 24" fill="#855fef" xmlns="http://www.w3.org/2000/svg">
          <circle cx="12" cy="12" r="10" stroke="#855fef" stroke-width="1.5"/>
          <path d="M15 12L12 12M12 12L9 12M12 12L12 9M12 12L12 15" stroke="#FFFFFF" stroke-width="1.5" stroke-linecap="round"/>
          </svg>
        </a>
      </Row>

      <AddTask
        addTaskShow={addTaskShow}
        addTaskHandleClose={addTaskHandleClose}
        columns_id={stateColumns[index]}

        checkUpdate={checkUpdate}
      />
     </Container>
    </div>
  );
}

export default App;
