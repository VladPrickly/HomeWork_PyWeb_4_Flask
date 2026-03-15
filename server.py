from flask import Flask, jsonify, request
from flask.views import MethodView
from pydantic import ValidationError

from db import Session, Advertisement
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

class HttpError(Exception):  # Класс для обработки ошибок
    def __init__(self, status_code: int, message: dict | list | str):
        self.status_code = status_code
        self.message = message


@app.errorhandler(HttpError)
def http_error_handler(error: HttpError):
    error_message = {
        'status': 'error',
        'description': error.message
    }
    response = jsonify(error_message)
    response.status_code = error.status_code
    return response


def get_adv(session: Session, adv_id: int):
    adv = session.get(Advertisement, adv_id)
    if adv is None:
        raise HttpError(404, message=f"Adv with id # {adv_id} doesn't exist")
    return adv

class AdvView(MethodView):

    def get(self, adv_id: int):
        with Session() as session:
            adv = get_adv(session, adv_id)
            return adv.to_dict()


    def post(self):
        json_data = request.json
        with Session() as session:
            adv = Advertisement(**json_data)
            session.add(adv)
            session.commit()
            return adv.to_dict()


    def patch(self, adv_id: int):
        json_data = request.json
        with Session() as session:
            adv = get_adv(session, adv_id)
            for field, value in json_data.items():
                setattr(adv, field, value)
            session.add(adv)
            session.commit()
            return adv.to_dict()
            # return jsonify({'id': adv_id,
            #                 'title': adv.title,
            #                 'description': adv.description,
            #                 'created_at': adv.created_at.isoformat(),
            #                 'owner': adv.owner
            #                 })


    def delete(self, adv_id: int):
        with Session() as session:
            adv = get_adv(session, adv_id)
            session.delete(adv)
            session.commit()
            return jsonify({'status': 'completed'})


app.add_url_rule(
    '/adv/<int:adv_id>',
    view_func=AdvView.as_view('with_adv_id'),
    methods=['GET', 'PATCH', 'DELETE'],
)

app.add_url_rule(
    '/adv/',
    view_func=AdvView.as_view('create_adv'),
    methods=['POST'],
)

if __name__ == '__main__':
    app.run()
