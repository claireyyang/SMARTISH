'''
Test the social preference action space. Tests especially relating to converting between
an integer action and a list or matrix of boolean social preferences.
'''
from typing import List
import pytest
from smartish.actions import SocialPreferenceActionSpace, SocialPreferenceConversionError

@pytest.fixture(name='sp_action_space3')
def fixture_sp_action_space3() -> SocialPreferenceActionSpace:
    ''' Returns a social preference action space designed for 3 agents'''
    return SocialPreferenceActionSpace(3)

def test_convert_to_social_preference_list_action_too_big(sp_action_space3):
    '''
    Test whether the social preference list conversion throws an error
    if the inputted action is out of range and too big.
    '''
    with pytest.raises(SocialPreferenceConversionError):
        sp_action_space3.convert_to_social_preference_list(0,6)

def test_convert_to_social_preference_list_action_too_small(sp_action_space3):
    '''
    Test whether the social preference list conversion throws an error
    if the inputted action is out of range and too small.
    '''
    with pytest.raises(SocialPreferenceConversionError):
        sp_action_space3.convert_to_social_preference_list(0,-1)

def test_convert_to_social_preference_list_agent_id_too_big(sp_action_space3):
    '''
    Test whether the social preference list conversion throws an error
    if the inputted agent is out of range and too big.
    '''
    with pytest.raises(SocialPreferenceConversionError):
        sp_action_space3.convert_to_social_preference_list(3,3)

def test_convert_to_social_preference_list_agent_id_too_small(sp_action_space3):
    '''
    Test whether the social preference list conversion throws an error
    if the inputted agent is out of range and too small.
    '''
    with pytest.raises(SocialPreferenceConversionError):
        sp_action_space3.convert_to_social_preference_list(-1,3)

def test_convert_to_social_preference_matrix_too_many_actions(sp_action_space3):
    '''
    Test whether the social preference matrix conversion throws an error
    if too many actions are provided based on the action space size.
    '''
    with pytest.raises(SocialPreferenceConversionError):
        # Expects 3 actions.
        sp_action_space3.convert_to_social_preference_matrix([1,2,1,2])

def test_convert_to_social_preference_list_agent0(sp_action_space3):
    '''
    Test conversions from actions to a social preference list for an agent with ID 0
    '''
    pref_list : List[bool] = sp_action_space3.convert_to_social_preference_list(0, 0)
    assert pref_list == [False, False, False]
    pref_list : List[bool] = sp_action_space3.convert_to_social_preference_list(0, 1)
    assert pref_list == [False, False, True]
    pref_list : List[bool] = sp_action_space3.convert_to_social_preference_list(0, 2)
    assert pref_list == [False, True, False]
    pref_list : List[bool] = sp_action_space3.convert_to_social_preference_list(0, 3)
    assert pref_list == [False, True, True]

def test_convert_to_social_preference_list_agent1(sp_action_space3):
    '''
    Test conversions from actions to a social preference list for an agent with ID 1
    '''
    pref_list : List[bool] = sp_action_space3.convert_to_social_preference_list(1, 0)
    assert pref_list == [False, False, False]
    pref_list : List[bool] = sp_action_space3.convert_to_social_preference_list(1, 1)
    assert pref_list == [False, False, True]
    pref_list : List[bool] = sp_action_space3.convert_to_social_preference_list(1, 2)
    assert pref_list == [True, False, False]
    pref_list : List[bool] = sp_action_space3.convert_to_social_preference_list(1, 3)
    assert pref_list == [True, False, True]

def test_convert_to_social_preference_list_agent2(sp_action_space3):
    '''
    Test conversions from actions to a social preference list for an agent with ID 2
    '''
    pref_list : List[bool] = sp_action_space3.convert_to_social_preference_list(2, 0)
    assert pref_list == [False, False, False]
    pref_list : List[bool] = sp_action_space3.convert_to_social_preference_list(2, 1)
    assert pref_list == [False, True, False]
    pref_list : List[bool] = sp_action_space3.convert_to_social_preference_list(2, 2)
    assert pref_list == [True, False, False]
    pref_list : List[bool] = sp_action_space3.convert_to_social_preference_list(2, 3)
    assert pref_list == [True, True, False]

def test_convert_to_social_preference_list_big():
    '''
    Test conversions from actions to a social preference list designed for 10 agents.
    '''
    action_space : SocialPreferenceActionSpace = SocialPreferenceActionSpace(10)
    pref_list : List[bool] = action_space.convert_to_social_preference_list(0, 0)
    assert pref_list == [False]*10
    pref_list : List[bool] = action_space.convert_to_social_preference_list(0, 511)
    assert pref_list == [False] + [True]*9
    pref_list : List[bool] = action_space.convert_to_social_preference_list(0, 100)
    assert pref_list == [False, False, False, True, True, False, False, True, False, False]

def test_convert_to_social_preference_matrix_all_cooperating(sp_action_space3):
    '''
    Test conversions from actions to a social preference matrix where everyone is
    cooperating.
    '''
    pref_matrix = sp_action_space3.convert_to_social_preference_matrix([3,3,3])
    assert pref_matrix == [
        [False, True, True],
        [True, False, True],
        [True, True, False]]

def test_convert_to_social_preference_matrix_no_cooperating(sp_action_space3):
    '''
    Test conversions from actions to a social preference matrix where no one is
    cooperating.
    '''
    pref_matrix = sp_action_space3.convert_to_social_preference_matrix([0,0,0])
    assert pref_matrix == [
        [False, False, False],
        [False, False, False],
        [False, False, False]]

def test_convert_to_social_preference_matrix_some_cooperating(sp_action_space3):
    '''
    Test conversions from actions to a social preference matrix where there is
    some cooperation.
    '''
    pref_matrix = sp_action_space3.convert_to_social_preference_matrix([1,2,1])
    assert pref_matrix == [
        [False, False, True],
        [True, False, False],
        [False, True, False]]
