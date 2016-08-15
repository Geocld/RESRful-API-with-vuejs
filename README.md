# RESRful-API-with-vuejs
基于Python Flask的简易RESTful API接口，可实现基本的前后端分离。

### 服务器端

采用Python Flask框架搭建基本api，可实现GET、POST、PUT、DELETE方法，为前端提供API接口。

片段：

```python
#GET方法api
@app.route('/todo/api/tasks', methods=['GET'])
def getTasks():
	return jsonify({'tasks': tasks})
```

### 前端

通过发送HTTP请求进行数据交互，此处使用vue.js框架进行示例，使用vue-resource发送HTTP请求。

片段：

```javascript
compiled: function() {
	var self = this;
	//在编译后即调用API接口取得服务器端数据
	self.$http.get('/todo/api/tasks').then(function(res) {
		self.tasks = res.data.tasks;
	});
},
```

### 项目依赖

* Python flask（请使用pip进行安装）
* vue.js
* vue-resource

### 运行

```
python3 ./app.py
```

打开浏览器，进入http://127.0.0.1:5000/

#### 备注（在virtualenv环境下运行的方法）

1、安装virtualenv

```shell
$ pip3 install virtualenv
```

2、创建项目目录

```shell
$mkdir project-name && cd project-name
```

3、建立名为venv的虚拟环境

```shell
$virtualenv --no-site-packages venv
```

4、进入虚拟环境

```shell
$source venv/bin/activate
```

5、运行项目

```shell
(venv)python3 app.py
```

6、退出虚拟环境

```shell
$deactivate
```

