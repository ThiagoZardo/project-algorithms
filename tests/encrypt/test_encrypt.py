import pytest
from challenges.challenge_encrypt_message import encrypt_message

def test_encrypt_message():
    message = 'development'

    for key in range(2, len(message)):
        encrypt = encrypt_message(message, key)
        if key % 2 != 0:
            part_one = message[:key]
            part_two = message[key:]
            assert encrypt == part_one[::-1] + '_' + part_two[::-1]
        else:
            part_one = message[:key]
            part_two = message[key:]
            assert encrypt == part_two[::-1] + '_' + part_one[::-1]

    encrypt = encrypt_message(message, len(message)+1)
    assert encrypt == message[::-1]

    with pytest.raises(TypeError, match='tipo inválido para key'):
        encrypt_message(message, '1')

    with pytest.raises(TypeError, match='tipo inválido para message'):
        encrypt_message(1, 1)
