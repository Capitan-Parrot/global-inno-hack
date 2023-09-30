import Card from 'react-bootstrap/Card';

function Columns(props){
    return(
        <Card style={{borderTop: '#855fef solid 2px'}}>
        <Card.Body >
          <Card.Title className='text-center'>{props.TaskName}</Card.Title>
        </Card.Body>
      </Card>
    )
}

export default Columns;