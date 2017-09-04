package main 

import "fmt"
import "net"
import "net/url"

func main() {
	s := "postgres://user:pass@host.com:5432/path?k=v#f"

	u, err := url.Parse(s)
	if err != nil {
		panic(err)
	}

	print := fmt.Println

	print(u.Scheme)
	print(u.User)
	print(u.User.Username())
	p, _ := u.User.Password()
	print(p)
	
	print(u.Host)
	host, port, _ := net.SplitHostPort(u.Host)
	print(host)
	print(port)

	print(u.Path)
	print(u.Fragment)
	print(u.RawQuery)
	m, _ := url.ParseQuery(u.RawQuery)
	print(m)
	print(m["k"][0])
}