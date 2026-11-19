from copy import deepcopy
from mergedeep import merge
from workspace.components.factory import register
from workspace.components.tube.tube import Tube


@register("tube_idex_100ml")
class TubeIdex100ml(Tube):
    """IDEX 100 mL bottle. Body 50 mm across to z 66, shoulder to 70, neck about 37.7 mm across with its thread from z 76 to the lip at 87. Screwed on, the cap's inside top meets the lip, so the cap's base sits at 87 - 9.75 = 77.3 (cap_seat); place 1 mm under it.

    Measured off tube_idex_100ml.glb (mm, origin at the base, centered in XY): 50.0 x 49.8 x 87.0.
    """
    KIND = "tube"

    DEFAULTS = dict(
        anchors={"body": {
            "center": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            "top": [0.0, 0.0, 87.0, 0.0, 0.0, 0.0],
            "cap_seat": [0.0, 0.0, 77.3, 0.0, 0.0, 0.0],
            "place": [0.0, 0.0, 76.3, 0.0, 0.0, 0.0]
        }},
        collision_box={"body": [
            {"pose": [0.0, 0.0, 43.5, 0.0, 0.0, 0.0], "scale": [50.0, 49.79, 87.0], "padding_enabled": True}
        ]},
        size=[50.0, 49.79, 87.0],
    )

    def __init__(self, name: str, cfg: dict, workspace, **kwargs):
        prm = deepcopy(Tube.DEFAULTS)
        merge(prm, self.DEFAULTS)
        merge(prm, cfg)
        merge(prm, kwargs)
        prm.setdefault("type", getattr(self.__class__, "_registered_type", prm.get("type")))
        super().__init__(name=name, workspace=workspace, **prm)
