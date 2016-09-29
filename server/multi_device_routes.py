from server import app
from server.receiver import api as receiver_api
from server.settings import BASE_API


# Halo on Xbox One
@app.route(BASE_API % '/halo', methods=('PUT',))
def halo():
    return receiver_api.halo()


# Music from Alexa
@app.route(BASE_API % '/music', methods=('PUT',))
def music():
    return receiver_api.music()

