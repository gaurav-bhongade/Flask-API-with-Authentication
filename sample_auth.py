from flask import Flask
from datetime import timedelta
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token, get_jwt_identity, jwt_required
from flask import request, jsonify
import json

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "1212jhjhu3364$@jhjhdsfjh"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=5)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(minutes=15)
jwt = JWTManager(app)



#http://localhost:5000/gettoken

@app.route('/gettoken', methods=['POST'])
def validate_user():

    req_body = request.get_json()
    if req_body.get('USERNAME') == 'admin' and req_body.get('PASSWORD') == 'root123':
        atoken = create_access_token(identity=(req_body.get('USERNAME'), req_body.get('PASSWORD')))
        rtoken = create_refresh_token(identity=(req_body.get('USERNAME'), req_body.get('PASSWORD')))
        return json.dumps({"access_token": atoken, "refresh_token": rtoken})
        #return json.dumps({"access_token": token})
    else:
        return json.dumps({"Error": "Invalid Credentials"})
        #return jsonify('invalid credentials...!'), 401

# http://localhost:5000/public/api
@app.route('/public/api', methods=['GET'])
def public_api_endpoint():
    return json.dumps({"SUCCESS": "Public API is Invoked....!"})


# http://localhost:5000/secure/api
@app.route('/secure/api', methods=['GET'])
@jwt_required()
def secure_api_endpoint():
    return json.dumps({"SUCCESS": "Secure API is Invoked....!"})

#http://localhost:5000/refresh/api
@app.route('/refresh/api', methods=['GET'])
@jwt_required(refresh=True)
def get_accesstoken_using_refreshtoken():
    identity = get_jwt_identity()
    atoken = create_access_token(identity=identity)
    return json.dumps({"access_token": atoken})


if __name__=='__main__':
    app.run(debug=True)
