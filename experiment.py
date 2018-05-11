from yank.experiment import ExperimentBuilder as _ExperimentBuilder
from .utils import load_healed_yaml as _load_healed_yaml
from .utils import dump_yaml_to_str as _dump_yaml_to_str

class Experiment:

    _yaml_file    = None
    _yaml_dict    = None
    _yaml_content = None
    _yaml_builder = None

    def __init__(self,yaml_file=None,molecules_input_files=None):

        if yaml_file is not None:

            self._yaml_file    = yaml_file
            self._yaml_dict    = _load_healed_yaml(yaml_file,molecules_input_files)
            self._yaml_content = _dump_yaml_to_str(self._yaml_dict)
            #self._yaml_builder = _ExperimentBuilder(self._yaml_content)

        pass
