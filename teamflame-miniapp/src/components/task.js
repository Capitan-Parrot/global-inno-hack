import {useEffect, useState } from 'react';
import axios from 'axios';

import Form from 'react-bootstrap/Form';
import InputGroup from 'react-bootstrap/InputGroup';
import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';

function Task(props){
    const [comments, setComments] = useState(['com 1', 'com 1','com 1','com 1','com 1','com 1','com 1',]);

    const [commentValue, setCommentValue] = useState('');

    const [newColumnId, setNewColumnId] = useState(0);

    const changeStatus = (index) => {
        console.log(props.task_id)
        axios.post("https://global-inno-hack-dd509ac0d0a4.herokuapp.com/tasks/change_column", {
            task_id: props.task_id,
            column_id: props.columns_id[index]
        },
        {
            params:{
                user_id: "100"
            }
        })
        .then(data=>{
            console.log(data)
            props.checkUpdate(index)
        })
        .catch(e=>{
            console.log(e)
        })
    }

    const sendComment = (text) => {
        axios.post("https://global-inno-hack-dd509ac0d0a4.herokuapp.com/comments", {
            task_id: props.task_id,
            text_message: text
        }, {
            params:{
                user_id: "100"
            }
        })
            .then(data=>{
                console.log(data)
                setCommentValue('')
                props.checkUpdate(text)
            })
            .catch(e=>{
                console.log(e)
            })
    }
    return(
    <Modal show={props.show} onHide={props.handleClose}>
        <Modal.Header closeButton>
          <Modal.Title style={{color:'black'}}>{props.taskName}</Modal.Title>
        </Modal.Header>
        <Modal.Body style={{color:'black'}}>
            <Form.Select aria-label="Default select example" onChange={e => changeStatus(e.target.value)}>
                <option>Статус таски</option>
                {props.statuses.map((val, i)=>{
                    return(
                        <option key={i} value={i} >{val}</option>
                    )
                })}
            </Form.Select>
            <p className='mt-3'><span>Автор:</span></p>
            <p className=''><span>Исполнители:</span></p>
            
            <p className='mt-3'>Комментарии</p>
            <InputGroup>
                <Form.Control
                    type="text"
                    id="inputComment"
                    aria-describedby="commentHelpBlock"
                    value={commentValue}
                    onChange={e => setCommentValue(e.target.value)}
                /> 
                <Button onClick={()=>sendComment(commentValue)}>
                    enter
                </Button>
            </InputGroup>
            
                {props.comments.length > 0 ? props.comments.map((val, i)=>{
                    return(
                        <div key={i} className='border-bottom'>
                            <p className='text-muted'>{val.userName}</p>
                            <p>{val.text}</p>
                        </div>   
                    )
                }) : <></>}
        </Modal.Body>
    </Modal>
    )
}

export default Task;