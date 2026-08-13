def test_create_and_get_patient(client):
    resp = client.post('/patients', json={'name': 'Alice', 'email': 'alice@example.com', 'phone': '123'})
    assert resp.status_code == 201
    data = resp.json()
    assert data['name'] == 'Alice'

    pid = data['id']
    resp2 = client.get(f'/patients/{pid}')
    assert resp2.status_code == 200
    assert resp2.json()['email'] == 'alice@example.com'
