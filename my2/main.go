package main

import (
	"fmt"
)

func main() {
	s := "ABAB"
	k := 2
	result := characterReplacement(s, k)
	fmt.Println(result)
}

func characterReplacement(s string, k int) int {
	// 统计每个字符出现的次数
	count := make([]int, 26)
	maxCount := 0 // 当前窗口内出现次数最多的字符的次数
	start := 0    // 窗口的起始位置
	maxLen := 0   // 最长子字符串的长度

	for end := 0; end < len(s); end++ {
		ch := s[end] - 'A'
		count[ch]++
		maxCount = max(maxCount, count[ch])

		// 窗口内需要替换的字符个数
		replaceCount := (end - start + 1) - maxCount

		if replaceCount > k {
			// 如果窗口内需要替换的字符个数大于k，则窗口右移
			count[s[start]-'A']--
			start++
		}

		// 更新最长子字符串的长度
		maxLen = max(maxLen, end-start+1)
	}

	return maxLen
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
