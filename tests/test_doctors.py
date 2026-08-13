def test_create_and_get_doctor(client):
    resp = client.post('/doctors', json={'name': 'Dr. Bob', 'specialization': 'Cardiology'})
    assert resp.status_code == 201
    data = resp.json()
    assert data['name'] == 'Dr. Bob'

    did = data['id']
    resp2 = client.get(f'/doctors/{did}')
    assert resp2.status_code == 200
    assert resp2.json()['specialization'] == 'Cardiology'
