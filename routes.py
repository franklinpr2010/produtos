from flask import Blueprint, request, jsonify

from models import Produtos, db


produtos_blueprint = Blueprint('produtos_api_routes', __name__, url_prefix='/api/produtos')


@produtos_blueprint.route('/all', methods=['GET'])
def get_all_produtos():
    all_produtos = Produtos.query.all()
    result = [produtos.serialize() for produtos in all_produtos]
    response = {"result":result}
    return jsonify(response)


@produtos_blueprint.route('/create', methods=['POST'])
def create_produto():
    try:
        produto = Produtos()
        produto.name = request.form['name']
        produto.slug = request.form['slug']
        produto.image = request.form['image']
        produto.price = request.form['price']

        db.session.add(produto)
        db.session.commit()

        response = {'message': 'Produto Create', 'result': produto.serialize()}
    except Exception as e:
        print(str(e))
        response = {'message': 'Produto creation failed'}

    return jsonify(response)

@produtos_blueprint.route('/delete/<id>', methods=['DELETE'])
def delete_produto(id):
    try:
        print(id)
        produto = Produtos.query.get(id)
        print(produto)
        db.session.delete(produto)
        db.session.commit()

        response = {'message': 'Produto deletado!!!', 'result': produto}
    except Exception as e:
        print(str(e))
        response = {'message': 'Falha ao deletar o produto!!!'}

    return jsonify(response)




@produtos_blueprint.route('/<slug>', methods=['GET'])
def produto_details(slug):
    produto = Produtos.query.filter_by(slug=slug).first()
    print(produto.serialize())
    if produto:
        response = {"result":produto.serialize()}
    else:
        response = {"message":"No produto found"}

    return jsonify(response)


@produtos_blueprint.route('/<id>', methods=['GET'])
def produto_by_id(id):
    produto = Produtos.query.get(id)
    return produto
