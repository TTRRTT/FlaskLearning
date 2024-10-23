from flask import Flask, request, jsonify

# Имеет тип flask.app.Flask, будет помогать создавать API порты
app = Flask(__name__)

users = {
    1: {
        'name': 'Lyoha',
        'age': 37
    },

    2: {
        'name': 'Borya',
        'age': -1
    },

    3: {
        'name': 'Kto-to',
        'age': 13
    }
}

# Адрес будет https://localhost:5000/hello_world
# /hello_world - это порт
@app.route('/hello_world') # По умолчанию methods=['GET']
def get_hello():
    data = {
        1: 'Hello, World!'
    }
    return jsonify(data)

@app.route('/users/')
def return_user_info():
    id = int(request.args.get('id'))
    if 0 <= id <= len(users) - 1:
        return jsonify(users[id])
    return jsonify('ID out of range')

if __name__ == '__main__':
    app.run(debug=True) # Запуск сервера
