import { Link } from "react-router-dom"
import  LogoMastersTavern from '../../img/LogoMastersTavernSinFondo.png';
import UserInfo from "../user_info/UserInfo";

const Header = (props) => {
    return(
        <header>
            <button>Hola</button>
            <Link to={'/'}><img src={LogoMastersTavern} alt="MastersTavernInicio"/></Link>
            <UserInfo></UserInfo>
        </header>
    )
}

export default Header