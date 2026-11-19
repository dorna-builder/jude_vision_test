from copy import deepcopy
from mergedeep import merge
from workspace.components.factory import register
from workspace.components.adapter.adapter import Adapter


@register("adapter_plate_idex_100ml_4x4")
class AdapterPlateIdex100ml4x4(Adapter):
    """Adapter for the IDEX 100 mL 4x4 rack: the standard two-standoff bar, 100 mm apart (the model is a copy of adapter_plate_autosampler_2ml_7x8's). Origin at mid-bar, place at the holes' height, top on the top face; calibration points on fixture-plate holes (multiples of 25 mm from hole_0 / hole_1): the corners of the widest grid rectangle inside the 250 x 250 footprint and two by the centre.

    Measured off adapter_plate_idex_100ml_4x4.glb (mm, origin at the base, centered in XY): 105.0 x 5.0 x 12.0.
    """
    KIND = "adapter"

    DEFAULTS = dict(
        anchors={"body": {
            "center": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            "place": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            "top": [0.0, 0.0, 6.0, 0.0, 0.0, 0.0],
            "hole_0": [50.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            "hole_1": [-50.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            "clb_0": [100.0, 100.0, 0.0, 0.0, 0.0, 0.0],
            "clb_1": [-100.0, 100.0, 0.0, 0.0, 0.0, 0.0],
            "clb_2": [-100.0, -100.0, 0.0, 0.0, 0.0, 0.0],
            "clb_3": [100.0, -100.0, 0.0, 0.0, 0.0, 0.0],
            "clb_4": [25.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            "clb_5": [-25.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        }},
        collision_box={"body": [
            {"pose": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "scale": [105.0, 5.0, 12.0], "padding_enabled": True}
        ]},
    )

    def __init__(self, name: str, cfg: dict, workspace, **kwargs):
        prm = deepcopy(Adapter.DEFAULTS)
        merge(prm, self.DEFAULTS)
        merge(prm, cfg)
        merge(prm, kwargs)
        prm.setdefault("type", getattr(self.__class__, "_registered_type", prm.get("type")))
        super().__init__(name=name, workspace=workspace, **prm)
