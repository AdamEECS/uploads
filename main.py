import os

import flask
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect


app = Flask(__name__)

# 设置上传文件的最大尺寸为 2M
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024
# 如果你上传过大的文件, flask 会生成一个 413 响应
# 413 Request Entity Too Large（请求实体太大）


@app.route('/')
def index_view():
    return render_template('index.html')


# 定义保存上传文件的路径
uploads_dir = 'uploads/'


@app.route('/upload', methods=['POST'])
def upload_file():
    print('upload')
    # 通过 request.files 访问上传的文件
    # uploaded 是上传时候的文件名
    f = request.files.get('uploaded')
    print(request)
    print('upload, ', request.files)
    if f:
        filename = f.filename
        print('filename, ', filename)
        path = uploads_dir + filename
        print(os.getcwd())
        f.save(path)
        return redirect(path)
    else:
        return '<h1>没有上传</h1>'


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    # 用这个函数直接返回文件的响应
    return flask.send_from_directory(uploads_dir, filename)


if __name__ == '__main__':
    config = {
        'debug': True,
    }
    app.run(**config)
