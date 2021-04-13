//counter code
import React from "react"
import CanvasDraw from "react-canvas-draw";
import Slider from '@material-ui/core/Slider';
import Typography from '@material-ui/core/Typography';
import { withStyles } from '@material-ui/core/styles';


const canvasStyles = {
    boxShadow: "0 13px 27px -5px rgba(50, 50, 93, 0.25), 0 8px 16px -8px rgba(0, 0, 0, 0.3)"
}


const guessStyles = {
    color: "#FF8C42",

}

const underStyles = {
    width: "400px",
    display: "flex",
    marginTop: "30px",

}

const clearStyles = {
    fontWeight: "bold",
    border: "none",
    borderRadius: "20px",
    cursor: "pointer",
    background: "#FF8C42",
    color: "white",
    paddingLeft: "20px",
    paddingRight: "20px",
    fontSize: "15px",
    paddingTop: "5px",
    paddingBottom: "5px",
    width: "40px",
    marginLeft: "auto",
    marginRight: "3px",
    float: "right",
    boxSizing: "content-box",
    ':focus': {
        letterSpacing: "1px",
        color:"red",
    }
}

const sliderStyles = {
    float: "left",
    width: "200px",
}

const BrushSlider = withStyles({
    root: {
        color: '#663399',
        width: "200px",
        height: 8,
        marginLeft: "3px",
    },
    thumb: {
        height: 24,
        width: 24,
        backgroundColor: '#fff',
        border: '2px solid currentColor',
        marginTop: -8,
        marginLeft: -12,
        '&:focus, &:hover, &$active': {
            boxShadow: 'inherit',
        },
    },
    active: {},
    valueLabel: {
        left: 'calc(-50% + 4px)',
    },
    track: {
        height: 8,
        borderRadius: 4,
    },
    rail: {
        height: 8,
        borderRadius: 4,
    },
})(Slider);

class Canvas extends React.Component {
    constructor(props) {
        super(props)
        this.canvas = React.createRef();

        this.state = {
            color: "#663399",
            width: 400,
            height: 400,
            brushRadius: 20,
            lazyRadius: 12,
            guess: -1
        };
    }

    indefiniteArticle(num) {
        if (num === "8")
            return "an"
        else
            return "a"
    }

    canvasChange = async () => {
        await fetch("http://localhost:8081", {
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
            this.setState({ "guess": response.item })
        }).catch(err => {
            alert("Unfortunatly, the server is currently down 😤\r\nPlease try again later")
        });
    }

    clear = () => {
        this.canvas.current.clear()
    }

    Guess = () => {
        let article = this.indefiniteArticle(this.state.guess)
        if (this && this.state.guess !== -1) {
            return <h3 style={guessStyles}>Looks like {article} {this.state.guess}</h3>
        } else {
            return <h3 style={guessStyles}>&#8203;</h3>
        }
    }
    sliderSlid = (event, newValue) => {
        this.setState({ brushRadius: newValue })
    }

    render() {
        return (
            <main>
                <this.Guess></this.Guess>
                <CanvasDraw
                    ref={this.canvas}
                    brushColor={this.state.color}
                    brushRadius={this.state.brushRadius}
                    lazyRadius={this.state.lazyRadius}
                    style={canvasStyles}
                    onChange={this.canvasChange}
                    canvasWidth={this.state.width}
                    canvasHeight={this.state.height}
                />
                <div style={underStyles}>
                    <div className={sliderStyles}>
                        <Typography id="discrete-slider" gutterBottom>
                            Brush Size&nbsp;
                            <span role="img" aria-label="Brush emojis">
                            🖌️
                            </span>
                        </Typography>

                        <BrushSlider
                            value={this.state.brushRadius}
                            onChange={this.sliderSlid}
                            aria-label="discrete-slider"
                            min={1}
                            max={40}
                            step={1}
                            valueLabelDisplay="auto"
                        />

                    </div>
                    <button onClick={this.clear} style={clearStyles}>Clear</button>
                </div>
            </main>
        )
    }
}

export default Canvas