package main

import (
	"fmt"
	"time"
)

func printNumber(num int, ch chan<- bool) {
	fmt.Printf("[%s] %d\n", time.Now().Format("15:04:05"), num)
	ch <- true
}

func t1(N int) {
	ch := make(chan bool)

	for i := 1; i <= N; i++ {
		go printNumber(i, ch)
	}

	for i := 1; i <= N; i++ {
		<-ch
	}
}
