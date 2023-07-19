package main

import (
	"fmt"
	"strings"
)

func main() {
	s := "owoztneoer"
	result := originalDigits(s)
	fmt.Println(result)
}

func originalDigits(s string) string {
	// 统计每个字母出现的次数
	count := make(map[rune]int)
	for _, ch := range s {
		count[ch]++
	}

	// 统计数字出现的次数
	digits := make([]int, 10)
	digits[0] = count['z']                                     // 'z' 只在 "zero" 中出现，表示数字 0
	digits[2] = count['w']                                     // 'w' 只在 "two" 中出现，表示数字 2
	digits[4] = count['u']                                     // 'u' 只在 "four" 中出现，表示数字 4
	digits[6] = count['x']                                     // 'x' 只在 "six" 中出现，表示数字 6
	digits[8] = count['g']                                     // 'g' 只在 "eight" 中出现，表示数字 8
	digits[1] = count['o'] - digits[0] - digits[2] - digits[4] // 'o' 在 "one", "zero", "two", "four" 中出现，减去已经统计过的次数
	digits[3] = count['h'] - digits[8]                         // 'h' 在 "three", "eight" 中出现，减去已经统计过的次数
	digits[5] = count['f'] - digits[4]                         // 'f' 在 "five", "four" 中出现，减去已经统计过的次数
	digits[7] = count['s'] - digits[6]                         // 's' 在 "seven", "six" 中出现，减去已经统计过的次数
	digits[9] = count['i'] - digits[5] - digits[6] - digits[8] // 'i' 在 "nine", "five", "six", "eight" 中出现，减去已经统计过的次数

	// 构造最终的结果字符串
	var result strings.Builder
	for i := 0; i < 10; i++ {
		for j := 0; j < digits[i]; j++ {
			result.WriteString(fmt.Sprintf("%d", i))
		}
	}

	return result.String()
}
