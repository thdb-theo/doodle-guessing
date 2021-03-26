//counter code
import React from "react"
import CanvasDraw from "react-canvas-draw";


const canvasStyles = {
    boxShadow: "0 13px 27px -5px rgba(50, 50, 93, 0.25), 0 8px 16px -8px rgba(0, 0, 0, 0.3)"
}
class Canvas extends React.Component {
    constructor(props) {
        super(props)
        this.canvas = React.createRef();

        this.state = {
            color: "#663399",
            width: 400,
            height: 400,
            brushRadius: 10,
            lazyRadius: 12
        };
    }
    componentDidMount() {
        // let's change the color randomly every 2 seconds. fun!
    }
    canvasChange = async () => {
        let response = await fetch("http://localhost:8081", {
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            },
            body: JSON.stringify(this.canvas.current.getSaveData()),
        }).then((data) => {
            if (!data.ok) {
                throw Error(data.status)
            }
            return data
        }).then(async data => {
            const response = await data.json();
            console.log(response)
        })
        // console.log(response);
    }

    render() {
        return (
            <CanvasDraw
                ref={this.canvas}
                brushColor={this.state.color}
                style={canvasStyles}
                onChange={this.canvasChange}
            />)
    }
}

export default Canvas