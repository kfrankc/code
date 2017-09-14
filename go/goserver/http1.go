package main 

import (
	"io"
	"net/http"
)

func hello(w http.ResponseWriter, r *http.Request) {
	io.WriteString(w, "Hellow World!")
}

var mux map[string]func(http.ResponseWriter, *http.Request)

func main() {
	server := http.Server{
		Addr: ":8000",
		Handler: &myHandler{},
	}


	mux := make(map[string]func(http.ResponseWriter, *http.Request))
	mux["/"] = hello
	server.ListenAndServe()
}