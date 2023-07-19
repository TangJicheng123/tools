package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	args := os.Args[1:]
	N := 10
	if len(args) > 0 {
		n, err := strconv.Atoi(args[0])
		if err != nil {
			fmt.Println("Invalid value for N.")
			return
		}
		N = n
	}
	fmt.Println("Start main func...")
	t1(N)
}
