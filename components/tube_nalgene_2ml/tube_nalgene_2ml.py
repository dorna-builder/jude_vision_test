from copy import deepcopy
from mergedeep import merge
from workspace.components.factory import register
from workspace.components.tube.tube import Tube


@register("tube_nalgene_2ml")
class TubeNalgene2ml(Tube):
    """Custom part tube_nalgene_2ml, made in the AI builder.

    Measured off tube_nalgene_2ml.glb (mm, origin at the base, centered in XY): 13.0 x 12.9 x 45.6.
    """
    KIND = "tube"

    DEFAULTS = dict(
        anchors={"body": {
            "center": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            "top": [0.0, 0.0, 45.6, 0.0, 0.0, 0.0],
            "place": [0.0, 0.0, 41.0, 0.0, 0.0, 0.0],
            "cap_seat": [0.0, 0.0, 41.5, 0.0, 0.0, 0.0]
        }},
        collision_box={"body": [
            {"pose": [0.0, 0.0, 22.8, 0.0, 0.0, 0.0], "scale": [13.0, 12.9, 45.6], "padding_enabled": True}
        ]},
        size=[13.0, 12.9, 45.6],
    )

    def __init__(self, name: str, cfg: dict, workspace, **kwargs):
        prm = deepcopy(Tube.DEFAULTS)
        merge(prm, self.DEFAULTS)
        merge(prm, cfg)
        merge(prm, kwargs)
        prm.setdefault("type", getattr(self.__class__, "_registered_type", prm.get("type")))
        super().__init__(name=name, workspace=workspace, **prm)
