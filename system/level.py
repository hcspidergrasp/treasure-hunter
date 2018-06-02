from typing import List

from system.metadata import LevelMetadata
from system.scenario import Scenario


class Level:

    def __init__(self, metadata: LevelMetadata, scenarios: List[Scenario]):
        self.__metadata: LevelMetadata = metadata
        self.__scenarios: List[Scenario] = scenarios

    @property
    def metadata(self) -> LevelMetadata:
        return self.__metadata

    @property
    def scenarios(self) -> List[Scenario]:
        return self.__scenarios

    def get_scenario_by_state(self, state) -> Scenario:
        for scenario in self.__scenarios:
            if scenario.state_id is state:
                return scenario
