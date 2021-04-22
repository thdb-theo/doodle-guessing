import React from "react";

const footerStyles = {
    position: "fixed",
    left: 0,
    bottom: 0,
    width: "100%",
    marginLeft: 96,
    marginBotton: 30,
    // textAlign: "center"
}

const Footer = () => (
    <p style={footerStyles}>This website is open source! To contribute, read the code, or to find out how it works, check out the <a href="https://github.com/thdb-theo/doodle-guessing">GitHub</a></p>
)

export default Footer;