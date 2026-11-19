from copy import deepcopy
from mergedeep import merge
from dorna2 import Solid
from workspace.components.factory import register


@register("scale_top_nalgene_2ml")
class ScaleTopNalgene2ml:
    """scaletop for nalgene 2ml tubes

    Measured off scale_top_nalgene_2ml.glb (mm, origin at the base, centered in XY): 82.9 x 82.9 x 36.0.
    """
    KIND = "other"

    DEFAULTS = dict(
        anchors={"body": {
            "center": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            "clb_0": [0.0, 0.0, 6.0, 0.0, 0.0, 0.0],
            "top": [0.1, 0.0, 36.0, 0.0, 0.0, 0.0],
            "place": [0.1, 0.0, 11.0, 0.0, 0.0, 0.0]
        }},
        collision_box={"body": [
            {"pose": [0.1, 0.0, 18.0, 0.0, 0.0, 0.0], "scale": [82.9, 82.9, 36.0], "padding_enabled": True}
        ]},
    )

    def __init__(self, name: str, cfg: dict, workspace, **kwargs):
        prm = deepcopy(self.DEFAULTS)
        merge(prm, cfg)
        merge(prm, kwargs)
        prm.setdefault("type", getattr(self.__class__, "_registered_type", prm.get("type")))
        self.name = name
        self.workspace = workspace
        self.type = prm["type"]
        self.assembly = {
            k: Solid(type=self.type, anchors=prm["anchors"][k], component=self.name,
                     **({"collision_box": cb[k]} if (cb := prm.get("collision_box")) and k in cb else {}))
            for k in prm["anchors"]
        }
