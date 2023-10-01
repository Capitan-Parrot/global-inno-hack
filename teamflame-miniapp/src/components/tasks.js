import { useState } from 'react';

import Card from 'react-bootstrap/Card';

import Task from './task';

function Tasks(props){
    const [show, setShow] = useState(false);

    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);

    return(
        <>
        <Card>
            <Card.Body onClick={handleShow}>
                <Card.Title style={{fontSize:'99%', opacity:'70%'}}>{props.title}</Card.Title>
                <Card.Text style={{fontSize:'110%'}}>{props.task}</Card.Text>
            </Card.Body>
        </Card>
        {/* {console.log(props.comments)} */}
        <Task
            show={show}
            handleShow={handleShow}
            handleClose={handleClose}
            taskName={props.task}
            statuses={props.statuses}
            status={props.status}
            author={props.author}
            comments={props.comments}
            columns_id={props.columns_id}
            task_id={props.task_id}
            task_desc={props.task_desc}

            checkUpdate={props.checkUpdate}
        />
        </>
    )
}

export default Tasks