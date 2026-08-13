from datetime import datetime, timedelta

def test_create_appointment_and_prevent_overlap(client):
    # create patient and doctor
    p = client.post('/patients', json={'name': 'P', 'email': 'p@example.com'}).json()
    d = client.post('/doctors', json={'name': 'D'}).json()

    start1 = datetime.utcnow()
    end1 = start1 + timedelta(hours=1)

    appt1 = client.post('/appointments', json={
        'patient_id': p['id'],
        'doctor_id': d['id'],
        'appointment_start': start1.isoformat(),
        'appointment_end': end1.isoformat(),
    })
    assert appt1.status_code == 201

    # overlapping appointment should be rejected
    start2 = start1 + timedelta(minutes=30)
    end2 = start2 + timedelta(hours=1)
    appt2 = client.post('/appointments', json={
        'patient_id': p['id'],
        'doctor_id': d['id'],
        'appointment_start': start2.isoformat(),
        'appointment_end': end2.isoformat(),
    })
    assert appt2.status_code == 400

    # non-overlapping after end is allowed
    start3 = end1
    end3 = start3 + timedelta(hours=1)
    appt3 = client.post('/appointments', json={
        'patient_id': p['id'],
        'doctor_id': d['id'],
        'appointment_start': start3.isoformat(),
        'appointment_end': end3.isoformat(),
    })
    assert appt3.status_code == 201
