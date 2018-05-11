import yaml
from yank import version as yank_version
from yank.experiment import YankLoader, YankDumper
from simtk.openmm import Platform

def check_yank_old_version():

    yaml_is_old   =False
    tmp_version   =int(yank_version.version.split('.')[0])
    tmp_subversion=int(yank_version.version.split('.')[1])

    if tmp_version==0:
        if tmp_subversion>20:
            yaml_is_old=True

    return yaml_is_old

def available_openmm_platforms(verbose=True):

    if verbose:
        print("Available OpenMM platforms:")
        for platform_index in range(Platform.getNumPlatforms()):
            print("{0:5d} {1:s}".format(platform_index, Platform.getPlatform(platform_index).getName()))
        print("")
    pass

def load_healed_yaml(yaml_file,molecules_input_files=None):

    tmp_yaml=load_yaml(yaml_file)

    if check_yank_old_version():
        tmp_yaml=upgrade_yaml(tmp_yaml)

    if molecules_input_files is not None:
        for key,val in molecules_input_files.items():
            tmp_yaml['molecules'][key]=val

    return tmp_yaml

def load_yaml(yaml_file=None):

    tmp_yaml=None
    with open(yaml_file, 'r') as f:
        tmp_yaml=yaml.load(f,Loader=YankLoader)

    return tmp_yaml

def dump_yaml_to_str(yaml_dict=None):

    dump_options = {'Dumper': YankDumper, 'line_break': '\n', 'indent': 4}
    tmp_str=yaml.dump(yaml_dict,explicit_start=True, **dump_options)
    return tmp_str

def upgrade_yaml(yaml_dict=None):

    tmp_yaml = yaml_dict.copy()
    tmp_options=tmp_yaml['options']

    if 'number_of_iterations' in tmp_options:
        updated_needed=True
        tmp_options['default_number_of_iterations']=tmp_options['number_of_iterations']
        tmp_options.pop('number_of_iterations', None)

    return tmp_yaml

