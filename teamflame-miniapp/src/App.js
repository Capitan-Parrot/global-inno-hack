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
  const [updateTasks, setUpdateTasks] = useState(0);

  const [comments, setComments] = useState([]);

  const [tasks, setTasks] = useState([]);

  const [index, setIndex] = useState(0);

  const [addTaskShow, setAddTaskShow] = useState(false);

  const [forBoardId, setForBoardId] = useState('');

  const addTaskHandleShow = () => setAddTaskShow(true);
  const addTaskHandleClose = () => setAddTaskShow(false);

  const project_id = '6517218ff074f999078a6ecd';
  const USER_ID = 'tg.initDataUnsafe.user.id ?';

  const getColumns = () => {
    axios.get(`https://global-inno-hack-dd509ac0d0a4.herokuapp.com/board/boardsByProject/${project_id}`,
    {params: {
      user_id:"100"
    }})
      .then(data=>{
        console.log(data.data[0].spaceId)
        setStateColumns(data.data[0].columns)
      })
      .catch(e => {
        console.log(e)
      })
  }

  const getTasksFromColumn = (column_id) => {
    axios.get(`https://global-inno-hack-dd509ac0d0a4.herokuapp.com/tasks/getTasksByColumn/${column_id}`,
    {params:{
      user_id: "100"
    }})
      .then(data=>{
        console.log(data)
        let column_names = [];
        let comments = [];

        data.data.map((col, i) => {
          column_names.push({"name": col.name, "task_num": col.taskNumber, "task_id": col.id})
          comments.push(col.comments);
        })
        console.log(comments)
        setComments(comments)
        setTasks(column_names)
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
      getColumns();
      // setTestState(tg.initDataUnsafe.chat.username)
  }, []);

  useEffect(() => {  
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

      <Row className=''>
        <Col >
          <a onClick={prevStateTask}>
            <svg width="30" height="30" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <rect width="24" height="24" fill="none"/>
            <path d="M14.5 17L9.5 12L14.5 7" stroke={tg.themeParams.text_color} stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </a>
        </Col>
        <Col xs={8}>
          <Columns
            TaskName={stateTasksName[index]}
          />
        </Col>
        <Col>
          <a onClick={nextStateTask}>
          <svg width="30" height="30" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
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
                    statuses={stateTasksName}
                    comments={comments[i]}
                    columns_id={stateColumns}

                    checkUpdate={checkUpdate}
                  />
                </Col>
            </Row>
        )
      }) : 
      
      // <Container >
        <Row style={{marginLeft: '40%', marginTop:'40%'}}>
          <Col>
            <div className="spinner-border" role="status"></div>
          </Col>
        </Row>
        // </Container>
      }
      
      <Row style={{position: 'absolute', top: tg.viewportStableHeight}}>
        <Button onClick={addTaskHandleShow}>Добавить задачу</Button>
      </Row>

      <AddTask
        addTaskShow={addTaskShow}
        addTaskHandleClose={addTaskHandleClose}
        columns_id={stateColumns}

        checkUpdate={checkUpdate}
      />
     </Container>
    </div>
  );
}

export default App;
