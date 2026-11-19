from copy import deepcopy
from mergedeep import merge
from workspace.components.factory import register
from workspace.components.cap.cap import Cap


@register("cap_nalgene_2ml")
class CapNalgene2ml(Cap):
    """cap for nalgene 2ml

    Measured off cap_nalgene_2ml.glb (mm, origin at the base, centered in XY): 13.0 x 13.0 x 6.5.

    Screw thread: not measured yet — bna's baseline for an unmeasured cap
    (geometry.cap_screw): rise = 0.79 x 6.5 = 5.1 mm, pitch = 3.33 x 13/26
    = 1.67 mm/turn, turns = 5.1 / 1.67 = 3.07 -> twist 1100 deg. Confirm
    on the bench and write the measured values here.
    """

    DEFAULTS = dict(
        anchors={"body": {"center": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                          "top": [0.0, 0.0, 6.5, 0.0, 0.0, 0.0]}},
        collision_box={"body": [
            {"pose": [0.0, 0.0, 3.25, 0.0, 0.0, 0.0], "scale": [13.0, 13.0, 6.5], "padding_enabled": True}
        ]},
        cap_type="screw",
        twist=1100,
        pitch=1.67,
    )

    def __init__(self, name: str, cfg: dict, workspace, **kwargs):
        prm = deepcopy(Cap.DEFAULTS)
        merge(prm, self.DEFAULTS)
        merge(prm, cfg)
        merge(prm, kwargs)
        prm.setdefault("type", getattr(self.__class__, "_registered_type", cfg.get("type")))
        super().__init__(name=name, workspace=workspace, **prm)
        self.assembly["body"].collision_box = prm["collision_box"]["body"]
