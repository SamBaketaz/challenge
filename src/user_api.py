from flask import Blueprint, request, jsonify

users_blueprint = Blueprint('users', __name__)

# Base de datos simulada para almacenar usuarios
db = {
    1: {"Sam": "admin", "role": "admin"},
    2: {"Rosales": "films_user", "role": "films"},
    3: {"Araujo": "people_user", "role": "people"},
    # Agregar más usuarios según sea necesario
}

@users_blueprint.route('/usuarios', methods=['POST'])
def crear_usuario():
    """
    Crea un nuevo usuario y lo agrega a la base de datos.
    """
    data = request.json
    if "username" not in data or "role" not in data:
        return jsonify({"error": "Se requiere nombre de usuario y rol"}), 400
    # Suponiendo que el ID del usuario sea incremental
    user_id = max(db.keys()) + 1
    db[user_id] = {"username": data["username"], "role": data["role"]}
    return jsonify({"message": "Usuario creado exitosamente", "id": user_id}), 201

@users_blueprint.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    """
    Obtiene todos los usuarios almacenados en la base de datos.
    """
    return jsonify(db), 200

@users_blueprint.route('/usuarios/<int:user_id>', methods=['GET'])
def obtener_usuario(user_id):
    """
    Obtiene los detalles de un usuario específico por su ID.
    """
    if user_id not in db:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify(db[user_id]), 200

@users_blueprint.route('/usuarios/<int:user_id>', methods=['PUT'])
def actualizar_usuario(user_id):
    """
    Actualiza los detalles de un usuario específico por su ID.
    """
    if user_id not in db:
        return jsonify({"error": "Usuario no encontrado"}), 404
    data = request.json
    db[user_id]["username"] = data.get("username", db[user_id]["username"])
    db[user_id]["role"] = data.get("role", db[user_id]["role"])
    return jsonify({"message": "Usuario actualizado exitosamente"}), 200

@users_blueprint.route('/usuarios/<int:user_id>', methods=['DELETE'])
def borrar_usuario(user_id):
    """
    Elimina un usuario específico por su ID.
    """
    if user_id not in db:
        return jsonify({"error": "Usuario no encontrado"}), 404
    del db[user_id]
    return jsonify({"message": "Usuario eliminado exitosamente"}), 200
