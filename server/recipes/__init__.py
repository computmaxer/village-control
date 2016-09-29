from flask import Blueprint

from server.receiver import api as receiver_api
from server.settings import BASE_API


recipes_module = Blueprint('recipes', __name__)


# Halo on Xbox One
@recipes_module.route(BASE_API % '/v1/halo', methods=('PUT',))
def halo():
    return receiver_api.halo()


# Music from Alexa
@recipes_module.route(BASE_API % '/v1/music', methods=('PUT',))
def music():
    return receiver_api.music()
