from copy import deepcopy
from mergedeep import merge
from workspace.components.factory import register
from workspace.components.cap.cap import Cap


@register("cap_idex_100ml")
class CapIdex100ml(Cap):
    """IDEX 100 mL screw cap, 40.5 mm across, 11.6 mm tall: a 1.85 mm top over a skirt about 9.75 mm deep inside. Screw estimated from bna's amber cap (rise 0.79 x height, pitch 3.33 x diameter/26): 638 deg at 5.19 mm a turn - set the real thread when known.

    Measured off cap_idex_100ml.glb (mm, origin at the base, centered in XY): 40.5 x 40.4 x 11.6.
    """
    KIND = "cap"

    DEFAULTS = dict(
        anchors={"body": {
            "center": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            "top": [0.0, 0.0, 11.6, 0.0, 0.0, 0.0]
        }},
        collision_box={"body": [
            {"pose": [0.0, 0.0, 5.8, 0.0, 0.0, 0.0], "scale": [40.5, 40.39, 11.6], "padding_enabled": True}
        ]},
        cap_type='screw',
        twist=638.0,
        pitch=5.19,
    )

    def __init__(self, name: str, cfg: dict, workspace, **kwargs):
        prm = deepcopy(Cap.DEFAULTS)
        merge(prm, self.DEFAULTS)
        merge(prm, cfg)
        merge(prm, kwargs)
        prm.setdefault("type", getattr(self.__class__, "_registered_type", prm.get("type")))
        super().__init__(name=name, workspace=workspace, **prm)
