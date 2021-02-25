from .gfl import GFL
from .gfl_t import GFL_t
from .gfl_bbHOA_incpt_128_96 import GFL_HOA_incpt_128

def build_model(model_cfg):
    if model_cfg.arch.name == 'GFL':
        model = GFL(model_cfg.arch.backbone, model_cfg.arch.fpn, model_cfg.arch.head)
    elif model_cfg.arch.name == 'GFL_t':
        model = GFL_t(model_cfg.arch.backbone, model_cfg.arch.fpn, model_cfg.arch.head)
    elif model_cfg.arch.name == 'GFL_HOA_incpt_128':

    else:
        raise NotImplementedError
    return model
