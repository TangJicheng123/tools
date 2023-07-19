package main

import (
	"fmt"
	"time"
)

func print1(s int, c chan int) {
	now := time.Now()
	fmt.Println(s, now)
	c <- s
}

func t1() {
	c1 := make(chan int)
	c2 := make(chan int)
	go print1(11, c1)
	go print1(22, c2)
	<-c2
	<-c1
}
