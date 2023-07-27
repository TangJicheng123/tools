package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

// 通过字典模拟 DB
var db = make(map[string]string)

func ping(c *gin.Context) {
	c.String(http.StatusOK, "pong")
}

func nameValue(c *gin.Context) {
	user := c.Params.ByName("name")
	value, ok := db[user]
	state := "OK"
	if !ok {
		state = "ERROR"
		value = "None"
	}
	c.JSON(http.StatusOK, gin.H{"status": state, "user": user, "value": value})
}

func adminFunc(c *gin.Context) {
	user := c.MustGet(gin.AuthUserKey).(string)

	// 解析并验证 JSON 格式请求数据
	var json struct {
		Value string `json:"value" binding:"required"`
	}

	if c.Bind(&json) == nil {
		db[user] = json.Value
		c.JSON(http.StatusOK, gin.H{"status": "ok"})
	}
}

func setupRouter() *gin.Engine {
	// 初始化 Gin 框架默认实例，该实例包含了路由、中间件以及配置信息
	r := gin.Default()

	// Ping 测试路由
	r.GET("/ping", ping)

	// 获取用户数据路由
	r.GET("/user/:name", nameValue)

	// 需要 HTTP 基本授权认证的子路由群组设置
	authorized := r.Group("/", gin.BasicAuth(gin.Accounts{
		"foo":  "bar", // 用户名:foo 密码:bar
		"manu": "123", // 用户名:manu 密码:123
	}))

	// 保存用户信息路由
	authorized.POST("admin", adminFunc)

	return r
}

func main1() {
	// 添加用户
	db["haha"] = "good"
	db["xiao"] = "hello"

	// 设置路由信息
	r := setupRouter()
	// 启动服务器并监听 8080 端口
	r.Run(":8080")
}
