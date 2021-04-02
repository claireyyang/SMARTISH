'''
Test the discrete action space. Specifically, test whether we can iterate
through an action space and sample from it.
'''
from smartish.actions import DiscreteActionSpace

def test_iterator():
    '''
    Test whether we can properly iterate through a discrete action
    space from 0 to size-1
    '''
    action_space : DiscreteActionSpace = DiscreteActionSpace(5)
    # A discrete action space should iterate from 0 to n-1
    # as should be the indicies when we enumerate it
    for idx, action in enumerate(action_space):
        assert idx == action

def test_equals_true():
    '''
    Test whether we can compare two equal discrete action spaces
    '''
    action_space1 : DiscreteActionSpace = DiscreteActionSpace(8)
    action_space2 : DiscreteActionSpace = DiscreteActionSpace(8)
    assert action_space1 == action_space2

def test_equals_false():
    '''
    Test whether we can compare two different discrete action spaces
    '''
    action_space1 : DiscreteActionSpace = DiscreteActionSpace(5)
    action_space2 : DiscreteActionSpace = DiscreteActionSpace(8)
    assert action_space1 != action_space2

# As this is random check that all numbers fall within
# the acceptable range
def test_sample():
    '''
    Test whether a collection of sampled values are within the
    expected range for the action space.
    '''
    action_space : DiscreteActionSpace = DiscreteActionSpace(5)
    # sample 50 times making sure all values are between 0 and 4
    for _ in range(50):
        action : int = action_space.sample()
        assert 0 <= action < 5
