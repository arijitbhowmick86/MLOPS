from flask import Flask

app = Flask(__name__)

@app.route('/ping/<name>', methods=['GET'])
def test_connection(name):
    val = f'Welcome Mr. {name} !'
    return val


@app.route('/ping_json/<name>', methods=['GET'])
def test_connection_json(name):
    val = f'Welcome Mr. {name} !'
    return {"message":val}


# docker build -t flask_app .
# docker build -t arijitbhowmick86/flask_app .
# docker run -d -p 8000:5000 flask_app
# docker push arijitbhowmick86/flask_app
# docker pull arijitbhowmick86/flask_app:latest


# Install AWS power shell and execute below commands
# aws configure
# AWS Access Key ID [None]: AKIAV7V2DTHZMN4SVULO
# AWS Secret Access Key [None]: 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
# Default region name [None]: us-east-1
# Default output format [None]:
# docker login -u AWS -p $(aws ecr get-login-password --region us-east-1) 411633424882.dkr.ecr.us-east-1.amazonaws.com
# docker build -t flask_app .
# docker tag flask_app:latest 411633424882.dkr.ecr.us-east-1.amazonaws.com/flask_app:latest
# OR
# docker tag arijitbhowmick86/flask_app:latest 411633424882.dkr.ecr.us-east-1.amazonaws.com/flask_app:latest
# docker push 411633424882.dkr.ecr.us-east-1.amazonaws.com/flask_app:latest



# Image uri
# 411633424882.dkr.ecr.us-east-1.amazonaws.com/flask_app:latest