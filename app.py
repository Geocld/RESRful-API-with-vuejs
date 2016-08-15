from flask import Flask, jsonify, make_response, request, abort

# 静态文件的放置路径，可根据实际情况设置，这里设置为默认路径：'./static/'
app = Flask(__name__, static_url_path='')

#模拟json数据
tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

#设置根路由
@app.route('/')
def root():
	return app.send_static_file('index.html')

#GET方法api
@app.route('/todo/api/tasks', methods=['GET'])
def getTasks():
	return jsonify({'tasks': tasks})

#POST方法API，添加数据项
@app.route('/todo/api/addTask', methods=['POST'])
def add_task():
	if request.json['title'] == "":
		abort(400)
	task = {
		'id' : tasks[-1]['id'] + 1,
		'title': request.json['title'],
		'description' : request.json.get('description', ""),
		'done' : False
	}
	tasks.append(task)
	return jsonify({'tasks': tasks}), 201

#POST方法API，删除数据项
@app.route('/todo/api/deleteTask', methods=['POST'])
def delete_task():
	task_id = request.json['id']
	for task in tasks:
		if task['id'] == task_id:
			tasks.remove(task)
			return jsonify({'tasks': tasks}), 201

#404
@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
	app.run(debug=True)

