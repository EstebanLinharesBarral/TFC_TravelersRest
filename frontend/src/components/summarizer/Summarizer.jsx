import './summarizer.css'

const Summarizer = (props) => {
    return(
        <div className="summarizer">
            <h3 className={"summarizer_title"}>{props.title}</h3>
            <div className={'summarizer_content'}>
                <h4><span>Campaña</span><span>Fecha</span></h4>
                <div className={"summarizer_data"}>

                </div>
            </div>
        </div>
    )
}

export default Summarizer