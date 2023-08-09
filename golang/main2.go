package main

import "fmt"

func main2() {
	slice1 := make([]int, 0, 10)
	for i := 0; i < 10; i++ {
		slice1 = append(slice1, i)
	}
	for i, v := range slice1 {
		fmt.Printf("[%d] value: %d\n", i, v)
	}
}
