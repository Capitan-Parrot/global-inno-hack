import {useEffect, useState } from 'react';
import axios from 'axios';

import Form from 'react-bootstrap/Form';
import InputGroup from 'react-bootstrap/InputGroup';
import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';
import { Badge } from 'react-bootstrap';

const tg = window.Telegram.WebApp;

function Task(props){
    // const [comments, setComments] = useState(['com 1', 'com 1','com 1','com 1','com 1','com 1','com 1',]);

    const [commentValue, setCommentValue] = useState('');

    const [newColumnId, setNewColumnId] = useState(0);

    const USER_ID = tg.initDataUnsafe.user.id;

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
            props.handleClose()
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
                user_id: USER_ID
            }
        })
            .then(data=>{
                console.log(data)
                setCommentValue('')
                // props.handleClose()
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
            {props.task_desc != '' ? <p><strong>Описание</strong></p> : ''}
            <p className='mb-1' style={{wordWrap: "break-word"}}>{props.task_desc}</p>
            <hr/>
            <Form.Select aria-label="Default select example" onChange={e => changeStatus(e.target.value)}>
                <option>Статус задачи</option>
                {props.statuses.map((val, i)=>{
                    return(
                        <option key={i} value={i} >{val}</option>
                    )
                })}
            </Form.Select>
            <p>Текущий статус <Badge bg="warning">{props.status}</Badge></p>
            <hr/>
            <p className='mt-3'><strong>Автор:</strong> {props.author}</p>
            <hr/>
            <p className=''><strong>Исполнители:</strong></p>
            <hr/>
            
            <p className='mt-3'><strong>Комментарии</strong></p>
            <InputGroup>
                <Form.Control
                    type="text"
                    id="inputComment"
                    aria-describedby="commentHelpBlock"
                    value={commentValue}
                    onChange={e => setCommentValue(e.target.value)}
                /> 
                <Button disabled={commentValue == '' ? true : false} onClick={()=>sendComment(commentValue)}>
                <svg width="30" height="30" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M20.7639 12H10.0556M3 8.00003H5.5M4 12H5.5M4.5 16H5.5M9.96153 12.4896L9.07002 15.4486C8.73252 16.5688 8.56376 17.1289 8.70734 17.4633C8.83199 17.7537 9.08656 17.9681 9.39391 18.0415C9.74792 18.1261 10.2711 17.8645 11.3175 17.3413L19.1378 13.4311C20.059 12.9705 20.5197 12.7402 20.6675 12.4285C20.7961 12.1573 20.7961 11.8427 20.6675 11.5715C20.5197 11.2598 20.059 11.0295 19.1378 10.5689L11.3068 6.65342C10.2633 6.13168 9.74156 5.87081 9.38789 5.95502C9.0808 6.02815 8.82627 6.24198 8.70128 6.53184C8.55731 6.86569 8.72427 7.42461 9.05819 8.54246L9.96261 11.5701C10.0137 11.7411 10.0392 11.8266 10.0493 11.9137C10.0583 11.991 10.0582 12.069 10.049 12.1463C10.0387 12.2334 10.013 12.3188 9.96153 12.4896Z"
                stroke={tg.themeParams.text_color} stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
                </Button>
            </InputGroup>
            
                {props.comments.length > 0 ? props.comments.map((val, i)=>{
                    return(
                        <div key={i} className='border-bottom'>
                            <p className='text-muted'>{val.userName}</p>
                            <p style={{wordWrap: "break-word"}}>{val.text}</p>
                        </div>   
                    )
                }) : <></>}
        </Modal.Body>
    </Modal>
    )
}

export default Task;