import axios from 'axios';
import { useEffect, useState } from 'react';

import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import Modal from 'react-bootstrap/Modal';

function AddTask(props){
    const [nameTask, setNameTask] = useState("");
    const [descTask, setDescTast] = useState("");


    const addTaskToServer = () => {
        axios.post("https://global-inno-hack-dd509ac0d0a4.herokuapp.com/tasks/create", {
            name: nameTask,
            description: descTask,
            column_id: props.columns_id[0],
            users: []
        },{
            params:{
                user_id:'100'
            }
        })
        .catch(resp=>{
            console.log(resp)
            props.addTaskHandleClose()
            props.checkUpdate(nameTask)
        })
        .catch(e=>{
            
            console.log(e)
        })
    }

    return(
    <Modal show={props.addTaskShow} onHide={props.addTaskHandleClose}>
        <Modal.Header closeButton>
          <Modal.Title style={{color:'black'}}>Добавление задачи</Modal.Title>
        </Modal.Header>
    <Modal.Body>
    <Form>
        <Form.Group className="mb-3" controlId="formBasicEmail">
            <Form.Label style={{color:'black'}}>Задача</Form.Label>
          <Form.Control onChange={e => setNameTask(e.target.value)} type="text"/>
        </Form.Group>
  
        <Form.Group className="mb-3" controlId="formBasicPassword">
          <Form.Label style={{color:'black'}}>Описание</Form.Label>
          <Form.Control onChange={e => setDescTast(e.target.value)} type="text"/>
        </Form.Group>

        {/* <Form.Group className="mb-3" controlId="formBasicPassword">
          <Form.Label style={{color:'black'}}></Form.Label>
          <Form.Control type="text"/>
        </Form.Group> */}

        <Button onClick={addTaskToServer}>
          Добавить
        </Button>
      </Form>
      </Modal.Body>
      </Modal>
    )
}

export default AddTask;