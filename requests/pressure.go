package main

import (
	"fmt"
	"io"
	"net/http"
	"time"
)

func fetchURL(url string, results chan<- int) {
	start := time.Now()

	resp, err := http.Get(url)
	if err != nil {
		fmt.Println("Error:", err)
		results <- -1
		return
	}
	defer resp.Body.Close()

	_, err = io.Copy(io.Discard, resp.Body)
	if err != nil {
		fmt.Println("Error:", err)
		results <- -1
		return
	}

	elapsed := time.Since(start)
	results <- int(elapsed.Milliseconds())
}

func main() {
	// 要测试的URL
	url := "http://localhost:8080"

	// 并发数量
	concurrency := 10000

	// 创建结果通道
	results := make(chan int, concurrency)

	// 启动并发请求
	for i := 0; i < concurrency; i++ {
		go fetchURL(url, results)
	}

	results_slice := make([]int, 0, concurrency)

	for i := 0; i < concurrency; i++ {
		temp := <-results
		results_slice = append(results_slice, temp)
	}

	// 关闭结果通道
	close(results)

	// 处理结果
	totalRequests := 0
	totalTime := 0
	minTime := int(^uint(0) >> 1) // 最大整数值
	maxTime := 0

	for elapsed := range results_slice {
		if elapsed != -1 {
			totalRequests++
			totalTime += elapsed

			if elapsed < minTime {
				minTime = elapsed
			}

			if elapsed > maxTime {
				maxTime = elapsed
			}
		}
	}

	// 输出结果
	fmt.Printf("URL: %s\n", url)
	fmt.Printf("并发数量: %d\n", concurrency)
	fmt.Printf("总请求数: %d\n", totalRequests)
	fmt.Printf("平均响应时间(ms): %d\n", totalTime/totalRequests)
	fmt.Printf("最小响应时间(ms): %d\n", minTime)
	fmt.Printf("最大响应时间(ms): %d\n", maxTime)
}
