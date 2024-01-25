

# generate dataset
from utils import build_dataset
args={}
args['input_csv'] = 'partition/GNN-HL.csv'
args['output_bin'] = 'partition/GNN-HL.bin'
args['output_csv'] = 'partition/GNN-HL_group.csv'

build_dataset.built_data_and_save_for_splited(
        origin_path=args['input_csv'],
        save_path=args['output_bin'],
        group_path=args['output_csv'],
        task_list_selected=None
         )

# generate dataset
from utils import build_dataset
args={}
args['input_csv'] = 'partition/GNN-KOA.csv'
args['output_bin'] = 'partition/GNN-KOA.bin'
args['output_csv'] = 'partition/GNN-KOA_group.csv'

build_dataset.built_data_and_save_for_splited(
        origin_path=args['input_csv'],
        save_path=args['output_bin'],
        group_path=args['output_csv'],
        task_list_selected=None
         )


# generate dataset
from utils import build_dataset
args={}
args['input_csv'] = 'partition/GNN-KOC.csv'
args['output_bin'] = 'partition/GNN-KOC.bin'
args['output_csv'] = 'partition/GNN-KOC_group.csv'

build_dataset.built_data_and_save_for_splited(
        origin_path=args['input_csv'],
        save_path=args['output_bin'],
        group_path=args['output_csv'],
        task_list_selected=None
         )


# generate dataset
from utils import build_dataset
args={}
args['input_csv'] = 'partition/GNN-KOW.csv'
args['output_bin'] = 'partition/GNN-KOW.bin'
args['output_csv'] = 'partition/GNN-KOW.csv'

build_dataset.built_data_and_save_for_splited(
        origin_path=args['input_csv'],
        save_path=args['output_bin'],
        group_path=args['output_csv'],
        task_list_selected=None
         )


# generate dataset
from utils import build_dataset
args={}
args['input_csv'] = 'partition/GNN-VP.csv'
args['output_bin'] = 'partition/GNN-VP.bin'
args['output_csv'] = 'partition/GNN-VP_group.csv'

build_dataset.built_data_and_save_for_splited(
        origin_path=args['input_csv'],
        save_path=args['output_bin'],
        group_path=args['output_csv'],
        task_list_selected=None
         )

# generate dataset
from utils import build_dataset
args={}
args['input_csv'] = 'partition/GNN-WS.csv'
args['output_bin'] = 'partition/GNN-WS.bin'
args['output_csv'] = 'partition/GNN-WS_group.csv'

build_dataset.built_data_and_save_for_splited(
        origin_path=args['input_csv'],
        save_path=args['output_bin'],
        group_path=args['output_csv'],
        task_list_selected=None
         )

