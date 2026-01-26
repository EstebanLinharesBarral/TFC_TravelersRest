import Header from "../../components/header/Header";
import Navigator from "../../components/navigator/Navigator";
import Footer from "../../components/footer/Footer";
import './main.css';
import Summary from "../../components/summary/Summary";

const Main = (props) => {
    return(
        <div className={"mainR"}>
            <Header></Header>
            <Navigator></Navigator>
            <Summary />
            <Footer></Footer>
        </div>
    )
}

export default Main;