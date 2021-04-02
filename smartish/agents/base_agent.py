'''
Base agent is the basic generic agent that is used by the generic base environment
'''


class BaseAgent:
    '''
    A class that will hold the attributes for a generic agent
    '''
    def __init__(self, agent_id: int, status: str = None) -> None:
        '''
        Constructs a BaseAgent that is used as the base class for all agents in the different simulations
        '''
        self._agent_id: int = agent_id
        self._status: str = status

    def getAgentId(self) -> int:
        return self._agent_id

    def getStatus(self) -> str:
        return self._status

    def setStatus(self, new_status: str) -> None:
        self._status = new_status
