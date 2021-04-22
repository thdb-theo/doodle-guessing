import * as React from "react"
import Canvas from "./canvas";
import Footer from "./footer";
// styles
const pageStyles = {
  color: "#232129",
  padding: 96,
  fontFamily: "-apple-system, Roboto, sans-serif, serif",
}
const headingStyles = {
  marginTop: 0,
  marginBottom: 32,
  maxWidth: 320,
}
const headingAccentStyles = {
  color: "#663399",
}



// markup
const IndexPage = () => {
  return (
    <main style={pageStyles}>
      <title>Home Page</title>
      <h1 style={headingStyles}>
        Welcome!
        <br />
        <span style={headingAccentStyles}>— Try drawing a digit! </span>
        <span role="img" aria-label="Party popper emojis">
         ✏️ ✏️ 
        </span>
      </h1>
      <Canvas></Canvas>
      <Footer></Footer>
    </main> 
  )
}

export default IndexPage
