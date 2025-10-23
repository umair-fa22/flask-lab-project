from flask import Flask, render_template, request

app = Flask(__name__)

def test_home():
    response = app.test_client().get('/')
    assert response.status_code == 200

def test_health():
    response = app.test_client().get('/health')
    assert b"OK" in response.data
