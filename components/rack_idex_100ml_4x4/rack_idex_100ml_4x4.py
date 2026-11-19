from copy import deepcopy
from mergedeep import merge
from workspace.components.factory import register
from workspace.components.rack.rack import Rack


@register("rack_idex_100ml_4x4")
class RackIdex100ml4x4(Rack):
    """Rack for the IDEX 100 mL bottles, 4x4, 250 x 250 x 25 mm: 16 pockets (dia 57.8) on a 60 mm pitch with their floors at z 3; slots at the floors. Two 4.5 mm pin holes at (+/-50, 0) take its adapter's standoffs.

    Measured off rack_idex_100ml_4x4.glb (mm, origin at the base, centered in XY): 250.0 x 250.0 x 25.0.
    """
    KIND = "rack"

    DEFAULTS = dict(
        anchors={"body": {
            "center": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            "place": [0.0, 0.0, 3.0, 0.0, 0.0, 0.0],
            "top": [0.0, 0.0, 25.0, 0.0, 0.0, 0.0]
        }},
        collision_box={"body": [
            {"pose": [0.0, 0.0, 12.5, 0.0, 0.0, 0.0], "scale": [250.0, 250.0, 25.0], "padding_enabled": True}
        ]},
        offset=[-90.0, -90.0, 3.0],
        pitch=[60.0, 60.0, 0],
        rows=['A', 'B', 'C', 'D'],
        cols=[1, 2, 3, 4],
        rvec_safe=[0.0, 0.0, 45.0],
    )

    def __init__(self, name: str, cfg: dict, workspace, **kwargs):
        prm = deepcopy(Rack.DEFAULTS)
        merge(prm, self.DEFAULTS)
        merge(prm, cfg)
        merge(prm, kwargs)
        prm.setdefault("type", getattr(self.__class__, "_registered_type", prm.get("type")))
        super().__init__(name=name, workspace=workspace, **prm)
