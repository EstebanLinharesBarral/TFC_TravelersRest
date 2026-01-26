import Summarizer from "../summarizer/Summarizer"
import './summary.css'

const Summary = (props) => {
    return(
        <div className={"summary"}>
            <Summarizer title = {"Próximas sesiones"}/>
            <Summarizer title = {"Sesiones anteriores"}/>
        </div>
    )
}

export default Summary