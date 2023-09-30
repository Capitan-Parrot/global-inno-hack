import Container from 'react-bootstrap/Container';
import Navbar from 'react-bootstrap/Navbar';
import logo from '../assets/image.svg'
import '../index.css';

function Header(){
    return(
        <Navbar expand="lg" className='header_back'>
        <Container>
            <Navbar.Brand href="#home">
                <img
                src={logo}
                width="30"
                height="30"
                className="d-inline-block align-top"
                alt="React Bootstrap logo"
                />
            </Navbar.Brand>
            <Navbar.Brand className='header_text' href="#home">TeamFlame</Navbar.Brand>
        </Container>
        </Navbar>
    )
}

export default Header;