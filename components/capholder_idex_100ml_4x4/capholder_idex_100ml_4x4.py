from copy import deepcopy
from mergedeep import merge
from workspace.components.factory import register
from workspace.components.rack.rack import Rack


@register("capholder_idex_100ml_4x4")
class CapholderIdex100ml4x4(Rack):
    """Cap holder for the IDEX 100 mL caps, 4x4, 250 x 250 x 9 mm: a 3 mm plate with 16 pegs (about 35 mm across) on a 60 mm pitch; each cap sits open side down over its peg and rests on the plate, so a slot is at z 3. Two 4.5 mm pin holes at (+/-50, 0) take its adapter's standoffs.

    Measured off capholder_idex_100ml_4x4.glb (mm, origin at the base, centered in XY): 250.0 x 250.0 x 9.0.
    """
    KIND = "capholder"

    DEFAULTS = dict(
        anchors={"body": {
            "center": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            "place": [0.0, 0.0, 3.0, 0.0, 0.0, 0.0],
            "top": [0.0, 0.0, 9.0, 0.0, 0.0, 0.0]
        }},
        collision_box={"body": [
            {"pose": [0.0, 0.0, 4.5, 0.0, 0.0, 0.0], "scale": [250.0, 250.0, 9.0], "padding_enabled": True}
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
