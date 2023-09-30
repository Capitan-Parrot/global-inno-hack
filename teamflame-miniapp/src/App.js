import './App.css';
import leftIcon from './assets/chevron-left-svgrepo-com.svg'
import rightIcon from './assets/chevron-right-svgrepo-com.svg'

import { useEffect, useState } from 'react';

import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Button from 'react-bootstrap/Button';

import Header from './components/header'
import Columns from './components/columns'

const tg = window.Telegram.WebApp;

function App() {
  const [stateTasksName, setStateTasksName] = useState(["Сделать", "В работе", "Закрыто"]);
  const [stateTaskName, setStateTaskName] = useState("Сделать");

  useEffect(() => {
      tg.ready();
  }, []);

  const nextStateTask = () => {
    let cur_arr = stateTasksName;
    const lastIndex = cur_arr.length - 1;

    for (let i = 0; i < lastIndex; i++) {
      const temp = cur_arr[i];
      cur_arr[i] = cur_arr[i + 1];
      cur_arr[i + 1] = temp;
    }

    // console.log(cur_arr)
    setStateTasksName(cur_arr)
    setStateTaskName(cur_arr[0])
  }

  const prevStateTask = () => {
    let cur_arr = stateTasksName;
    const lastIndex = cur_arr.length - 1;

    for (let i = lastIndex; i > 0; i--) {
      const temp = cur_arr[i];
      cur_arr[i] = cur_arr[i - 1];
      cur_arr[i - 1] = temp;
    }

    // console.log(cur_arr)
    setStateTasksName(cur_arr)
    setStateTaskName(cur_arr[0])
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
            TaskName={stateTaskName}
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

      <Row>
        <Col>
          
        </Col>
      </Row>
     </Container>
    </div>
  );
}

export default App;
