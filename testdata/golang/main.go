package main

import (
	"fmt"
	"os"
)

func main() {
	fmt.Println("helloworld")
	r, _ := os.LookupEnv("runner")
	fmt.Println(r)
}
