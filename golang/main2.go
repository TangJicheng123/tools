package main

import "fmt"

func sum(x ...int) int {
	ret := 0
	for _, v := range x {
		ret += v
	}
	return ret
}

func main2() {
	fmt.Println(sum(1, 2, 3, 4, 5, 6, 7, 8, 9))
}
