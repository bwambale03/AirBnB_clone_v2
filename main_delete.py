#!/usr/bin/python3
""" Test delete feature
"""
from models.engine.file_storage import FileStorage
from models.state import State

fs = FileStorage()

# Function to filter states
def get_all_states():
    all_objects = fs.all()
    return {k: v for k, v in all_objects.items() if isinstance(v, State)}

# All States initially
all_states = get_all_states()
print("All States: {}".format(len(all_states)))
for state in all_states.values():
    print(state)

# Create a new State
new_state = State()
new_state.name = "California"
fs.new(new_state)
fs.save()
print("New State: {}".format(new_state))

# All States after adding California
all_states = get_all_states()
print("All States: {}".format(len(all_states)))
for state in all_states.values():
    print(state)

# Create another State
another_state = State()
another_state.name = "Nevada"
fs.new(another_state)
fs.save()
print("Another State: {}".format(another_state))

# All States after adding Nevada
all_states = get_all_states()
print("All States: {}".format(len(all_states)))
for state in all_states.values():
    print(state)

# Delete the new State
fs.delete(new_state)
fs.save()

# All States after deletion
all_states = get_all_states()
print("All States: {}".format(len(all_states)))
for state in all_states.values():
    print(state)

