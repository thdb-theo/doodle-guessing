using HTTP

HTTP.listen() do http::HTTP.Stream
    @show http.message
    @show HTTP.header(http, "Content-Type")
    while !eof(http)
        println("body data: ", String(readavailable(http)))
    end

    HTTP.setstatus(http, 200)
    HTTP.setheader(http, "Access-Control-Allow-Headers" => "content-type")
    HTTP.setheader(http, "Access-Control-Allow-Origin" => "http://localhost:8000")
    HTTP.startwrite(http)
    write(http, "{\"item\": \"cat\"}")
end