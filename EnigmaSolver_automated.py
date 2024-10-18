# pip install py-enigma
from enigma.machine import EnigmaMachine

# https://py-enigma.readthedocs.io/en/latest/reference.html#enigma.machine.EnigmaMachine.from_key_sheet
# config from the riddle
machine = EnigmaMachine.from_key_sheet(
    rotors='II IV I',
    reflector='C',
    ring_settings='12 15 23',
    plugboard_settings='AU SF CW EY RZ TN GP'
)

# message: FHAEGQUUDJZLZODJXYJVFASXOBYGOAK

message = input("Enter the message you recieved: ")

grundstellung = message[:3]
machine.set_display(grundstellung)

# decrypt the spruch schluessel
spruch_key_ciphertext = message[3:6]
spruch_key = machine.process_text(spruch_key_ciphertext)
print(f'Spruchschlüssel: {spruch_key}')

machine.set_display(spruch_key)

# decrypt the message (after the first six characters)
ciphertext = message[6:]
plaintext = machine.process_text(ciphertext)

print(f'Entschlüsselte Nachricht: {plaintext}')
